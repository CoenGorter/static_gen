import sys

from copy_content import (
    copy_contents,
    generate_pages_recursive,
)


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    print(basepath)

    copy_contents("./docs/", "./static/")
    generate_pages_recursive("./content/", "template.html", "./docs/", basepath)


if __name__ == "__main__":  # True when run as script, False when imported
    # execute only if run as a script
    main()
