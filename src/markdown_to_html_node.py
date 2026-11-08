from src.markdown_to_blocks import *
from src.block_to_block_type import *
from src.text_to_textnodes import *
from src.textnode import *
from src.htmlnode import *
from src.leafnode import *
from src.parentnode import *


def markdown_to_html_node(markdown) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    block_nodes: list[HTMLNode] = []
    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                block_node = ParentNode(
                    tag="p",
                    children=text_to_children(block.replace("\n", " ")),
                )
            case BlockType.HEADING:
                match = re.match(r"^(#{1,6}) (.+)", block)
                hashes = match.group(1)
                text = match.group(2)
                block_node = ParentNode(
                        tag=f"h{len(hashes)}", 
                        children=text_to_children(text),
                )
            case BlockType.CODE:
                block_node = ParentNode(
                        tag="pre", 
                        children=[LeafNode(tag="code", value=block[4:-3])]
                )
            case BlockType.QUOTE:
                text = "\n".join(
                    line[1:].lstrip() 
                    for line in block.split("\n")
                )
                block_node = ParentNode(
                        tag="blockquote", 
                        children=text_to_children(text),
                ) 
            case BlockType.UNORDERED_LIST:
                clean_lines = [line[2:] for line in block.split("\n")]
                line_nodes = [
                    ParentNode(tag="li", children=text_to_children(line))
                    for line in clean_lines
                ]
                block_node = ParentNode(
                        tag="ul", 
                        children=line_nodes,
                )                 
            case BlockType.ORDERED_LIST:
                clean_lines = [
                    line[len(str(i+1))+2:] 
                    for i, line in enumerate(block.split("\n"))
                ]
                line_nodes = [
                    ParentNode(tag="li", children=text_to_children(line))
                    for line in clean_lines
                ]
                block_node = ParentNode(
                        tag="ol", 
                        children=line_nodes,
                )           
        block_nodes.append(block_node)
    node = ParentNode(tag="div", children=block_nodes)
    return node

def text_to_children(text: str) -> list[HTMLNode]:
    children: list[HTMLNode] = [
        text_node_to_html_node(text_node) 
        for text_node in text_to_textnodes(text)
    ]
    return children