from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        markdown_content = file.read()
    with open(template_path) as file:
        template_content = file.read()
    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
    final_html.replace('href="/','href=f"{basepath}')
    final_html.replace('src="/', 'src=f"{basepath}')
    
    dir_path = os.path.dirname(dest_path)
    os.makedirs(dir_path, exist_ok=True)
    
    with open(dest_path, "w") as file:
        file.write(final_html)
    