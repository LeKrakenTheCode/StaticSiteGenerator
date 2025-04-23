import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test(self):
        node = HTMLNode()
        node1 = HTMLNode("a", "TestLink")
        node2 = HTMLNode("a", value=None, children=None, props={"target": "_blank", "href": "https://youtube.com"})
        self.assertIsNotNone(str(node))
        self.assertIsNotNone(node2.props_to_html())
        self.assertEqual(node1.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

if __name__ == "__main__":
    unittest.main()