from textnode import *


def split_nodes_delimiter(
        old_nodes: list[TextNode], 
        delimiter: str, 
        text_type: TextType,
) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise Exception(
                f"Invalid markdown syntax: {delimiter} not closed."
            )
        new_nodes.extend(
            [
                TextNode(text, text_type) if i % 2 == 1
                else TextNode(text, TextType.TEXT) 
                for i, text in enumerate(split_text)
                if text != ""
            ]
        )
    return new_nodes