
from textnode import TextNode

from text_extraction import extract__markdown_images, extract_markdown_links

from textnode import (
    text_type_text,
    text_type_bold,
    text_type_image,
    text_type_link,
)


def split_nodes_image(old_nodes: TextNode) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for old_node in old_nodes:
        original_text: str = old_node.text
        markdown_images : tuple = extract__markdown_images(original_text)

        for image in markdown_images:
            image_alt, image_link = image

            parts: list = original_text.split(
                f"![{image_alt}]({image_link})", 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], text_type_text))

            if len(parts) > 1:
                new_nodes.append(
                    TextNode(image_alt, text_type_image, image_link))

            original_text : str = parts[1] if len(parts) > 1 else ""

        if original_text:
            new_nodes.appenad(TextNode(original_text, text_type_text))

    return new_nodes


def split_nodes_link(old_nodes: TextNode) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for old_node in old_nodes:
        original_text: str = old_node.text
        markdown_text: tuple = extract_markdown_links(original_text)

        for current_link in markdown_text:
            link_alt, link = current_link

            parts: list = original_text.split(
                f"[{link_alt}]({link})", 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], text_type_text))

            if len(parts) > 1:
                new_nodes.append(
                    TextNode(link_alt, text_type_link, link))

            original_text: str = parts[1] if len(parts) > 1 else ""

        if original_text:
            new_nodes.appenad(TextNode(original_text, text_type_text))

    return new_nodes



