import unittest
from textnode import TextNode, TextType
from split_nodes_linksandimages import split_nodes_image, split_nodes_link

class TestSplitImagesLinks(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_images_starts_with_image(self):
        node = TextNode(
            "![img](https://x.com/a.png) then text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("img", TextType.IMAGE, "https://x.com/a.png"),
                TextNode(" then text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_ends_with_image(self):
        node = TextNode(
            "text then ![img](https://x.com/a.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("text then ", TextType.TEXT),
                TextNode("img", TextType.IMAGE, "https://x.com/a.png"),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode("just text", TextType.TEXT)
        self.assertListEqual([node], split_nodes_image([node]))

    def test_split_links_multiple(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )

    def test_split_links_starts_with_link(self):
        node = TextNode("[x](https://x.com) end", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("x", TextType.LINK, "https://x.com"),
                TextNode(" end", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_non_text_nodes_untouched(self):
        node = TextNode("bold", TextType.BOLD)
        self.assertListEqual([node], split_nodes_image([node]))
        self.assertListEqual([node], split_nodes_link([node]))

if __name__ == "__main__":
    unittest.main()