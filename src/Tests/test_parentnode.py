from htmlnode import ParentNode, LeafNode, HTMLNode
import unittest

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
            "<div><span><b>grandchild</b></span></div>",)

    def test_to_html_basic_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_props(self):
        node = ParentNode(
            "p",
            [LeafNode(None, "Hello")],
            props={"class": "greeting", "id": "main"},
        )
        html = node.to_html()

        # Because dict order might vary, accept either ordering
        option1 = '<p class="greeting" id="main">Hello</p>'
        option2 = '<p id="main" class="greeting">Hello</p>'
        self.assertIn(html, (option1, option2))

    def test_to_html_nested_parent_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode("p", [LeafNode(None, "Paragraph")]),
                ParentNode("span", [LeafNode("b", "Bold")]),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><p>Paragraph</p><span><b>Bold</b></span></div>",
        )

    def test_to_html_deeply_nested(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "A "),
                        ParentNode("span", [LeafNode(None, "nested")]),
                        LeafNode(None, " node"),
                    ],
                )
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><p>A <span>nested</span> node</p></div>",
        )

    def test_raises_when_tag_is_none(self):
        node = ParentNode(
            None,
            [LeafNode(None, "Hello")],
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_raises_when_children_is_none(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_children_must_render_via_to_html(self):
        # Ensures recursion is used and not str(child) / repr(child)
        node = ParentNode("p", [LeafNode("b", "X")])
        self.assertEqual(node.to_html(), "<p><b>X</b></p>")


if __name__ == "__main__":
    unittest.main()
