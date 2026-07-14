import enum
from parentnode import ParentNode
from leafnode import LeafNode
from block_helper import *
from inline_helper import *
from textnode import TextNode


class BlockTag(Enum):
  PARAGRAPH = "p"       # <p>
  HEADING = "h"         # <h1>../..<h6>
  CODE = "pre><code"    # <pre><code> ... </code></pre>
  CODE_INNER = "code"   # <code>
  CODE_OUTER = "pre"    # <pre>
  QUOTE = "blockquote"  # <blockquote>
  UNORDERED_LIST = "ul" # <ul>
  UNORDERED_ITEM = "li" # <li>
  ORDERED_LIST = "ol"   # <ol>
  ORDERED_ITEM = "li"   # <li>


def markdown_to_html_node(doc: str) -> ParentNode:
  #print("markdown_to_html_node")
  #print(doc)
  if doc[0] == "\n" and doc[1] != "\n":
    doc = doc[1:]
  #blocks = doc.split("\n\n")
  #print(blocks)
  block_and_type = []
  for block in doc.split("\n\n"):
    if len(block) > 0 and (len(block) > 1 or block[0] != '\n'):
      block_and_type.append((block, block_to_block_type(block)))
  #print(block_and_type)
  children = []
  for block_tuple in block_and_type:
    children.append(block_to_html_node(block_tuple[0], block_tuple[1]))
  #print("children")
  #print(children)
  #rint("PARENT TO HTML!")
  parent = ParentNode("div", children)
  #print(parent.to_html())
  return parent


def block_to_html_node(block:str, block_type: BlockType) -> ParentNode:
  match block_type:
    case BlockType.PARAGRAPH:
      #text_nodes = text_to_textnodes(block.replace("\n", " "))
      #print("Paragraph's text_nodes")
      #print(f"\nBlock in:\n{block}\n\nNodes Out:")
      #for node in text_nodes:
      #  print(node)
      #html_nodes = TextNode.text_nodes_to_html_nodes(text_to_textnodes(block))
      #print("HTMLNodes:")
      #for node in html_nodes:
      #  print(node)
      return ParentNode(BlockTag.PARAGRAPH.value, text_to_leaf_nodes(block.replace("\n", " ")))
    
    case BlockType.HEADING:
      count = 1
      counting = True
      while counting:
        if block[count] == BlockTypeMarkdown.HEADING:
          count += 1
        else:
          counting = False
      return ParentNode(f"{BlockTag.HEADING.value}{count}", text_to_leaf_nodes(block[count:].replace("\n", " ")))
    
    case BlockType.CODE:
      #print("COOOOOOODE")
      #print(block[4:-4])
      #for node in [LeafNode(None, block[4:-4])]:
      #  print(node.to_html())
      inner = ParentNode(BlockTag.CODE_INNER.value, [LeafNode(None, block[4:-4])])
      return ParentNode(BlockTag.CODE_OUTER.value, inner)
    
    case BlockType.QUOTE:
      return ParentNode(BlockTag.QUOTE.value, text_to_leaf_nodes(block.replace("\n>", "\n")))

    case BlockType.UNORDERED_LIST:
      items = []
      for list_item in block[2:].split(f"\n{BlockTypeMarkdown.UNORDERED_LIST.value} "):
        items.append(ParentNode(BlockTag.UNORDERED_ITEM.value, text_to_leaf_nodes(list_item)))
      return ParentNode(BlockTag.UNORDERED_LIST.value, items)

    case BlockType.ORDERED_LIST:
      items = []
      i = 1
      for list_item in block.split("\n"):
        count = 2 + len(str(i))
        i += 1
        items.append(ParentNode(BlockTag.ORDERED_ITEM.value, text_to_leaf_nodes(list_item[count:])))
      return ParentNode(BlockTag.ORDERED_LIST.value, items)
  raise ValueError("BlockType not valid")

def text_to_leaf_nodes(text: str) -> list[LeafNode]:
  return TextNode.text_nodes_to_html_nodes(text_to_textnodes(text))

#.replace("\n", " ")
### PARAGRAPH = "paragraph"   # paragraph (plain)
### HEADING = "heading"       # #:h1, ##:h2, ###:h3 ... h6
# CODE = "code"             # ```\n Code block ```
# QUOTE = "quote"           # > Quote block
# UNORDERED_LIST = "unordered_list" # - for each \n
# ORDERED_LIST = "ordered_list"     # 1234. for each \n

#text_to_textnodes(text: str) -> list[TextNode]:
#text_node_to_html_node(text_node: 'TextNode')

#text.replace("\n", "")  # Result: "HelloWorld"