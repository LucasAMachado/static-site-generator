from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode


paragraph = "paragraph"
heading = "heading"
code = "code"
quote = "quote"
unordered_list = "unordered_list"
ordered_list = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip()]


def block_to_block_type(markdown_block: str) -> str:
    lines = markdown_block.split("\n")

    if markdown_block.startswith(("#", "##", "###", "####", "#####", "######")):
        return heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return code
    if all(line.startswith("> ") for line in lines):
        return quote
    if all(line.startswith("* ") or line.startswith("- ") for line in lines):
        return unordered_list
    if all(line.startswith(f"{i+1}. ") for i, line in enumerate(lines)):
        return ordered_list
    return paragraph


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks: list[str] = markdown_to_blocks(markdown)
    children: list[HTMLNode] = [block_to_html_node(block) for block in blocks]
    return ParentNode("div", children, None)


def block_to_html_node(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)
    if block_type == paragraph:
        return paragraph_to_html_node(block)
    elif block_type == heading:
        return heading_to_html_node(block)
    elif block_type == code:
        return code_to_html_node(block)
    elif block_type == unordered_list:
        return unordered_list_to_html_node(block)
    elif block_type == ordered_list:
        return ordered_list_to_html_node(block)
    elif block_type == quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")


def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes: list[TextNode] = text_to_textnodes(text)
    return [text_node_to_html_node(text_node) for text_node in text_nodes]


def paragraph_to_html_node(block: str) -> HTMLNode:
    children = text_to_children(block.replace("\n", " "))
    return ParentNode("p", children)


def heading_to_html_node(block: str) -> HTMLNode:
    level = block.count("#")
    text = block[level:].strip()
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block: str) -> HTMLNode:
    text = block.strip("```").strip()
    children = text_to_children(text)
    code_node = ParentNode("code", children)
    return ParentNode("pre", [code_node])


def ordered_list_to_html_node(block: str) -> HTMLNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:].strip()
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def unordered_list_to_html_node(block: str) -> HTMLNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:].strip()
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block: str) -> HTMLNode:
    lines = [line.lstrip("> ").strip() for line in block.split("\n")]
    content = " ".join(lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
