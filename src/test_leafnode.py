import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

  def test_eq(self):
    node = LeafNode(None, "")
    node2 = LeafNode(None, "")
    self.assertEqual(node, node2)

  def test_eq1(self):
    props = {
      "href": "https://www.google.com",
      "target": "_blank",
    }
    prop_str = f' href="{props["href"]}" target="{props["target"]}"'
    node = LeafNode("a", "This is plain text", props)
    self.assertEqual(node.props_to_html(), prop_str)

  def test_eq2(self):
    props = {
      "href": "https://www.google.com",
      "target": "_blank",
    }
    leaf_html_str = f'<a href="{props["href"]}" target="{props["target"]}">This is plain text</a>'
    node = LeafNode("a", "This is plain text", props)
    self.assertEqual(node.to_html(), leaf_html_str)

  def test_eq3(self):
    props = {
      "href": "https://www.google.com",
      "target": "_blank",
    }
    leaf_node_str = f"LeafNode(a, This is plain text, {props})"
    node = LeafNode("a", "This is plain text", props)
    self.assertEqual(str(node), leaf_node_str)

  def test_eq4(self):
    props = {
      "href": "https://www.google.com",
      "target": "_blank",
    }
    leaf_node_str = "This is plain text"
    node = LeafNode(None, "This is plain text", props)
    self.assertEqual(node.to_html(), leaf_node_str)

  def test_eq5(self):
    props = {
      "href": "https://www.google.com",
      "target": "_blank",
    }
    node = LeafNode(None, None, props)
    with self.assertRaises(ValueError):
      node.to_html()

  def test_not_eq(self):
    node = LeafNode("p", None)
    node2 = LeafNode(None, None)
    self.assertNotEqual(node, node2)

  def test_not_eq1(self):
    props = {
      "href": "https://www.google.com",
      "target": "_blank",
    }
    prop_str = f'href="{props["href"]}" target="{props["target"]}"'
    node = LeafNode("p", "This is plain text", props)
    self.assertNotEqual(node.props_to_html(), prop_str)

  def test_not_eq1(self):
    props = {
      "href": "https://www.google.com",
      "target": "_blank",
    }
    node = LeafNode("p", "Just Text", props)
    node2 = LeafNode("a", "Just Text", props)
    self.assertNotEqual(node, node2)

if __name__ == "__main__":
  unittest.main()