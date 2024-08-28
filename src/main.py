from generate_page import  generate_pages_recursive, source_to_destination


def main() -> None:
    from_path: str = "./content"
    template_path: str = "./template.html"
    dest_path: str = "./public"
    source_to_destination()
    generate_pages_recursive(from_path, template_path, dest_path)


if __name__ == "__main__":
    main()
