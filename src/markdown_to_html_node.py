from htmlnode import ParentNode, LeafNode
from blocktype import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from text_node_to_html_node import text_node_to_html_node
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            text = " ".join(block.split("\n"))
            html_nodes.append(ParentNode("p", text_to_children(text)))

        elif block_type == BlockType.HEADING:
            level = 0
            while level < len(block) and block[level] == "#":
                level += 1
            text = block[level + 1:]  # assumes "#... " (space)
            html_nodes.append(ParentNode(f"h{level}", text_to_children(text)))

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned = [line[1:].lstrip() for line in lines]
            text = " ".join(cleaned)
            html_nodes.append(ParentNode("blockquote", text_to_children(text)))

        elif block_type == BlockType.UNORDERED_LIST:
            items = []
            for line in block.split("\n"):
                item_text = line[2:]
                items.append(ParentNode("li", text_to_children(item_text)))
            html_nodes.append(ParentNode("ul", items))

        elif block_type == BlockType.ORDERED_LIST:
            items = []
            list_inventory = block.split("\n")
            for i in range(1, len(list_inventory) + 1):
                line = list_inventory[i - 1]
                prefix = f"{i}. "
                item_text = line[len(prefix):]
                items.append(ParentNode("li", text_to_children(item_text)))
            html_nodes.append(ParentNode("ol", items))

        elif block_type == BlockType.CODE:
            code_text = block[len("```\n"):-len("```")]
            code_node = ParentNode("code", [LeafNode(None, code_text)])
            pre_node = ParentNode("pre", [code_node])
            html_nodes.append(pre_node)

        else:
            raise ValueError(f"Unknown block type: {block_type}")

    return ParentNode("div", html_nodes)

def text_to_children(text):
    list_of_textnodes = text_to_textnodes(text)
    list_of_htmlnodes = []
    for node in list_of_textnodes:
        list_of_htmlnodes.append(text_node_to_html_node(node))
    return list_of_htmlnodes