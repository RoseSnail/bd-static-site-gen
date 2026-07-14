
from enum import Enum
from textnode import TextNode, TextType, TextTypeMarkdown


class BlockTypeMarkdown(Enum):
  PARAGRAPH = ""  # paragraph (plain)
  HEADING = "#"   # #:h1, ##:h2, ###:h3 ... h6
  CODE = "`"      # ```\n Code block ````
  QUOTE = ">"     # > Quote block
  UNORDERED_LIST = "-"  # [anchor text](url)
  ORDERED_LIST = "*."   # ![alt text](url)

class BlockType(Enum):
  PARAGRAPH = "paragraph"   # paragraph (plain)
  HEADING = "heading"       # #:h1, ##:h2, ###:h3 ... h6
  CODE = "code"             # ```\n Code block ````
  QUOTE = "quote"           # > Quote block
  UNORDERED_LIST = "unordered_list" # - for each \n
  ORDERED_LIST = "ordered_list"     # 1234. for each \n


def markdown_to_blocks(document: str) -> list[str]:
  if document[0] == "\n" and document[1] != "\n":
    document = document[1:]
  blocks = []
  split_doc = document.split("\n\n")
  for i in range(len(split_doc)):
    block = split_doc[i].strip()
    if len(block) > 0:
      blocks.append(block)
  return blocks

def block_to_block_type(markdown:str) -> BlockType:
  if markdown[0] == "\n":
    markdown = markdown[1:]
  match markdown[0]:
    case BlockTypeMarkdown.HEADING.value:
      length = min(7, len(markdown))
      for i in range(1, length):
        char = markdown[i]
        if char == BlockTypeMarkdown.HEADING.value:
          continue
        elif char == ' ':
          return BlockType.HEADING
        else:
          break
  
    case BlockTypeMarkdown.CODE.value:
      if markdown[:4] == "```\n" and (markdown[-3:] == "```" or markdown[-4:] == "```\n"):
        return BlockType.CODE
      
    case BlockTypeMarkdown.QUOTE.value:
      split_test = markdown.split('\n')
      if len(split_test[-1]) == 0 or split_test[-1] == '\n':
        split_test.pop(-1)
      for test in split_test:
        if len(test) < 1 or test[0] != BlockTypeMarkdown.QUOTE.value:
          return BlockType.PARAGRAPH
      return BlockType.QUOTE

    case BlockTypeMarkdown.UNORDERED_LIST.value:
      split_test = markdown.split('\n')
      if len(split_test[-1]) == 0 or split_test[-1] == '\n':
        split_test.pop(-1)
      for test in split_test:
        if len(test) < 2 or test[:2] != f"{BlockTypeMarkdown.UNORDERED_LIST.value} ":
          return BlockType.PARAGRAPH
      return BlockType.UNORDERED_LIST

    #case BlockTypeMarkdown.ORDERED_LIST.value
    case str(text) if text.isdigit(): # Catches ordered lists
      for i in range(len(markdown)):
        if markdown[i].isdigit():
          continue
        elif markdown[i] == '.':
          return BlockType.ORDERED_LIST
        break
  return BlockType.PARAGRAPH