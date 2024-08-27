def markdown_to_blocks(markdown: str) -> list:
    split_blocks = markdown.split("\n")
    result_blocks = []

    for line in split_blocks:
        if line.strip() != "":
            result_blocks.append(line.strip())

    new_blocks = []
    temp_block = []  

    for line in result_blocks:
        if line.startswith("*"):
            temp_block.append(line)  
        else:
            if temp_block:  
                new_blocks.append("\n".join(temp_block))
                temp_block = []  
            new_blocks.append(line)  


    if temp_block:
        new_blocks.append("\n".join(temp_block))

    return new_blocks  
