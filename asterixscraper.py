import os
import urllib

from bs4 import BeautifulSoup
for i in range(1,35):
    link = "http://www.omgbeaupeep.com/comics/Asterix/"+str(i)+"/"
    r = requests.get(link)
    soup = BeautifulSoup(r.text,"html.parser")
    url = soup.find("img",{"class":"picture"}).get('src')
    flag = False
    foldername = ''
    for i in url:
        if (i == '-'):
            flag = True
        if flag:
            foldername = foldername + i
            if (i == '/'):
                break
    foldername = foldername[2:]
    os.mkdir(foldername)
    flag = True
    endlink = 1
    while (flag):
        url = link + str(endlink)
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        if (soup.find("div",{"class":"warn"})):
            break
        else:
            imglink = 'http://www.omgbeaupeep.com/comics/' + soup.find("img",{"class":"picture"}).get('src')
            resource = urllib.urlopen(imglink)
            localname = str(endlink) + ".jpg"
            output = open(foldername+localname,"wb")
            output.write(resource.read())
            output.close()
            print localname
        endlink = endlink + 1
