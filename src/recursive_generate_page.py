import os
from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path) -> None:
    """
    Recursively walk dir_path_content. For each .md file, generate an .html file
    in dest_dir_path with the same relative path.
    """
    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, entry)

        if os.path.isdir(src_path):
            # Recurse into subdirectory
            new_dest_dir = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(src_path, template_path, new_dest_dir)

        elif os.path.isfile(src_path) and entry.endswith(".md"):
            # Convert .md -> .html filename
            filename_no_ext = entry[:-3]  # remove ".md"
            dest_path = os.path.join(dest_dir_path, f"{filename_no_ext}.html")

            generate_page(src_path, template_path, dest_path)