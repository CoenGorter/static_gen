from copy_content import (
    copy_contents,
    generate_pages_recursive,
)


def main():
    copy_contents()
    generate_pages_recursive("./content/", "template.html", "./public/")


if __name__ == "__main__":  # True when run as script, False when imported
    # execute only if run as a script
    main()
