from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    items_in_content_file = os.listdir(dir_path_content)
    for item in items_in_content_file:
        item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(item_path):
            from_path = item_path
            html_filename = item.replace(".md", ".html")
            dest_path = os.path.join(dest_dir_path, html_filename)
            print(f"Generating page from {from_path} to {dest_path} using {template_path}")
            with open(from_path) as file:
                markdown_content = file.read()
            with open(template_path) as file:
                template_content = file.read()
            html_content = markdown_to_html_node(markdown_content).to_html()
            title = extract_title(markdown_content)
            final_html = template_content.replace("{{ Title }}", title)
            final_html = final_html.replace("{{ Content }}", html_content)
            final_html = final_html.replace('href="/', f'href="{basepath}')
            final_html = final_html.replace('src="/', f'src="{basepath}')
            
            dir_path = os.path.dirname(dest_path)
            os.makedirs(dir_path, exist_ok=True)
            
            with open(dest_path, "w") as file:
                file.write(final_html)
        else:
            sub_dir_path = os.path.join(dir_path_content, item)
            sub_dest_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(sub_dir_path, template_path, sub_dest_path, basepath)