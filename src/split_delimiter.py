from textnode import *


def split_nodes_delimiter(
        old_nodes: list[TextNode], 
        delimiter: str, 
        text_type: TextType,
) -> list[TextNode]:
    pass
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        match text_type:
            case TextType.BOLD:
                if delimiter != "**": 
                    raise Exception(
                        "Invalid delimiter: need ** for bold text type."
                    )
            case TextType.ITALIC:
                if delimiter != "_": 
                    raise Exception(
                        "Invalid delimiter: need _ for italic text type."
                    )
            case TextType.CODE:
                if delimiter != "`": 
                    raise Exception(
                        "Invalid delimiter: need ` for code text type."
                    )
            case _:
                raise Exception("Not a valid text type.")
        if node.text.count(delimiter) % 2 == 1:
            raise Exception(
                f"Invalid markdown syntax: {delimiter} not closed."
            )
        new_nodes.extend(
            [
                TextNode(text, text_type) if i % 2 == 1
                else TextNode(text, TextType.TEXT) 
                for i, text in enumerate(node.text.split(delimiter))
                if text != ""
            ]
        )
    return new_nodes