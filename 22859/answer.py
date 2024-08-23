import re

def main():
    html = input().strip().replace("\n", "")
    main = re.findall(r"<main>(.*)<\/main>", html)[0]
    divs = re.findall(r'<div title="(.*?)">(.*?)<\/div>', main)
    for title, div in divs:
        print(f"title : {title}")
        for p in re.findall(r"<p>(.*?)<\/p>", div):
            print(
                re.sub(
                    r"\s+", ' ',
                    re.sub(r"<\/?[a-zA-Z ]+>", '', p).strip()
                )
            )

if __name__ == "__main__":
    main()