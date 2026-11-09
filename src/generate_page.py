import os

from src.markdown_to_html_node import *


def extract_title(markdown) -> str:
    first_line = markdown.strip().split("\n", maxsplit=1)[0]
    if first_line[:2] == "# ":
        return first_line[2:].strip()
            
def generate_page(from_path, template_path, dest_path):

    for path in [from_path, template_path]:
        if not os.path.exists(path):
            raise Exception(f"{path} does not exist.")

    print(
        f"Generating page from {from_path} to {dest_path}"
        f" using {template_path}."
    )

    with open(from_path) as file:
        markdown = file.read()

    with open(template_path) as file:
        template = file.read()    

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as file:
        file.write(template)

def generate_pages(from_path, template_path, dest_path):

    for item in os.listdir(from_path):
        item_path = os.path.join(from_path, item)
        if os.path.isdir(item_path):
            generate_pages(
                item_path, 
                template_path, 
                os.path.join(dest_path, item)
            )
        else:
            generate_page(
                item_path, 
                template_path, 
                os.path.join(
                    dest_path, 
                    os.path.splitext(item)[0] + ".html"
                )
            )