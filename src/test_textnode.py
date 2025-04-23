import unittest

from converters import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("this is different", TextType.BOLD)
        node4 = TextNode("this is different", TextType.IMAGE)
        node5 = TextNode("this is different", TextType.IMAGE, "youtube.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node4, node5)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        node1 = TextNode("Bad Image", TextType.IMAGE, "https://hi.com/image.png")
        html1_node = text_node_to_html_node(node1)
        self.assertEqual(html1_node.children, None)
        self.assertEqual(html1_node.to_html(), "<img src=\"https://hi.com/image.png\" alt=\"Bad Image\"></img>")

    def test_converter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

if __name__ == "__main__":
    unittest.main()