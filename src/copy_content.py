import os
import shutil

from markdown_blocks import markdown_to_blocks, markdown_to_html_node


def copy_contents(
    folder_path_public="./docs/", folder_path_static="./static/", level=0
):
    # Remove old content
    if level == 0:
        if not os.path.isdir(folder_path_public):
            raise Exception(
                f"Error: {folder_path_public} is not a valid directory path."
            )
        elif len(os.listdir(folder_path_public)) == 0:
            pass
        else:
            shutil.rmtree(folder_path_public)
            os.mkdir(folder_path_public)

    # Copy Paste to public folder
    if not os.path.isdir(folder_path_static):
        raise Exception(
            f"Error: {folder_path_static} is not there....gimmie some content"
        )
    else:
        static_content = os.listdir(folder_path_static)
        for content in static_content:
            source_path = os.path.join(folder_path_static, content)
            destination_path = os.path.join(folder_path_public, content)
            if os.path.isdir(source_path):
                os.mkdir(destination_path)
                copy_contents(destination_path, source_path, level + 1)
            if os.path.isfile(source_path):
                shutil.copy(source_path, destination_path)
    pass


def extract_title(markdown):
    # blocks = markdown_to_html_node(markdown)
    # print(blocks.to_html())
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return str(block[2:].strip())
    pass


def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        content = file.read()
    md = markdown_to_html_node(content)
    html = md.to_html()
    title = extract_title(content)
    with open(template_path) as file:
        template = file.read()
    template = template.replace("{{ Title }}", title, 1)
    template = template.replace("{{ Content }}", html, 1)
    template = template.replace('href="/', f'href="{base_path}')
    template = template.replace('src="/', f'src="{base_path}')
    with open(dest_path, "w") as html_file:
        html_file.write(template)
    pass


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    # Copy Paste to public folder
    if not os.path.isdir(dir_path_content):
        raise Exception(
            f"Error: {dir_path_content} is not there....gimmie some content"
        )
    else:
        static_content = os.listdir(dir_path_content)
        for content in static_content:
            source_path = os.path.join(dir_path_content, content)
            destination_path = os.path.join(dest_dir_path, content)
            if os.path.isdir(source_path):
                os.mkdir(destination_path)
                generate_pages_recursive(
                    source_path, template_path, destination_path, base_path
                )
            if os.path.isfile(source_path):
                destination_path = destination_path.replace(".md", ".html")
                generate_page(source_path, template_path, destination_path, base_path)
    pass
