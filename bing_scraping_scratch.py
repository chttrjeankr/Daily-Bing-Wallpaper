import requests
import bs4
import re
import webbrowser

file = requests.get("https://www.bing.com/")
soup = bs4.BeautifulSoup(file.text,"xml")

pretty = soup.prettify()
# print(pretty)

subs = ''
linkList = soup.find_all('script', type=re.compile("text/javascript"))
for i in linkList:
    print(i)
    print()
#     try:
#         print(i.index("g_img"))
#     except:
#         print()
#         continue
#     print()
#     find = "g_img={url: "
#     istr = str(i)
#     try:
#         ind = istr.index(find)+ len(find)
#         subs = istr[ind+1:istr.index('"',ind+1)]
#         print(subs)
#     except:
#         continue
#
# webbrowser.open("https://www.bing.com/"+subs)