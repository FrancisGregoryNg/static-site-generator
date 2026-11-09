import os
import shutil
import sys

from src.generate_page import *


def main():
    if sys.argv[0] == "":
        basepath = "/"
    else: 
        basepath = sys.argv[0]
    static = os.path.abspath("static")
    docs = os.path.abspath("docs")
    if not os.path.isdir(docs):
        os.mkdir(docs)
    shutil.rmtree(docs)
    print(f"cleared old {docs}")
    os.mkdir(docs)
    print(f"created new {docs}")
    populate(source=static, destination=docs)
    generate_pages(
        base_path = basepath,
        from_path="content", 
        template_path="template.html", 
        dest_path="docs",
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