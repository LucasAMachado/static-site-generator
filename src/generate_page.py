from typing import List
from blocks import markdown_to_blocks, markdown_to_html_node
import os
import shutil


def source_to_destination() -> None:
    directory_file_path: str = "./public"
    source_file: str = "./static"
    delete_files_in_directory(directory_file_path)
    copy_files_from_one_directory_to_another(source_file, directory_file_path)


def delete_files_in_directory(directory_file_path: str) -> None:
    try:
        files: List[str] = os.listdir(directory_file_path)
        for file in files:
            file_path: str = os.path.join(directory_file_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("All of the files have been deleted")
    except OSError:
        print("Error occurred while deleting the files in,", directory_file_path)


def copy_files_from_one_directory_to_another(source_file: str, destination_file: str) -> None:
    image_dir: str = os.path.join(destination_file, "images")
    os.makedirs(image_dir, exist_ok=True)
   
    for item in os.listdir(source_file):
        source_item: str = os.path.join(source_file, item)
        destination_item: str = os.path.join(destination_file, item)
        if os.path.isdir(source_item):
            shutil.copytree(source_item, destination_item, dirs_exist_ok=True)
        else:
            shutil.copy2(source_item, destination_item)
    print(
        f"The files have been copied over from {source_file} to {destination_file}")


def extract_title(markdown: str) -> str:
    markdown_blocks: List[str] = markdown_to_blocks(markdown)
    if "#" in markdown_blocks[0] and markdown_blocks[0].count("#") == 1:
        return markdown_blocks[0].replace("#", "").strip()
    else:
        raise Exception("Must have an h1 title")


def create_file_with_content(file_path: str, content: str) -> None:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File has been created in {file_path}")


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path} for the template")
    with open(os.path.join(from_path, 'index.md'), 'r') as file:
        markdown: str = file.read()
    with open(os.path.join(template_path), 'r') as file:
        template: str = file.read()
    html: str = markdown_to_html_node(markdown).to_html()
    title: str = extract_title(markdown)
    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', html)
    create_file_with_content(dest_path, template)


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):
                md_file_path: str = os.path.join(root, file)

                rel_path: str = os.path.relpath(md_file_path, dir_path_content)

                dest_path: str = os.path.join(
                    dest_dir_path, os.path.splitext(rel_path)[0] + '.html')
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                generate_page(os.path.dirname(md_file_path),
                              template_path, dest_path)
