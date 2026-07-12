import unittest
from htmlnode import HTMLNode, HTMLType

class TestHTMLNode(unittest.TestCase):
  def test_eq(self):
    node = HTMLNode()
    node2 = HTMLNode()
    self.assertEqual(node, node2)

  def test_eq1(self):
    props = {
      "href": "https://www.google.com",
      "target": "_blank",
    }
    prop_str = f' href="{props["href"]}" target="{props["target"]}"'
    node = HTMLNode("p", "This is plain text", None, props)
    self.assertEqual(node.props_to_html(), prop_str)

  def test_not_eq(self):
    node = HTMLNode("p")
    node2 = HTMLNode()
    self.assertNotEqual(node, node2)

  def test_not_eq1(self):
    props = {
      "href": "https://www.google.com",
      "target": "_blank",
    }
    prop_str = f'href="{props["href"]}" target="{props["target"]}"'
    node = HTMLNode("p", "This is plain text", None, props)
    self.assertNotEqual(node.props_to_html(), prop_str)

if __name__ == "__main__":
  unittest.main()