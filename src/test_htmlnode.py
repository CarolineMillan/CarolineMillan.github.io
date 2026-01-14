import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        # this is the test that is failing, the only one
        blank_node = HTMLNode()
        children = []
        props = {"testing": 1}
        node = HTMLNode("a", "this is the string inside a.", children, props)
        node2 = HTMLNode("a", "this is the string inside a.", children, props)
        self.assertEqual(node, node2)
    
    def test_eq_none(self):
        # this is the test that is failing, the only one
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_neq1(self):
        blank_node = HTMLNode()
        children = [blank_node]
        props = {"testing": 1}
        node = HTMLNode("a", "this is the string inside a.", children, props)
        node2 = HTMLNode("a", "this is another string inside a.", children, props)
        self.assertNotEqual(node, node2)
        
    def test_neq2(self):
        blank_node = HTMLNode()
        not_blank_node = HTMLNode(tag="p")
        children = [blank_node]
        children2 = [not_blank_node]
        props = {"testing": 1}
        node = HTMLNode("a", "this is the string inside a.", children, props)
        node2 = HTMLNode("a", "this is the string inside a.", children2, props)
        self.assertNotEqual(node, node2)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_a(self):
        props = {"href": "https://boot.dev"}
        node = LeafNode("a", "Hello, world!", props)
        self.assertEqual(node.to_html(), "<a href=\"https://boot.dev\">Hello, world!</a>")
    
    # you could definitely add more parent node tests here
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        

if __name__ == "__main__":
    unittest.main()