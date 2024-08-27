from split_links_and_images import split_nodes_image, split_nodes_link

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

from inline_markdown import split_nodes_delimiter


def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    print("After bold split:", nodes)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic) 
    print("After italic split:", nodes)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    print("After code split:", nodes)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes