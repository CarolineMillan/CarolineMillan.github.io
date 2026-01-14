import os
import shutil
import sys
from textnode import TextNode, TextType
from utils import markdown_to_html_node

def main():
    if len(sys.argv) > 1:
        print(sys.argv)
        basepath = sys.argv[1]
    else:
        basepath = '/'
    copy_contents()
    generate_pages_recursive("content", "template.html", "docs", basepath)

def copy_contents():
    # recursively copy contents of static in to public
    
    # first delete everything in public
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    
    # create public again
    os.mkdir("docs")

    # write a recursive function to copy all files from static into public
    copy_contents_r("static")

def copy_contents_r(filepath):
    # get new filepath by removing static prefix and replacing it with public

    # log filepath
    print(filepath)
    print('*')

    # base case: it's a file so copy it and return
    if os.path.isfile(filepath):
        new_filepath = filepath.replace("static", "docs", 1)
        shutil.copy(filepath, new_filepath)
        return
    # recursive case: it's a folder so create a corresponding folder in public and call copy_contents_r() on everything in it
    if filepath != "static":
        new_filepath = filepath.replace("static", "docs", 1)
        print(f"new: {new_filepath}")
        os.mkdir(new_filepath)
    for file in os.listdir(filepath):
        print(f"file: {file}")
        # may need to join file and filepath
        next = os.path.join(filepath, file)
        copy_contents_r(next)

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith('#'):
            if not line[1:].startswith('#'):
                return line[1:].strip()
    raise Exception("No Title")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path, 'r')
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path, 'r')
    template = template_file.read()
    template_file.close()
    
    # use markdown_to_html_node and .to_html to convert markdown to a html string
    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()
    
    title = extract_title(markdown)

    # replace title and content in the template
    t1 = template.replace("{{ Title }}", title)
    t_content = t1.replace("{{ Content }}", html_string)
    # FIXME you've messed up this replace bit here
    t_href = t_content.replace("href=\"/", f"href=\"{basepath}")
    t2 = t_href.replace("src=\"/", f"src=\"{basepath}")
    
    #print(t2)
    # Extract the directory path from the full file path
    dest_dir = os.path.dirname(dest_path)

    # Create the directory (and any parent directories) if they don't exist
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    # Now you can safely write the file
    dest_file = open(dest_path, 'w')
    dest_file.write(t2)
    dest_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # generate_page() for each page in dir_path_content into dest_dir_path
    list = os.listdir(dir_path_content)
    for thing in list:
        if thing[-2:] == "md":
            new_thing = thing[:-2] + "html"
            dest_path = os.path.join(dest_dir_path,new_thing)
        else:
            dest_path = os.path.join(dest_dir_path,thing)
        dir_path = os.path.join(dir_path_content, thing)
        # only generate a page if its a file, not a directory
        # if it's a direvtory then recurse!
        
        if os.path.isfile(dir_path):
            generate_page(dir_path, template_path, dest_path, basepath)
        else:
            # make the directory here first
            os.mkdir(dest_path)
            generate_pages_recursive(dir_path, template_path, dest_path, basepath)

if __name__ == "__main__":
    main()