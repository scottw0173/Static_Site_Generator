
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned = []
    for block in blocks:
        block = block.strip()
        if block != "":
            cleaned.append(block)
    return cleaned

