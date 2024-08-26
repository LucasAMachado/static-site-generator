from textnode import TextNode


def main():
    text_node: TextNode = TextNode(
        'This is a text node', 'bold', 'https://www.boot.dev')
    print(text_node)


if __name__ == "__main__":
    main()
