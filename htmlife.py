import sys
import random
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import webbrowser

def main():
    # exit if they dont prove number
    if len(sys.argv) != 2:
        exit("Usage: python html.py [# of websites]")

    # call search function
    print("")
    links = scrape(int(sys.argv[1]))

    # loop through each randlink and open it, extra prints for spacing
    print("")
    print("Process Succesfull!")
    print("")
    for i in range(len(links)):
        print("Opening: " + str(links[i]))
        webbrowser.open(links[i])
    print("")

def scrape(num):
    """
    Scraps awwards.com, returns (num) links
    """
    # start linklist
    linkList = []

    # iterate for each page
    for i in range(3):
        # set base url
        if i == 0:
            url = "https://www.awwwards.com/websites/nominees/"
        if i == 1:
            url = "https://www.awwwards.com/websites/nominees/?page=2"
        if i == 2:
            url = "https://www.awwwards.com/websites/nominees/?page=3"

        # open connection and grab page
        client = uReq(url)
        html = client.read()
        client.close()

        # create soup object
        souped = soup(html, "html.parser")

        # create link searcher
        linkSearch = souped.findAll("a",{"class":"js-visit-item bt-item bt-link"})

        # create list with all links
        for link in linkSearch:
            link = link["href"]
            linkList += [link]

        # track progress
        print("[" + str(i+1) + "/3] Pages Searched", end='\r')

    #
    randLinks = []
    for i in range(num):
        randLinks += [random.choice(linkList)]
    return randLinks
    

if __name__ == '__main__':
    main()