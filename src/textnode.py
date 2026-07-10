from enum import Enum


#example enum
class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"


class TextTypeMarkdown(Enum):
    PLAIN = ""      # text (plain)
    BOLD = "**"     # **Bold text**
    ITALIC = "_"    # _Italic text_
    CODE = "`"      # `Code text`
    LINK = "["      # [anchor text](url)
    IMAGE = "!["    # ![alt text](url)

class TextType(Enum):
    PLAIN = "plain"    # text (plain)
    BOLD = "*bold"     # **Bold text**
    ITALIC = "italic"  # _Italic text_
    CODE = "code"      # `Code text`
    LINK = "link"      # [anchor text](url)
    IMAGE = "image"    # ![alt text](url)


class TextNode():

    def __init__(self, text:str, text_type:TextType, url:str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: 'TextNode') -> bool:
        return (self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"