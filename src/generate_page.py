from blocks import markdown_to_blocks

def extract_title(markdown) -> str:
    markdown_blocks = markdown_to_blocks(markdown)

    if "#" in markdown_blocks[0] and markdown_blocks[0].count("#") == 1:
        return markdown_blocks[0].replace("#", "").strip()
    else:
        raise Exception("Must have an h1 title")
