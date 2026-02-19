import unittest

from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes  # <-- change this to your module name


class TestTextToTextNodes(unittest.TestCase):
    def test_full_example(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` and an "
            "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a "
            "[link](https://boot.dev)"
        )

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertListEqual(expected, text_to_textnodes(text))

    def test_plain_text_only(self):
        text = "Just plain text."
        expected = [TextNode("Just plain text.", TextType.TEXT)]
        self.assertListEqual(expected, text_to_textnodes(text))

    def test_multiple_bold_sections(self):
        text = "A **bold** and **bolder** day"
        expected = [
            TextNode("A ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("bolder", TextType.BOLD),
            TextNode(" day", TextType.TEXT),
        ]
        self.assertListEqual(expected, text_to_textnodes(text))

    def test_multiple_links(self):
        text = "Links: [one](https://a.com) and [two](https://b.com)!"
        expected = [
            TextNode("Links: ", TextType.TEXT),
            TextNode("one", TextType.LINK, "https://a.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("two", TextType.LINK, "https://b.com"),
            TextNode("!", TextType.TEXT),
        ]
        self.assertListEqual(expected, text_to_textnodes(text))

    def test_images_and_text(self):
        text = "![a](https://a.png) mid ![b](https://b.png)"
        expected = [
            TextNode("a", TextType.IMAGE, "https://a.png"),
            TextNode(" mid ", TextType.TEXT),
            TextNode("b", TextType.IMAGE, "https://b.png"),
        ]
        self.assertListEqual(expected, text_to_textnodes(text))

    def test_non_nested_rule_example(self):
        text = "This is _italic and **bold** word_."
        with self.assertRaises(Exception):
            text_to_textnodes(text)

    def test_unmatched_bold_raises(self):
        text = "This is **broken"
        with self.assertRaises(Exception):
            text_to_textnodes(text)

    def test_unmatched_code_raises(self):
        text = "This is `broken"
        with self.assertRaises(Exception):
            text_to_textnodes(text)


if __name__ == "__main__":
    unittest.main()