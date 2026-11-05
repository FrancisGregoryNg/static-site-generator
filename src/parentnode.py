from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self, 
        tag: str, 
        children: list["HTMLNode"], 
        props: dict[str, str] = None,
    ):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Tag is required for parent node.")
        if self.children is None:
            raise ValueError("Children are required for parent node.")
        return (
            f"<{self.tag}{self.props_to_html()}>"
            f"{''.join(child.to_html() for child in self.children)}"
            f"</{self.tag}>"
        )

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