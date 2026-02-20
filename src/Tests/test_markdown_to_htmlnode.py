import unittest
from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLnodes(unittest.TestCase):
    # --- Provided starter tests (formatted properly) ---

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_level_1(self):
        md = """
# Heading one
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>Heading one</h1></div>")

    def test_heading_level_3_with_inline(self):
        md = """
### A **bold** move
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h3>A <b>bold</b> move</h3></div>")

    def test_quote_block(self):
        md = """
> This is a quote
> that spans lines
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        # Newlines inside quote blocks become spaces (common approach)
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote that spans lines</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- first item
- second item with **bold**
- third item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul>"
            "<li>first item</li>"
            "<li>second item with <b>bold</b></li>"
            "<li>third item</li>"
            "</ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. first
2. second with _italic_
3. third
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol>"
            "<li>first</li>"
            "<li>second with <i>italic</i></li>"
            "<li>third</li>"
            "</ol></div>",
        )

    def test_multiple_blocks_mixed(self):
        md = """
# Title

This is a paragraph with a [link](https://boot.dev) and an ![img](https://x.com/a.png)

- item one
- item two
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<h1>Title</h1>"
            "<p>This is a paragraph with a <a href=\"https://boot.dev\">link</a> and an <img src=\"https://x.com/a.png\" alt=\"img\"></img></p>"
            "<ul><li>item one</li><li>item two</li></ul>"
            "</div>",
        )

    def test_paragraph_preserves_inline_code(self):
        md = """
Use `x = 1` here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>Use <code>x = 1</code> here</p></div>")



if __name__ == "__main__":
    unittest.main()