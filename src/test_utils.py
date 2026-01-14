import unittest

from main import extract_title
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from utils import markdown_to_html_node, text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes, markdown_to_blocks, block_to_block_type, BlockType
# you could do more of all of these tests
class TestUtils(unittest.TestCase):
    # you could add more tests for this function
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    # add tests for split nodes delimiter
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        test_nodes = [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ]
        self.assertListEqual(
            test_nodes,
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and another [second link](https://youtube.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        test_nodes = [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second link", TextType.LINK, "https://youtube.com"
                ),
            ]
        self.assertListEqual(
            test_nodes,
            new_nodes,
        )
        
    def test_text_to_textnodes(self):
        expected_nodes = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.PLAIN),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        
        test_nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")

        self.assertListEqual(
            test_nodes,
            expected_nodes,
        )
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_blocks_to_block_type_h1(self):
        
        blocks = "# heading 1"
        blocktype = block_to_block_type(blocks)
        self.assertEqual(
            blocktype,
            BlockType.HEADING,
        )

    def test_blocks_to_block_type_nh1(self):
        
        blocks = "#heading 1"
        blocktype = block_to_block_type(blocks)
        self.assertNotEqual(
            blocktype,
            BlockType.HEADING,
        )
    def test_blocks_to_block_type_h2(self):
        
        blocks = "## heading 2"
        blocktype = block_to_block_type(blocks)
        self.assertEqual(
            blocktype,
            BlockType.HEADING,
        )

    def test_blocks_to_block_type_nh2(self):
        
        blocks = "##heading 2"
        blocktype = block_to_block_type(blocks)
        self.assertNotEqual(
            blocktype,
            BlockType.HEADING,
        )
    def test_blocks_to_block_type_h3(self):
        
        blocks = "### heading 3"
        blocktype = block_to_block_type(blocks)
        self.assertEqual(
            blocktype,
            BlockType.HEADING,
        )

    def test_blocks_to_block_type_nh3(self):
        
        blocks = "###heading 3"
        blocktype = block_to_block_type(blocks)
        self.assertNotEqual(
            blocktype,
            BlockType.HEADING,
        )
    def test_blocks_to_block_type_h4(self):
        
        blocks = "#### heading 4"
        blocktype = block_to_block_type(blocks)
        self.assertEqual(
            blocktype,
            BlockType.HEADING,
        )

    def test_blocks_to_block_type_nh4(self):
        
        blocks = "#### "
        blocktype = block_to_block_type(blocks)
        self.assertNotEqual(
            blocktype,
            BlockType.HEADING,
        )
    def test_blocks_to_block_type_h5(self):
        
        blocks = "##### heading 5"
        blocktype = block_to_block_type(blocks)
        self.assertEqual(
            blocktype,
            BlockType.HEADING,
        )

    def test_blocks_to_block_type_nh5(self):
        
        blocks = "#####"
        blocktype = block_to_block_type(blocks)
        self.assertNotEqual(
            blocktype,
            BlockType.HEADING,
        )
    def test_blocks_to_block_type_h6(self):
        
        blocks = "###### heading 6"
        blocktype = block_to_block_type(blocks)
        self.assertEqual(
            blocktype,
            BlockType.HEADING,
        )

    def test_blocks_to_block_type_nh6(self):
        
        blocks = "######heading 6"
        blocktype = block_to_block_type(blocks)
        self.assertNotEqual(
            blocktype,
            BlockType.HEADING,
        )
    def test_blocks_to_block_type_code(self):
        
        blocks = "```cat hello world```"
        blocktype = block_to_block_type(blocks)
        self.assertEqual(
            blocktype,
            BlockType.CODE,
        )

    def test_blocks_to_block_type_ncode1(self):
        
        blocks = "```cat hello world"
        blocktype = block_to_block_type(blocks)
        self.assertNotEqual(
            blocktype,
            BlockType.CODE,
        )
    
    def test_blocks_to_block_type_ncode2(self):
        
        blocks = "```cat hello world``"
        blocktype = block_to_block_type(blocks)
        self.assertNotEqual(
            blocktype,
            BlockType.CODE,
        )
    
    def test_blocks_to_block_type_ncode3(self):
        
        blocks = "'''cat hello world"
        blocktype = block_to_block_type(blocks)
        self.assertNotEqual(
            blocktype,
            BlockType.CODE,
        )
    
    def test_blocks_to_block_type_quote(self):
        
        blocks = ">quote1\n>quote 2\n>quote3"
        blocktype = block_to_block_type(blocks)
        self.assertEqual(
            blocktype,
            BlockType.QUOTE,
        )

    def test_blocks_to_block_type_nquote1(self):
        
        blocks = ">quote1\nquote 2\n>quote3"
        blocktype = block_to_block_type(blocks)
        self.assertNotEqual(
            blocktype,
            BlockType.QUOTE,
        )

    def test_blocks_to_block_type_uolist(self):
        
        blocks = "- thing 1\n- thing 2\n- thing 3"
        blocktype = block_to_block_type(blocks)
        self.assertEqual(
            blocktype,
            BlockType.UNORDERED_LIST,
        )

    def test_blocks_to_block_type_nuolist1(self):
        
        blocks = "- thing 1\n-thing 2\n- thing 3"
        blocktype = block_to_block_type(blocks)
        self.assertNotEqual(
            blocktype,
            BlockType.UNORDERED_LIST,
        )

    def test_blocks_to_block_type_nuolist2(self):
        
        blocks = "- thing 1\n- thing 2\n - thing 3"
        blocktype = block_to_block_type(blocks)
        self.assertNotEqual(
            blocktype,
            BlockType.UNORDERED_LIST,
        )

    def test_blocks_to_block_type_olist(self):
        
        blocks = "1. thing 1\n2. thing 2\n3. thing 3"
        blocktype = block_to_block_type(blocks)
        self.assertEqual(
            blocktype,
            BlockType.ORDERED_LIST,
        )

    def test_blocks_to_block_type_nolist1(self):
        
        blocks = "1. thing 1\n2 thing 2\n3. thing 3"
        blocktype = block_to_block_type(blocks)
        self.assertNotEqual(
            blocktype,
            BlockType.ORDERED_LIST,
        )

    def test_blocks_to_block_type_nolist2(self):
        
        blocks = "1. thing 1\n3. thing 2\n2. thing 3"
        blocktype = block_to_block_type(blocks)
        self.assertNotEqual(
            blocktype,
            BlockType.ORDERED_LIST,
        )
        
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quoteblock(self):
        md = """
>This is a single quote line
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a single quote line</blockquote></div>",
        )

    def test_quoteblock2(self):
        md = """
>This is a single quote line.
>This is a single quote line.
>This is a single quote line.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a single quote line. This is a single quote line. This is a single quote line.</blockquote></div>",
        )

    def test_ullist(self):
        md = """
- This is a ul line
- This is another ul line
- And another
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a ul line</li><li>This is another ul line</li><li>And another</li></ul></div>",
        )

    def test_ullist(self):
        md = """
1. This is a ul line
2. This is another ul line
3. And another
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is a ul line</li><li>This is another ul line</li><li>And another</li></ol></div>",
        )
    
    def test_extract_title(self):
        md = "# Hello"

        title = extract_title(md)
        self.assertEqual(
            title,
            "Hello",
        )
    
    def test_extract_title2(self):
        md = "## Hello"

        with self.assertRaises(Exception):
            title = extract_title(md)


if __name__ == "__main__":
    unittest.main()
