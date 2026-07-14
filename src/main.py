import os
import shutil
from functions import markdown_to_html_node
from textnode import TextNode, TextType


def copy_contents_from_to(source: str, destination: str) -> None:
  invalid_sources = ["src", "./src", "public", "./public", "solution", "./solution"]
  invalid_destinations = ["src", "./src", "static", "./static", "solution", "./solution"]
  if source in invalid_sources or destination in invalid_destinations:
    raise Exception("Wrong directory passed! Cannot use certain directories")

  #print(f'delete contents of destination: "{destination}"')
  if os.path.exists(destination):
    shutil.rmtree(destination)
  os.makedirs(destination)
  
  #print(f'copy into destination all files and\n subdirectories, nested files, etc. from: "{source}"')
  copy_dir_contents(source, destination)

def copy_dir_contents(source: str, destination: str):
  if not os.path.exists(destination):
    os.makedirs(destination)
  contents = os.listdir(source)
  #print(contents)
  for content in contents:
    sourcepath = f"{source}/{content}"
    destinationpath = f"{destination}/{content}"
    if os.path.isfile(sourcepath):
      #print(f"File: {content}")
      shutil.copy(sourcepath, destinationpath)
    elif os.path.isdir(sourcepath):
      #print(f"Dir: {content}")
      copy_dir_contents(sourcepath, destinationpath)
    else:
      print(f"Unknown: {sourcepath}")


def extract_title(markdown:str) -> str:
  lines = markdown.split("\n")
  for line in lines:
    if len(line) > 2 and line[0] == '#' and line[1] != '#':
      return line[1:].strip()
  raise Exception("No title found")


def generate_page(from_path: str, template_path: str, dest_path: str):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  if not os.path.isfile(from_path) or from_path[-3:] != ".md":
    raise Exception("markdown filepath is not a valid .md file")
  if not os.path.isfile(template_path) or template_path[-5:] != ".html":
    raise Exception("template filepath is not a valid .html file")
  contents = None
  with open(from_path, "r") as file:
    contents = file.read()
  #print("-------\\\\--Markdown--//-------")
  #print(contents)
  template = None
  with open(template_path, "r") as file:
    template = file.read()
  #print("-------\\\\--Template--//-------")
  #print(template)

  node = markdown_to_html_node(contents)
  #node_string = node.to_html()
  #print("-------\\\\--Markdown-To-Node--//-------")
  #print(node_string)

  #title = extract_title(contents)
  template = template.replace("{{ Title }}", extract_title(contents)).replace("{{ Content }}", node.to_html())
  #template = template.replace("{{ Title }}", title)
  #template = template.replace("{{ Content }}", node.to_html())
  #print("-------\\\\--Updated-Template--//-------")
  #print(template)
  
  # Ensure that filepaths exist
  # dest_path - filename
  #if not os.path.isfile(dest_path - filename):
  #  os.makedirs(dest_path - filename)
  filename = dest_path.split('/')[-1]
  f_length = len(filename) + 1    # add 1 to include the '/' from the last dir reference
  if f_length < len(dest_path) and not os.path.exists(dest_path[:-f_length]):
    #print(dest_path[:-f_length])
    os.makedirs(dest_path[:-f_length])

  # Write updated template to destination filepath
  with open(dest_path, "w") as file:
    file.write(template)
  


def main():
  copy_contents_from_to('static', 'public')
  generate_page('content/index.md', 'template.html', 'public/index.html')
  #node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
  #print(node)


if __name__ == "__main__":
  main()
