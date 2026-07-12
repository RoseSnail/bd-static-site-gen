from operator import index

from htmlnode import HTMLNode


class ParentNode(HTMLNode):

  def __init__(self, tag: str, children: list['HTMLNode'], props: dict[str,str] | None = None) -> None:
    super().__init__(tag, None, children, props)

  def __repr__(self) -> str:
    return f"ParentNode({self.tag}, {self.children}, {self.props})"
  
  def to_html(self, index = -1) -> str:
    if self.tag is None:
      raise ValueError("ParentNode: tag is missing")
    if self.children is None or len(self.children) == 0:
      raise ValueError("ParentNode: children are missing")
    if index >= len(self.children):
      return ""
    if index < 0:
      return f"<{self.tag}{self.props_to_html()}>{self.to_html(0)}</{self.tag}>"
    return f"{self.children[index].to_html()}{self.to_html(index + 1)}"
    #html = f"<{self.tag}{self.props_to_html()}>"
    #for child in self.children:
    #  html += child.to_html()
    #return html + f"<{self.tag}>"
