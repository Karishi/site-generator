from textnode import TextNode, TextType

def main():
    dummy = TextNode("This is some anchor text", TextType.image.value, "https://www.boot.dev")

    print(dummy)

main()