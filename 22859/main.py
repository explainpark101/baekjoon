from __future__ import annotations
import re
from typing import Optional

class reSearch:
    Match: Optional[re.Match[str]]
    def __init__(self, pattern: str, string: str) -> None:
        self.Match = re.search(pattern, string)
    def start(self):
        if self.Match is None:
            return 0
        return self.Match.start()
    def end(self):
        if self.Match is None:
            return 0
        return self.Match.end()

class Element:
    tag: str = ""
    childList: list[Element]
    argumentDict:dict[str, str]
    innerHTML: str

    @property
    def tagName(self) -> str:
        tagIndex = reSearch(r"<[a-zA-Z]+[ >]", self.tag)
        return self.tag[tagIndex.start()+1:tagIndex.end()-1].strip()
    @property
    def tagNameRegex(self) -> str:
        return "".join([f"[{_.lower()}{_.upper()}]" for _ in self.tagName])

    @property
    def attributes(self) -> dict[str, str]:
        if self.argumentDict: return self.argumentDict
        for kvs in re.findall(r"((([^ <>]*)*=[\"\']([^ <>]*)*[\"\'])*)",self.tag):
            for kv in kvs:
                if "=" not in kv: continue
                k, v = kv.split("=")
                self.argumentDict[k.strip()] = v[1:-1]
        return self.argumentDict

    def __init__(self, html: str) -> None:
        self.childList = list()
        self.argumentDict = dict()
        if not html: return
        _searched = reSearch(r"<[a-zA-Z]+[ ]*([^ <>]*=[\"\'][^ <>]*[\"\'])*[ ]*>", html)
        self.tag = html[_searched.start():_searched.end()].strip()
        if self.tagName == 'br': return None
        if ">" not in html:
            self.tag = "#text"
            self.innerHTML = html
            return None
        tagIndex = reSearch(f"(<\\/[ ]*{self.tagNameRegex}[ ]*>)", html)
        self.innerHTML = html[_searched.end():tagIndex.start()]
        self.innerHTML = self.innerHTML.replace("\n", "")
        # self.innerHTML = re.sub(r"<[bB][rR][ ]*>", "\n", self.innerHTML)
        innerHTML = self.innerHTML

        if "<" not in innerHTML:
            return

        elementHTMLList = []
        while innerHTML:
            openTags = re.findall(r"<([a-zA-Z]+)[ >]?", innerHTML)
            if len(openTags):
                openTag = openTags[0].strip().replace(">", "")
                if openTag.lower() == 'br':
                    innerHTML = re.sub(r"<[bB][rR][ ]*>", "\n", innerHTML)
                    continue
                reg = "".join([f"[{_.lower()}{_.upper()}]" for _ in openTag])
                endTagMatch = reSearch(f"<\\/{reg}[ ]*>", innerHTML)
                outerHTML = innerHTML[:endTagMatch.end()]
                elementHTMLList.append(outerHTML)
                innerHTML = innerHTML[len(outerHTML):]
            else: return
        self.childList = [Element(outerHTML) for outerHTML in elementHTMLList]

    @property
    def opening(self) -> str:
        if self.attributes == {}:
            return f"<{self.tagName}>"
        return f"<{self.tagName} {' '.join(('='.join(kv) for kv in self.attributes.items()))}>"
    @property
    def closing(self) -> str:
        return f"</{self.tagName}>"

    def __str__(self) -> str:
        return f"<{self.tagName} {' '.join(('='.join(kv) for kv in self.attributes.items()))}>" + f"</ {self.tagName}>"

    def __repr__(self) -> str:
        return f"<Element[{self.tagName}] object at {id(self):0x}>"

def printTree(element: Element, recurse=0) -> None:
    print("\t"*recurse+element.opening)
    if element.childList == []:
        print("\t"*recurse+element.innerHTML)
    else:
        for child in element.childList:
            printTree(child, recurse+1)
    print("\t"*recurse+element.closing)

def print_answer(element: Element) -> None:
    print(f"title : {element.attributes.get('title')}")
    for child in element.childList:
        print(
            re.sub(
                r"<[a-zA-Z]+[ ]*([^ <>]*=[\"\'][^ <>]*[\"\'])*[ ]*>",
                "",
                re.sub(
                    r"<\/[a-zA-Z]+[ ]*>",
                    "",
                    re.sub(
                        r"<\/[pP][ ]*>",
                        "\n",
                        re.sub(
                            r"<[bB][rR][ ]*>",
                            "\n",
                            child.innerHTML
                        )
                    )
                )
            )
        )

def main():
    html = input().strip()
    mainElement = Element(html)
    # print("========Tree========")
    for div in mainElement.childList:
        print_answer(div)


    return None

if __name__ == "__main__":
    main()