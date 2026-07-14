from platform import node
import unittest
from textnode import TextNode, TextType
from text_helper import *


class TestTextHelper(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(new_nodes, [
      TextNode("This is text with a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.TEXT),
    ])
    
  def test_eq1(self):
    node = TextNode("This is text with a _italic block_ word", TextType.BOLD)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    self.assertEqual(new_nodes, [
      TextNode("This is text with a ", TextType.BOLD),
      TextNode("italic block", TextType.ITALIC),
      TextNode(" word", TextType.BOLD),
    ])
    
  def test_eq2(self):
    node = TextNode("This is text with a **bold block** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(new_nodes, [
      TextNode("This is text with a ", TextType.TEXT),
      TextNode("bold block", TextType.BOLD),
      TextNode(" word", TextType.TEXT),
    ])
    
  def test_raise(self):
    node = TextNode("This is text `with a `code block` word", TextType.TEXT)
    with self.assertRaises(Exception):
      split_nodes_delimiter([node], "`", TextType.CODE)


class TestRegExTextHelper(unittest.TestCase):
  def test_eq(self):
    image_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    self.assertEqual(extract_markdown_images(image_text) , [
      ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
      ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
    ])

  def test_eq1(self):
    link_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    self.assertEqual(extract_markdown_links(link_text) , [
      ("to boot dev", "https://www.boot.dev"),
      ("to youtube", "https://www.youtube.com/@bootdotdev")
    ])

  def test_extract_markdown_images(self):
    matches = extract_markdown_images(
      "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


class TestRegExSplitTextHelper(unittest.TestCase):
  def test_split_images(self):
    node = TextNode(
      "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
      TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(new_nodes, [
      TextNode("This is text with an ", TextType.TEXT),
      TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
      TextNode(" and another ", TextType.TEXT),
      TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
    ])

  def test_split_links(self):
    node = TextNode(
      "This is text with an [first link](https://i.imgur.com/zjjcJKZ.png) and another [second linky](https://i.imgur.com/3elNhQu.png)",
      TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(new_nodes, [
      TextNode("This is text with an ", TextType.TEXT),
      TextNode("first link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
      TextNode(" and another ", TextType.TEXT),
      TextNode("second linky", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
    ])

  def test_text_to_textnodes(self):
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    self.assertListEqual(nodes, [
      TextNode("This is ", TextType.TEXT),
      TextNode("text", TextType.BOLD),
      TextNode(" with an ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" word and a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" and an ", TextType.TEXT),
      TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
      TextNode(" and a ", TextType.TEXT),
      TextNode("link", TextType.LINK, "https://boot.dev"),
    ])

if __name__ == "__main__":
  unittest.main()