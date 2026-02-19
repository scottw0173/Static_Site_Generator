from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_linksandimages import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    text = [TextNode(text, TextType.TEXT)]
    text_after_images = split_nodes_image(text)
    text_after_links = split_nodes_link(text_after_images)
    text_after_bold = split_nodes_delimiter(text_after_links, "**", TextType.BOLD)
    text_after_italic = split_nodes_delimiter(text_after_bold, "_", TextType.ITALIC)
    text_after_code = split_nodes_delimiter(text_after_italic, "`", TextType.CODE)
   # for list in text_after_code:
   #     print(f"\n{list}")
    return text_after_code

