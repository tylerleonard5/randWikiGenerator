from bs4 import BeautifulSoup
import requests
import webbrowser

while (True):
    wiki = "http://en.wikipedia.org/wiki/Special:Random"

    url = requests.get(wiki)
    soup = BeautifulSoup(url.text, 'html.parser')

    title = soup.find("h1", {"id": "firstHeading"}).string

    print("Random article generated: " + title)


    response = input("Do you want to check out this wikipedia article?\n")


    if (response == "y" or response == "yes"):
        webbrowser.open(url.url)
        break



