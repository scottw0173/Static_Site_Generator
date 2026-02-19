from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        for alt, url in images:
            markdown = f"![{alt}]({url})"
            parts = text.split(markdown, 1)
            if len(parts) != 2:
                raise Exception("Invalid markdown image syntax")

            before, after = parts

            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            text = after  # keep processing the remainder

        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        links = extract_markdown_links(node.text)

        if len(links) == 0:
            new_nodes.append(node)
            continue

        for alt, url in links:
            markdown = f"[{alt}]({url})"
            parts = text.split(markdown, 1)
            if len(parts) != 2:
                raise Exception("Invalid markdown syntax for URL")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, url))
            text = parts[1]
        if text != "":
            new_nodes.append(TextNode(text,TextType.TEXT))
    return new_nodes
        