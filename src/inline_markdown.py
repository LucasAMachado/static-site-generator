from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: str) -> list[TextNode]:
    list_of_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            list_of_nodes.append(node)
            continue

        split_text: list[str] = node.text.split(delimiter)

        if len(split_text) % 2 == 0:
            raise Exception(
                "Invalid Markdown: The formatted sections have to be closed")

        split_nodes: list[TextNode] = []

        for index, text in enumerate(split_text):
            if text == "":
                continue
            if index % 2 == 0:
                split_nodes.append(TextNode(text, text_type_text))
            else:
                split_nodes.append(TextNode(text, text_type))

        list_of_nodes.extend(split_nodes)

    return list_of_nodes
