from markdown_to_blocks import markdown_to_blocks

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        lines = block.split('\n')
        for line in lines:
            if line.startswith('#') and line[1:].startswith(' '):
                title = line[1:].strip()
                return title
    raise Exception("Missing h1 header")