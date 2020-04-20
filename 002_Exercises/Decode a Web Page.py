import requests
from bs4 import BeautifulSoup

base_url = 'http://www.onet.pl'
r = requests.get(base_url)
features = "html.parser"
soup = BeautifulSoup(r.text)

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())
