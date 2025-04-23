import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("this is different", TextType.BOLD)
        node4 = TextNode("this is different", TextType.IMG)
        node5 = TextNode("this is different", TextType.IMG, "youtube.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node4, node5)

if __name__ == "__main__":
    unittest.main()