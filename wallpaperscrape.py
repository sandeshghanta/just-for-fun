import requests
import shutil
from bs4 import BeautifulSoup
url = "https://www.geckoandfly.com/13248/40-free-motivational-inspirational-quotes-wallpapers-posters/"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data,"html.parser")
linklist = []
for link in soup.find_all('a'):
    linklist.append(link.get('href'))
    #print link.get('href')
imagelist = []
for i in linklist:
    if (i.find('.jpg') != -1 or i.find('.png') != -1 or i.find('.jpeg') != -1):
        imagelist.append(i)
        print i
count = 0
for i in imagelist:
    print i
    response = requests.get(i, stream=True)
    name = "img"+str(count)+".jpg"
    with open(name,'wb') as f:
        f.write(response.content)
    del response
    count = count + 1
    print count
