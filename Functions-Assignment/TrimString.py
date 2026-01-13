import html

def cleanString(s):
    return " ".join(html.unescape(s).split())

s = "Hello &amp; Welcome &nbsp; to Python!"
print(cleanString(s))