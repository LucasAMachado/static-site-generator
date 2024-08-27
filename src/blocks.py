# block-types
paragraph = "paragraph"
heading = "heading"
code = "code"
quote = "quote"
unorderd_list = "unordered_list"
ordered_list = "ordered_list"


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

def block_to_block_type(markdown_block) -> str:

    lines = markdown_block.split("\n")

    if lines[0].startswith('```') and lines[-1].startswith('```'):
        return code
    
    if lines[0].startswith("#") and lines[0].count("#") <= 6:
        return heading
    
    if all(line.startswith("> ") for line in lines):
        return quote 
    
    if all(line.startswith("* ") for line in lines):
        return unorderd_list   

    if all(line.startswith("- ") for line in lines):
        return unorderd_list    

    if all(line.startswith(f"{i+1}. ") for i, line in enumerate(lines)):
        return ordered_list
    
    return paragraph




