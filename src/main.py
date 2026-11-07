from src.textnode import *


def main():
    sample = TextNode(
        "This is some anchor text", 
        TextType.LINK, 
        "https://www.boot.dev",
    )
    print(sample)

if __name__ == "__main__":
    main()