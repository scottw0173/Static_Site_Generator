import os
from extracting_markdown import extract_title
from markdown_to_html_node import markdown_to_html_node

def generate_page(from_path, template_path, dest_path,basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    title = extract_title(markdown)
    content_html = markdown_to_html_node(markdown).to_html()

    full_html = template.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", content_html)
    full_html = full_html.replace('href="/','href="{basepath}')
    full_html = full_html.replace('src="/','src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)
