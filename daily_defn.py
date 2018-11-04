import requests
import bs4
import re


def defn():
    """
    
    :return:
    """
    file = requests.get("https://www.bing.com/")
    soup = bs4.BeautifulSoup(file.text, "xml")

    linkList = soup.find_all('script', type=re.compile("text/javascript"))
    for i in linkList:
        find = '_H.mcImgData ={"copyright":"'
        i_str = str(i)
        try:
            ind = i_str.index(find) + len(find)
            name = i_str[ind: i_str.index(' (', ind + 1)]
            return (name, linkList)
        except:
            continue