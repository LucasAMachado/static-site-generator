import re

def extract__markdown_images(text: str) -> list:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> list:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
