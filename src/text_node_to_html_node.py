from enum import Enum
from htmlnode import LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        if text_node.text_type == TextType.BOLD:
            return LeafNode(tag='b',value=text_node.text)
        if text_node.text_type == TextType.ITALIC:
            return LeafNode(tag='i',value=text_node.text)
        if text_node.text_type == TextType.CODE:
            return LeafNode(tag='code',value=text_node.text)
        if text_node.text_type == TextType.LINK:
            if text_node.url is None:
                 raise ValueError("Link TextNode must have a url")
            return LeafNode(tag='a', value=text_node.text, props={'href': text_node.url})
        if text_node.text_type == TextType.IMAGE:
            if text_node.url is None:
                 raise ValueError("Image TextNode must have a url")
            return LeafNode(tag='img',value=None,props={'src': text_node.url, 'alt': text_node.text})
        return Exception(f'Unsupported TextType: {text_node.text_type}')
             
        