import os
import shutil

from src.generate_page import *


def main():
    static = os.path.abspath("static")
    public = os.path.abspath("public")
    shutil.rmtree(public)
    print(f"cleared old {public}")
    os.mkdir(public)
    print(f"created new {public}")
    populate(source=static, destination=public)
    generate_page(
        from_path="content/index.md", 
        template_path="template.html", 
        dest_path="public/index.html",
    )

def populate(source: str, destination: str) -> None:
    if not os.path.exists(destination):
        raise Exception(f"{destination} is not a valid path")
    if not os.path.exists(source):
        raise Exception(f"{source} is not a valid path")
    for content in os.listdir(source):
        content_path=os.path.join(source, content)
        if os.path.isdir(content_path):
            destination = os.path.join(destination, content)
            os.mkdir(destination)
            populate(source=content_path, destination=destination)
        else:
            shutil.copy(src=content_path, dst=destination)
            print(f"copied {os.path.join(destination, content_path)}")


if __name__ == "__main__":
    main()