from copy_full_directory import copy_complete_dir
from recursive_generate_page import generate_pages_recursive

def main():
    copy_complete_dir("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()