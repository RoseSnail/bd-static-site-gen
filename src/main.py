import os, shutil, sys
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
    source_path = f"{source}/{content}"
    destination_path = f"{destination}/{content}"
    if os.path.isfile(source_path):
      #print(f"File: {content}")
      shutil.copy(source_path, destination_path)
    elif os.path.isdir(source_path):
      #print(f"Dir: {content}")
      copy_dir_contents(source_path, destination_path)
    else:
      print(f"Unknown: {source_path}")


def extract_title(markdown:str) -> str:
  lines = markdown.split("\n")
  for line in lines:
    if len(line) > 2 and line[0] == '#' and line[1] != '#':
      return line[1:].strip()
  raise Exception("No title found")


def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str = "/") -> int:
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
  template = template.replace("{{ Title }}", extract_title(contents))
  template = template.replace("{{ Content }}", node.to_html())
  template = template.replace('href="/', f'href="{basepath}')
  template = template.replace('src="/', f'src="{basepath}')
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
  written_chars = 0
  with open(dest_path, "w") as file:
    written_chars = file.write(template)
  return written_chars
  
  
def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str = "/") -> int:
  count = 0

  if not os.path.exists(dest_dir_path):
    os.makedirs(dest_dir_path)
  contents = os.listdir(dir_path_content)
  #print(contents)
  for content in contents:
    source_path = f"{dir_path_content}/{content}"
    destination_path = f"{dest_dir_path}/{content}"
    if os.path.isfile(source_path) and source_path[-3:] == ".md":
      #print(f"File: {content}")
      #shutil.copy(source_path, destination_path)
      count += generate_page(source_path, template_path, f"{destination_path[:-3]}.html", basepath)
    elif os.path.isdir(source_path):
      #print(f"Dir: {content}")
      #copy_dir_contents(source_path, destination_path)
      count += generate_pages_recursive(source_path, template_path, destination_path, basepath)
    else:
      print(f"Unknown: {source_path}")
  
  return count
  


def main():
  args = sys.argv
  basepath = args[1] if len(args) > 1 else "/"
  #print(basepath)

  #shutil.rmtree("public")
  copy_contents_from_to('static', 'docs')
  #count = generate_page('content/index.md', 'template.html', 'public/index.html')
  count = generate_pages_recursive('content', 'template.html', 'docs', basepath)
  print(f"generated {count} characters")
  #node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
  #print(node)


if __name__ == "__main__":
  main()
