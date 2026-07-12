import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

  def test_eq(self):
    props = {
      "class": "main secondary",
    }
    leaf = LeafNode("b", "Bold text")
    node = ParentNode("p", [leaf], props)
    node2 = ParentNode("p", leaf, props)
    self.assertEqual(node, node2)

  def test_eq1(self):
    props = {
      "class": "main secondary",
    }
    leaf = LeafNode("b", "Bold text")
    leaf1 = LeafNode(None, "Normal text")
    leaf2 = LeafNode("i", "italic text")
    leaf3 = LeafNode(None, "normal text")
    html_str = '<p class="main secondary"><b>Bold text</b>Normal text<i>italic text</i>normal text</p>'
    node = ParentNode("p", [leaf, leaf1, leaf2, leaf3], props)
    self.assertEqual(node.to_html(), html_str)

  def test_eq2(self):
    props = {
      "class": "main secondary",
    }
    leaf = LeafNode("b", "Bold text")
    parent_node_str = f"ParentNode(a, {[leaf]}, {props})"
    node = ParentNode("a", [leaf], props)
    self.assertEqual(str(node), parent_node_str)

  def test_raise(self):
    props = {
      "class": "main secondary",
    }
    node = ParentNode(None, LeafNode(None, "Leaf 1 text"), props)
    with self.assertRaises(ValueError):
      node.to_html()

  def test_raise1(self):
    props = {
      "class": "main secondary",
    }
    node = ParentNode("p", None, props)
    with self.assertRaises(ValueError):
      node.to_html()

  def test_not_eq(self):
    node = ParentNode("p", None)
    node2 = ParentNode(None, None)
    self.assertNotEqual(node, node2)

  def test_not_eq1(self):
    props = {
      "class": "main secondary",
      "style": "color: blue;"
    }
    leaf = LeafNode("b", "Bold text")
    leaf1 = LeafNode(None, "Normal text")
    prop_str = f'class="main secondary" style="color: blue;"'
    node = ParentNode("p", [leaf, leaf1], props)
    self.assertNotEqual(node.props_to_html(), prop_str)

  def test_not_eq1(self):
    props = {
      "class": "main secondary",
      "style": "color: blue;"
    }
    leaf = LeafNode("b", "Bold text")
    leaf1 = LeafNode(None, "Normal text")
    node = ParentNode("p", [leaf, leaf1], props)
    node2 = ParentNode("p", [leaf1], props)
    self.assertNotEqual(node, node2)

if __name__ == "__main__":
  unittest.main()