from typing import Optional, List, Dict


class HTMLNode:
    def __init__(self, tag: Optional[str] = None, value: Optional[str] = None, children: Optional[List['HTMLNode']] = None, props: Optional[Dict[str, str]] = None):
        self.tag: Optional[str] = tag
        self.value: Optional[str] = value
        self.children: Optional[List['HTMLNode']] = children
        self.props: Optional[Dict[str, str]] = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None:
            return ""

        converted_string: str = ""
        for key, value in self.props.items():
            converted_string += f' {key}="{value}"'
        return converted_string

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag: Optional[str] = None, value: Optional[str] = None, props: Optional[Dict[str, str]] = None):
        super().__init__(tag, value, None, props)
        self.tag: Optional[str] = tag
        self.value: Optional[str] = value
        self.props: Optional[Dict[str, str]] = props

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: List[HTMLNode], props: Optional[Dict[str, str]] = None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html: str = ""

        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
