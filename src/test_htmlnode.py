import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init_sets_fields(self):
        node = HTMLNode(
            tag="p",
            value="hello",
            children=None,
            props={"class": "greeting", "id": "p1"},
        )
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "hello")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"class": "greeting", "id": "p1"})

    def test_defaults_are_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props_to_html_none(self):
        node = HTMLNode(tag="p", value="hi", props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_multiple(self):
        node = HTMLNode(
            tag="a",
            value="boot.dev",
            props={"href": "https://www.boot.dev", "target": "_blank"},
        )

        html = node.props_to_html()

        # Order in dicts is usually insertion order, but don't rely on it.
        # So assert substrings rather than exact full string.
        self.assertIn(' href="https://www.boot.dev"', html)
        self.assertIn(' target="_blank"', html)
        # Should start with a space if non-empty
        self.assertTrue(html.startswith(" "))

    def test_repr_contains_fields(self):
        node = HTMLNode(
            tag="p",
            value="hello",
            children=[],
            props={"class": "greeting"},
        )
        r = repr(node)

        # Don't overfit exact formatting unless your assignment demands it.
        self.assertIn("HTMLNode", r)
        self.assertIn("p", r)
        self.assertIn("hello", r)
        self.assertIn("greeting", r)

if __name__ == "__main__":
    unittest.main()
