from enum import Enum

class HTMLTypeMarkdown(Enum):
  PARAGRAPH = "p"     # text (plain)
  ANCHOR = "a"        # **Bold text**
  HEADER_1 = "h1"     # #
  HEADER_2 = "h2"     # ##
  HEADER_3 = "h3"     # ###
  HEADER_4 = "h4"     # ####

class HTMLType(Enum):
  PLAIN = "plain"     # text (plain)
  BOLD = "bold"       # **Bold text**
  ITALIC = "italic"   # _Italic text_
  CODE = "code"       # `Code text`
  LINK = "link"       # [anchor text](url)
  IMAGE = "image"     # ![alt text](url)


class HTMLNode():

  def __init__(self, tag: str | None = None, value: str | None = None, children: list['HTMLNode'] | None = None, props: dict[str,str] | None = None) -> None:
    self.tag = tag
    self.value = value
    # handle if a single child is passed directly instead of a list (wrap it)
    if isinstance(children, HTMLNode):
      self.children = [children]
    else:
      self.children = children
    self.props = props

  def __eq__(self, other: 'HTMLNode') -> bool:
    return (self.tag == other.tag
      and self.value == other.value
      and self.children == other.children
      and self.props == other.props
    )
  
  def __repr__(self) -> str:
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
  
  def to_html(self):
    raise NotImplementedError
  
  def props_to_html(self) -> str:
    html = ""
    if self.props is None:
      return html
    for kvp in self.props:
      #if len(html) > 0:
      #    html += " "
      html += f' {kvp}="{self.props[kvp]}"'
    #print(html)
    return html