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

if __name__ == "__main__":
    unittest.main()