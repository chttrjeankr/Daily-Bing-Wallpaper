import datetime
import os
from daily_defn import *

# file = requests.get("https://www.bing.com/")
# soup = bs4.BeautifulSoup(file.text,"xml")
# subs = ''
# linkList = soup.find_all('script', type=re.compile("text/javascript"))
name, linkList = defn()
url = ''
for i in linkList:
    find = 'g_img={url: '
    i_str = str(i)
    try:
        beg = i_str.index(find) + len(find) + 1
        end = i_str.index('"', beg)
        url = i_str[beg:end]
        # print(subs)
        break
    except:
        continue

# webbrowser.open("https://www.bing.com/"+url)
path = "C:\\Users\chttr\PycharmProjects\BingHomepageWallpaper\Images Downloaded"
imgname = datetime.date.today().__str__() + " " + name + ".jpg"
imgfile = os.path.join(path,imgname)
with open(imgfile,'wb') as f:
    f.write(requests.get("https://www.bing.com/"+url).content)
print("Done Perfectly!")