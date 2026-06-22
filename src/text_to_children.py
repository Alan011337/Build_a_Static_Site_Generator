from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node


def text_to_children(text):
    html_nodes = []
    textnodes = text_to_textnodes(text)
    for textnode in textnodes:
        html_node = text_node_to_html_node(textnode)
        html_nodes.append(html_node)
    return html_nodes