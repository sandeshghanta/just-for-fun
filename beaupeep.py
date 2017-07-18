def isok(mypath):
    request = requests.get(mypath)
    if request.status_code == 200:
        print('Web site exists')
        return True
    else:
        print('Web site does not exist')
        return False
import requests
import httplib
import urllib2
import os
link = "001/1"
for i in range(1,11):
    newpath = "C:\\Users\\sandesh\\Desktop\\beau-peep\\book" + str(i) +"\\"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    check = 1
    num = 1
    while (check == 1):
        if (i == 11 or i == 10):
            url = "http://www.omgbeaupeep.com/comics/mangas/Beau Peep/0"+str(i)+" - Beau Peep Book "+str(i)+"/Beau-Peep-Book-"+str(i)+"-Page-" 
        else:
            url = "http://www.omgbeaupeep.com/comics/mangas/Beau Peep/00"+str(i)+" - Beau Peep Book "+str(i)+"/Beau-Peep-Book-"+str(i)+"-Page-"
        if (num < 10):
            url = url + "00" + str(num)+ '.jpg'
        else:
            url = url + "0" + str(num)+ '.jpg' 
        print 'wt'
        if (isok(url)):
            print 'w'
            page = requests.get(url)
            local = newpath + str(num)+".jpg"
            with open(local,'wb') as pic:
                pic.write(page.content)
            num = num + 1
            print num
    print i


