from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self, 
        tag: str, 
        value: str, 
        props: dict[str, str] = None,
    ):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Value is required for leaf node.")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __eq__(self, other: "HTMLNode"):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self):
        return (
            f"LeafNode({self.tag}, {self.value}, {self.props})"
        )