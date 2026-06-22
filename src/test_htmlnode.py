import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test1(self):
        node1 = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"}).props_to_html()
        node2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node1, node2)
    
    def test2(self):
        node1 = HTMLNode(None, None, None,  None).props_to_html()
        node2 = ""
        self.assertEqual(node1, node2)
        
    def test3(self):
        node1 = HTMLNode(None, None, None,  None).props_to_html()
        node2 = ' href="https://www.google.com" target="_blank"'
        self.assertNotEqual(node1, node2)
    
    
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        

class TestParentNode(unittest.TestCase):
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