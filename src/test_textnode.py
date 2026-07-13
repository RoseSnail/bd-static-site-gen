import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode

# Available tests
####
# assertEqual(a, b)    a == b
# assertNotEqual(a, b) a != b
# assertTrue(x)        bool(x) is True
# assertFalse(x)       bool(x) is False
# assertIs(a, b)       a is b
# assertIsNot(a, b)    a is not b
# assertIsNone(x)      x is None
# assertIsNotNone(x)   x is not None
# assertIn(a, b)       a in b
# assertNotIn(a, b)    a not in b
# assertIsInstance(a, b)     isinstance(a, b)
# assertNotIsInstance(a, b)  not isinstance(a, b)
# assertIsSubclass(a, b)     issubclass(a, b)
# assertNotIsSubclass(a, b)  not issubclass(a, b)
####
# assertRaises(exc, fun, *args, **kwds)          fun(*args, **kwds) raises exc
# assertRaisesRegex(exc, r, fun, *args, **kwds)  fun(*args, **kwds) raises exc and the message matches regex r
# assertWarns(warn, fun, *args, **kwds)          fun(*args, **kwds) raises warn
# assertWarnsRegex(warn, r, fun, *args, **kwds)  fun(*args, **kwds) raises warn and the message matches regex r
# assertLogs(logger, level)    The with block logs on logger with minimum level
# assertNoLogs(logger, level)
####

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)

  def test_eq_1(self):
    node = TextNode("This is a text node", TextType.TEXT)
    node2 = TextNode("This is a text node", TextType.TEXT, None)
    self.assertEqual(node, node2)

  def test_eq_2(self):
    node = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
    node2 = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
    self.assertEqual(node, node2)
    
  def test_eq_3(self):
    node = TextNode("This is a text node", TextType.TEXT, "https://www.test.com")
    node_str = "TextNode(This is a text node, text, https://www.test.com)"
    self.assertEqual(str(node), node_str)
    
  def test_not_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a different text node", TextType.BOLD)
    self.assertNotEqual(node, node2)
    
  def test_not_eq1(self):
    node = TextNode("This is a text node", TextType.BOLD, None)
    node2 = TextNode("This is a text node", TextType.BOLD, "None")
    self.assertNotEqual(node, node2)
    
  def test_not_eq_2(self):
    node = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
    node2 = TextNode("This is a text node", TextType.TEXT, "https://www.test.com")
    self.assertNotEqual(node, node2)
    
  def test_not_eq_3(self):
    node = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
    node2 = TextNode("This is a text node", TextType.BOLD, "https://www.no-test.com")
    self.assertNotEqual(node, node2)
    
  def test_not_eq_4(self):
    node = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
    node_str = "TextNode(This is a text node, TextType.BOLD, https://www.test.com)"
    self.assertNotEqual(str(node), node_str)

  def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = TextNode.text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")
    
  def test_text1(self):
    node = TextNode("This is an image node", TextType.IMAGE, "http://imageurl.png")
    html_node = node.to_html_node()
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.props_to_html(), ' src="http://imageurl.png" alt="This is an image node"')

  def test_text2(self):
    node = TextNode("This is a link node", TextType.LINK, "http://linkurl.com")
    html_node = node.to_html_node()
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "This is a link node")
    self.assertEqual(html_node.props_to_html(), ' href="http://linkurl.com"')

if __name__ == "__main__":
  unittest.main()