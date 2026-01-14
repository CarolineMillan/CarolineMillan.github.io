from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
import re
from enum import Enum

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.PLAIN:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            props = {"href":text_node.url}
            return LeafNode(tag="a", value=text_node.text, props=props)
        case TextType.IMAGE:
            props = {
                "src":text_node.url,
                "alt":text_node.text
                }
            return LeafNode(tag="img", value="", props=props)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # splits old nodes of textType.PLAIN into new nodes given a text_type
    ans = []
    for node in old_nodes:
        # split on the delimiter
        new_texts = node.text.split(delimiter)
        # check there was a closing delimiter by checking that the number of new_texts is odd
        if len(new_texts) % 2 == 0:
            raise Exception(f"Invalid markdown syntax. {text_type} has no closing delimiter {delimiter}")
        # create new nodes 
        for i in range(len(new_texts)):
            # THIS BIT HERE: we want == 0 for non-code blocks, but != 0 for code blocks (or that is the way to get it to work with the way I've coded it, I have probably gone wrong somewhere else tbh)
            # also, check for i==0
            
            # why is text_type code overwriting everything?
            # it's the last one I call
            # so I want to change this so that if I'm not in a delimiter block then I don't change the type
            if (i % 2 != 0): #& i != 0:
                type = text_type
            else:
                type = node.text_type#TextType.PLAIN
            new_node = TextNode(new_texts[i], type, node.url)
            ans.append(new_node)
    return ans

def extract_markdown_images(text):
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regex, text)
    
def extract_markdown_links(text):
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regex, text)

def split_nodes_image(old_nodes):
    ans = []
    for node in old_nodes:
        # extract all images
        images = extract_markdown_images(node.text)
        current_text = node.text
        # if there are no images in the node, just return the original node
        if len(images) == 0:
            ans.append(node)
            continue
        # split on each image then append head append image to ans
        for image in images:
            delimiter = f"![{image[0]}]({image[1]})"
            not_images = current_text.split(delimiter, 1)
            current_text = not_images[1]
            # TODO check for emptiness
            head = TextNode(text=not_images[0], text_type=TextType.PLAIN)
            image_node = TextNode(text=image[0], text_type=TextType.IMAGE, url=image[1])
            ans.append(head)
            ans.append(image_node)
        if current_text:
                    ans.append(TextNode(text=current_text, text_type=TextType.PLAIN))
    return ans

def split_nodes_link(old_nodes):
    ans = []
    for node in old_nodes:
        # extract all images
        links = extract_markdown_links(node.text)
        current_text = node.text
        # if there are no images in the node, just return the original node
        if len(links) == 0:
            ans.append(node)
            continue
        # split on each image then append head append image to ans
        for link in links:
            delimiter = f"[{link[0]}]({link[1]})"
            not_links = current_text.split(delimiter, 1)
            current_text = not_links[1]
            # TODO check for emptiness
            head = TextNode(text=not_links[0], text_type=TextType.PLAIN)
            link_node = TextNode(text=link[0], text_type=TextType.LINK, url=link[1])
            ans.append(head)
            ans.append(link_node)
        if current_text:
            ans.append(TextNode(text=current_text, text_type=TextType.PLAIN))
    return ans

def text_to_textnodes(text):
    # use all the split functions one after the other
    # we start with PLAIN
    plain = [TextNode(text=text, text_type=TextType.PLAIN)]
    # get BOLD
    bold = split_nodes_delimiter(plain, "**", TextType.BOLD)
    # ITALIC
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    # CODE
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    # LINK
    link = split_nodes_link(code)
    # IMAGE
    image = split_nodes_image(link)
    return image

