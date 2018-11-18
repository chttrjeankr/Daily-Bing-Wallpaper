import requests
import bs4
import re


def defn():
    """
    Fetches the title of the daily bing image from the website
    :return: the title, the soup object from bs4
    """
    file = requests.get("https://www.bing.com/")
    soup = bs4.BeautifulSoup(file.text, "xml")

    linkList = soup.find_all('script', type=re.compile("text/javascript"))
    for i in linkList:
        find = '_H.mcImgData ={"copyright":"'
        i_str = str(i)
        try:
            ind = i_str.index(find) + len(find)
            title = i_str[ind: i_str.index(' (', ind + 1)]
            title = title.encode('ascii').decode('unicode_escape')
            return (title, linkList)
        except:
            continue