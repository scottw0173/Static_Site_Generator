from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    delimiter_dic = {'**': TextType.BOLD,
                     '_': TextType.ITALIC,
                     '`': TextType.CODE,
                     }
    new_nodes= []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        separated_text = node.text.split(delimiter)
        if len(separated_text) == 1:
            new_nodes.append(node)
            continue
        if len(separated_text) % 2 ==0:
            raise Exception(f'Invalid Markdown Syntax: missing closing delimiter "{delimiter}"')
        for i in range(len(separated_text)):
            if separated_text[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(separated_text[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(separated_text[i], text_type))
   # print(f'THIS IS THE RETURNED LIST OF NODES: {new_nodes}')        
    return new_nodes

split_nodes_delimiter([TextNode('This is text with a **bolded phrase** in the middle',TextType.TEXT)], '**', TextType.BOLD)