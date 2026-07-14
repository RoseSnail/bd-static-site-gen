import os
import shutil
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

def main():
  copy_contents_from_to('static', 'public')
  #node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
  #print(node)


if __name__ == "__main__":
  main()
