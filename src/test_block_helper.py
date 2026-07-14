import unittest
from block_helper import *


class TestBlockHelper(unittest.TestCase):
  def test_markdown_to_blocks(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(blocks, [
      "This is **bolded** paragraph",
      "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
      "- This is a list\n- with items",
    ])

  def test_markdown_to_blocks2(self):
    md = """
- This is a single list
- with items
- A
- and B
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(blocks, [
      "- This is a single list\n- with items\n- A\n- and B",
    ])


  def test_block_to_block_type_paragraph(self):
    md = """
This is a parapgraph
- with a bunch of incorrect formatting
### thus forcing it into this junk collection
> Of Garbage
"""
    type = block_to_block_type(md)
    self.assertEqual(type, BlockType.PARAGRAPH)

    
  def test_block_to_block_type_heading(self):
    md = """###### This is a heading
- with a bunch of incorrect formatting
### thus forcing it into this junk collection
> Of Garbage
"""
    type = block_to_block_type(md)
    self.assertEqual(type, BlockType.HEADING)
    

  def test_block_to_block_type_code(self):
    md = """```
This is a code block
- with a bunch of incorrect formatting
### thus forcing it into this junk collection
> Of Garbage
```"""
    type = block_to_block_type(md)
    self.assertEqual(type, BlockType.CODE)


  def test_block_to_block_type_quote(self):
    md = """> This whole set
>> This is a quote block
> > it entirely works as a quote block
>>"""
    type = block_to_block_type(md)
    self.assertEqual(type, BlockType.QUOTE)


  def test_block_to_block_type_unordered_list(self):
    md = """- Testing
- This is an unordered list block
- with these
- items"""
    type = block_to_block_type(md)
    self.assertEqual(type, BlockType.UNORDERED_LIST)


  def test_block_to_block_type_ordered_list(self):
    md = """90. Testing
1. This is an ordered list block
7. with these
1057. random items"""
    type = block_to_block_type(md)
    self.assertEqual(type, BlockType.ORDERED_LIST)
