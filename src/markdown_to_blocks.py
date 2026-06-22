def markdown_to_blocks(markdown):
    blocks = markdown.strip().split("\n\n")
    for block in blocks:
        if not block:
            blocks.pop(block)
    return blocks