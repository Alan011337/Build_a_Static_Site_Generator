from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from htmlnode import HTMLNode, ParentNode
from block_type import BlockType
from textnode import TextNode, TextType, text_node_to_html_node
from text_to_children import text_to_children


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            if block.startswith("# "):
                children = text_to_children(block[2:])
                node = ParentNode("h1", children, None)
            elif block.startswith("## "):
                children = text_to_children(block[3:])
                node = ParentNode("h2", children, None)
            elif block.startswith("### "):
                children = text_to_children(block[4:])
                node = ParentNode("h3", children, None)
            elif block.startswith("#### "):
                children = text_to_children(block[5:])
                node = ParentNode("h4", children, None)
            elif block.startswith("##### "):
                children = text_to_children(block[6:])
                node = ParentNode("h5", children, None)
            elif block.startswith("###### "):
                children = text_to_children(block[7:])
                node = ParentNode("h6", children, None)
        elif block_type == BlockType.CODE:
            new_block = block.strip(" \n")
            new_block = new_block.strip("```")
            text_node = TextNode(new_block, TextType.TEXT, None)
            html_node = text_node_to_html_node(text_node)
            code_node = ParentNode("code", [html_node], None)
            node = ParentNode("pre", [code_node], None)
        elif block_type == BlockType.QUOTE:
            new_lines = []
            lines = block.split("\n")
            for line in lines:
                new_line = line.strip("> ")
                new_lines.append(new_line)
            text = "\n".join(new_lines)
            children = text_to_children(text)
            node = ParentNode("blockquote", children, None)
        elif block_type == BlockType.UNORDERED_LIST:
            li_nodes = []
            lines = block.split("\n")
            for line in lines:
                text = line[2:]
                children = text_to_children(text)
                li_node = ParentNode("li", children, None)
                li_nodes.append(li_node)
            node = ParentNode("ul", li_nodes, None)
        elif block_type == BlockType.ORDERED_LIST:
            li_nodes = []
            lines = block.split("\n")
            for line in lines:
                line_splits = line.split(" ", 1)
                text = line_splits[1]
                children = text_to_children(text)
                li_node = ParentNode("li", children, None)
                li_nodes.append(li_node)
            node = ParentNode("ol", li_nodes, None)
        elif block_type == BlockType.PARAGRAPH:
            text = block.replace("\n", " ")
            children = text_to_children(text)
            node = ParentNode("p", children, None)
        nodes.append(node)
    parent_html_node = ParentNode("div", nodes, None)
    return parent_html_node