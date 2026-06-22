from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_splits = node.text.split(delimiter)
            if len(node_splits) % 2 == 0:
                raise Exception("Invalid markdown syntax")
            for i in range(len(node_splits)):
                if node_splits[i] == "":
                    continue
                if i % 2 == 0:
                    new_node = TextNode(node_splits[i], TextType.TEXT)
                    new_nodes.append(new_node)
                else:
                    new_node = TextNode(node_splits[i], text_type)
                    new_nodes.append(new_node)
    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            if len(images) == 0:
                new_nodes.append(node)
                continue
            original_text = node.text
            for image in images:
                split_word = f"![{image[0]}]({image[1]})"
                sections = original_text.split(split_word, 1)
                if sections[0] != "":
                    text_node = TextNode(sections[0], TextType.TEXT)
                    new_nodes.append(text_node)
                image_node = TextNode(image[0], TextType.IMAGE, image[1])
                new_nodes.append(image_node)
                original_text = sections[1]
            if original_text != "":
                text_node = TextNode(original_text, TextType.TEXT)
                new_nodes.append(text_node)
                
    return new_nodes
            
            


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            if len(links) == 0:
                new_nodes.append(node)
                continue
            original_text = node.text
            for link in links:
                split_word = f"[{link[0]}]({link[1]})"
                sections = original_text.split(split_word, 1)
                if len(sections) != 2:
                    raise Exception("Invalid markdown, link not found")
                if sections[0] != "":
                    text_node = TextNode(sections[0], TextType.TEXT)
                    new_nodes.append(text_node)
                link_node = TextNode(link[0], TextType.LINK, link[1])
                new_nodes.append(link_node)
                original_text = sections[1]
            if original_text != "":
                text_node = TextNode(original_text, TextType.TEXT)
                new_nodes.append(text_node)
                
    return new_nodes