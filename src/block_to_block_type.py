from block_type import BlockType


def block_to_block_type(block) -> BlockType:
    if block.startswith("# ") or block.startswith("## ") or block.startswith("### ") or block.startswith("#### ") or block.startswith("##### ") or block.startswith("###### "):
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in block.split("\n")):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST
    elif all(line.startswith(f"{i+1}. ") for i, line in enumerate(block.split("\n"))):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH