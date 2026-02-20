import sys
from copy_full_directory import copy_complete_dir
from recursive_generate_page import generate_pages_recursive

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_complete_dir("static", "docs")
    generate_pages_recursive("content", "template.html", "docs",basepath)

if __name__ == "__main__":
    main()