def markdown_to_blocks(markdown):
    split = markdown.split("\n\n")
    blocks = []
    for thing in split:
        block = thing.strip()
        if block != "":
            blocks.append(block)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    match(markdown[0]):
        case '#':
            # headings start with 1-6 '#' followed by a space and the heading text
            # count # symbols
            i = 0
            while i < 6:
                if len(markdown) > i:
                    if markdown[i] != '#':
                        break
                    i += 1
                else:
                    break
            
            # check for a space
            # check for heading text
            if len(markdown) > i+1 and markdown[i] == " ":
                return BlockType.HEADING
        case '`':
            # block must start and end with three '`'
            # check that the length is at least 6
            # check that it starts and ends with '```'
            if len(markdown) >= 6:
                if markdown[:3] == "```":
                    if markdown[-3:] == "```":
                        return BlockType.CODE
        case '>':
            # every line must start with a '<'
            lines = markdown.split('\n')
            bad = False
            for line in lines:
                if line[0] != '>':
                    bad = True
            if not bad:
                return BlockType.QUOTE
        case '-':
            # every line must start with a '-' and a space
            lines = markdown.split('\n')
            bad = False
            for line in lines:
                if line[:2] != "- ":
                    bad = True
            if not bad:
                return BlockType.UNORDERED_LIST
        case '1':
            # check that every line starts with a number followed by a '.', the numbers must be ascending
            lines = markdown.split('\n')
            bad = False
            i = 1
            for line in lines:
                if line[:2] != f"{i}.":
                    bad = True
                i += 1
            if not bad:
                return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH
        
    # else it's a normal paragraph
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        # determine block type
        type = block_to_block_type(block)
        # match on block type to create the relevant html node (seperate helper func for each one)
        # a block is just a block of text, so use text_to_text_nodes then for each text_node use text_node_to_html_node (be aware of children -- is this something you need to consider?)
        match type:
            case BlockType.PARAGRAPH:
                html_node0 = paragraph_block_to_html_node(block)
                html_node = assign_children_to_html_node(html_node0)
            case BlockType.HEADING:
                html_node0 = heading_block_to_html_node(block)
                html_node = assign_children_to_html_node(html_node0)
            case BlockType.CODE:
                html_node = code_block_to_html_node(block)
            case BlockType.QUOTE:
                html_node0 = quote_block_to_html_node(block)
                html_node = assign_children_to_html_node(html_node0)
            case BlockType.UNORDERED_LIST:
                html_node = unordered_list_block_to_html_node(block)
            case BlockType.ORDERED_LIST:
                html_node = ordered_list_block_to_html_node(block)
        # assign children to this html node (use a helper function that does text_to_textnodes and text_node_to_html_node)
        # ie get the children for this html_node (recursively?)

        # add this node to the list of children
        children.append(html_node)
    # make all block nodes children of one parent div html node (helper function)
    final_node = ParentNode("div", children)
    return final_node

def paragraph_block_to_html_node(block):
    lines = block.split('\n')
    value = ' '.join(line.strip() for line in lines if line.strip())
    return HTMLNode("p", value)

def heading_block_to_html_node(block):
    count = 0 
    while block[count] == '#':
        count += 1
    tag = f"h{count}"
    value = block[count+1:] # + 1 to get rid of the space 
    return HTMLNode(tag, value)

def code_block_to_html_node(block):
    value = block[3:-3]
    if value[0] == '\n':
        value = value[1:]
    #if value[-1] == '\n':
    #    value = value[:-1]
    child = LeafNode("code", value)
    parent = ParentNode("pre", [child])
    return parent

def quote_block_to_html_node(block):
    # get rid of the > on every line
    lines = block.split('\n')
    value = ""
    #for line in lines:
    #    value += ' ' + line[1:]
    value = ' '.join(line[1:] for line in lines)
    stripped = value.lstrip()
    return HTMLNode("blockquote", stripped)

def unordered_list_block_to_html_node(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        # extract text after '-'
        text = line.lstrip()
        if not text.startswith("-"):
            continue
        text = text[1:]
        if text.startswith(" "):
            text = text[1:]
        html_node = LeafNode("li", text)
        item = assign_children_to_html_node(html_node)
        items.append(item)
    ul = ParentNode("ul", items)
    return ul

def ordered_list_block_to_html_node(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        text = line.lstrip()
        # assuming lines start with "1. " / "2. " etc, or just something like that
        # if your block_to_block_type guarantees "- " vs "1. ", you should strip the prefix appropriately
        text = text.split(".", 1)[1].lstrip()   # or similar logic
        li_plain = HTMLNode("li", text)
        li_node = assign_children_to_html_node(li_plain)
        items.append(li_node)
    return ParentNode("ol", items)

def assign_children_to_html_node(html_node):
    # take html_node.val and use text_to_text_nodes and text_node_to_html_node to turn val into child nodes
    text_nodes = text_to_textnodes(html_node.value)
    children = []
    for thing in text_nodes:
        child = text_node_to_html_node(thing)
        # do it recursively? You'll need a base case
        # try no recursion for now. I'm not convinced you need it
        # we do one round of splitting the markdown into blocks, then another round of splitting the text into inline blocks
        # this is just round 2, so all children are on the same level
        # this might be an area to expand in future? This is probably simplified compared to Hugo or Jekyll
        children.append(child)
    parent = ParentNode(html_node.tag, children, html_node.props)
    return parent