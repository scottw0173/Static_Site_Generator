import unittest

from extract_markdown_images import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    # -------- Images --------
    def test_extract_markdown_images_single(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "Text ![rick roll](https://i.imgur.com/aKaOqIh.gif) and "
            "![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            matches,
        )

    def test_extract_markdown_images_none(self):
        matches = extract_markdown_images("No images here, just text.")
        self.assertListEqual([], matches)

    # -------- Links --------
    def test_extract_markdown_links_single(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and "
            "[to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )

    def test_extract_markdown_links_none(self):
        matches = extract_markdown_links("No links here.")
        self.assertListEqual([], matches)

    # -------- Mixed / edge cases --------
    def test_extract_markdown_links_does_not_capture_images(self):
        # Many regex patterns accidentally capture the [alt](url) part of images as links.
        matches = extract_markdown_links(
            "An image ![alt](https://img.com/a.png) and a link [x](https://x.com)"
        )
        self.assertListEqual([("x", "https://x.com")], matches)

    def test_extract_markdown_images_does_not_capture_links(self):
        matches = extract_markdown_images(
            "A link [x](https://x.com) and an image ![alt](https://img.com/a.png)"
        )
        self.assertListEqual([("alt", "https://img.com/a.png")], matches)


if __name__ == "__main__":
    unittest.main()