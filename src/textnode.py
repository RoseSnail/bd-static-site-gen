from enum import Enum
from leafnode import LeafNode


#example enum
class Bender(Enum):
  AIR_BENDER = "air"
  WATER_BENDER = "water"
  EARTH_BENDER = "earth"
  FIRE_BENDER = "fire"


class TextTypeMarkdown(Enum):
  PLAIN = ""        # text (plain)
  BOLD = "**"       # **Bold text**
  ITALIC = "_"      # _Italic text_
  CODE = "`"        # `Code text`
  LINK = "[]()"     # [anchor text](url)
  IMAGE = "![]()"   # ![alt text](url)

class TextType(Enum):
  TEXT = "text"     # text (plain)
  BOLD = "bold"    # **Bold text**
  ITALIC = "italic" # _Italic text_
  CODE = "code"     # `Code text`
  LINK = "link"     # [anchor text](url)
  IMAGE = "image"   # ![alt text](url)


class TextNode():

  def __init__(self, text:str, text_type:TextType, url:str | None = None) -> None:
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other: 'TextNode') -> bool:
    return (self.text == other.text
      and self.text_type == other.text_type
      and self.url == other.url
    )
  
  def __repr__(self) -> str:
    url = f', "{self.url}"' if self.url else ''
    return f'TextNode("{self.text}", {self.text_type}{url})'
  
  def to_html_node(self) -> LeafNode:
    match self.text_type:
      case TextType.TEXT:
        return LeafNode(None, self.text)
      case TextType.BOLD:
        return LeafNode("b", self.text)
      case TextType.ITALIC:
        return LeafNode("i", self.text)
      case TextType.CODE:
        return LeafNode("code", self.text)
      case TextType.LINK:
        if self.url is None:
          raise ValueError("invalid URL")
        return LeafNode("a", self.text, {"href": self.url})
      case TextType.IMAGE:
        if self.url is None:
          raise ValueError("invalid URL")
        return LeafNode("img", "", {"src": self.url, "alt":self.text})
    raise Exception("TextType not found")  
      
  def text_node_to_html_node(text_node: 'TextNode') -> LeafNode:
    match text_node.text_type:
      case TextType.TEXT:
        return LeafNode(None, text_node.text)
      case TextType.BOLD:
        return LeafNode("b", text_node.text)
      case TextType.ITALIC:
        return LeafNode("i", text_node.text)
      case TextType.CODE:
        return LeafNode("code", text_node.text)
      case TextType.LINK:
        if text_node.url is None:
          raise ValueError("invalid URL")
        return LeafNode("a", text_node.text, {"href": text_node.url})
      case TextType.IMAGE:
        if text_node.url is None:
          raise ValueError("invalid URL")
        return LeafNode("img", "", {"src": text_node.url, "alt":text_node.text})
    raise Exception("TextType not found")  