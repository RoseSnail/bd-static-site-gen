import re
from textnode import TextNode, TextType, TextTypeMarkdown


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
  split_nodes = []
  for node in old_nodes:
    split_text = node.text.split(delimiter)
    if len(split_text) % 2 == 0:
      raise Exception(f"Split Nodes Delimiter: invalid Markdown syntax encountered with {delimiter}")
    for i in range(len(split_text)):
      if i % 2 == 0:
        if len(split_text[i]) > 0:
          split_nodes.append(TextNode(split_text[i], node.text_type))
      else:
        split_nodes.append(TextNode(split_text[i], text_type))
  return split_nodes

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
  regex_images = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
  matches = re.findall(regex_images, text)
  #print(matches)
  return matches

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
  regex_links = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
  matches = re.findall(regex_links, text)
  #print(matches)
  return matches

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
  split_nodes = []
  for node in old_nodes:
    delimiters = extract_markdown_images(node.text)
    if delimiters is None or len(delimiters) < 1:
      split_nodes.append(node)
      continue
    to_split = node.text
    #print(f"NodeText: {node.text}")
    for delimiter in delimiters:
      #print(f"Delimiter: {delimiter}")
      #print(f"ToSplit: {to_split}")
      split_text = to_split.split(f"![{delimiter[0]}]({delimiter[1]})")
      #print(f"SplitText: {split_text}")
      if len(split_text[0]) > 0:
        split_nodes.append(TextNode(split_text[0], node.text_type))
      split_nodes.append(TextNode(delimiter[0], TextType.IMAGE, delimiter[1]))
      to_split = split_text[1] if len(split_text) > 1 else ""
    if len(to_split) > 0:
      split_nodes.append(TextNode(to_split, node.text_type))
  #print(split_nodes)
  return split_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
  split_nodes = []
  for node in old_nodes:
    delimiters = extract_markdown_links(node.text)
    if delimiters is None or len(delimiters) < 1:
      split_nodes.append(node)
      continue
    to_split = node.text
    #print(f"NodeText: {node.text}")
    for delimiter in delimiters:
      #print(f"Delimiter: {delimiter}")
      #print(f"ToSplit: {to_split}")
      split_text = to_split.split(f"[{delimiter[0]}]({delimiter[1]})")
      #print(f"SplitText: {split_text}")
      if len(split_text[0]) > 0:
        split_nodes.append(TextNode(split_text[0], node.text_type))
      split_nodes.append(TextNode(delimiter[0], TextType.LINK, delimiter[1]))
      to_split = split_text[1] if len(split_text) > 1 else ""
    if len(to_split) > 0:
      split_nodes.append(TextNode(to_split, node.text_type))
  #print(split_nodes)
  return split_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
  #print(text)
  nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], TextTypeMarkdown.BOLD.value, TextType.BOLD)
  nodes = split_nodes_delimiter(nodes, TextTypeMarkdown.ITALIC.value, TextType.ITALIC)
  nodes = split_nodes_delimiter(nodes, TextTypeMarkdown.CODE.value, TextType.CODE)
  nodes = split_nodes_image(nodes)
  nodes = split_nodes_link(nodes)
  #print(nodes)
  return nodes
