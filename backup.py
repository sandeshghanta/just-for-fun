import inspect
import datetime
import os
import shutil
import tempfile
lis = []
extlis = []
def func(url):
    for i in os.listdir(url):
        if (i.find('.') != -1):
            ext = i[i.find('.')+1:]
            if (ext == 'png' or ext == 'jpg' or ext == 'jpeg' or ext == 'gif'):
                print url + '\\' + i
                extlis.append(ext)
                lis.append(url + '\\' + i)
        elif (os.path.isdir(url+'\\'+i)):
            func(url + '\\' + i)
        else:
            len(lis)
    return 1
url = inspect.stack()[0][1]
length = len(url)
i = length - 1 
while (i >= 0):
    if (url[i] == '\\'):
        url = url[:i]
        break
    i = i - 1
func(url)
print lis
print len(lis)
now = datetime.datetime.now()
name = now.strftime("%d-%m-%Y")
name = url + '\\' + name
if not os.path.exists(name):
    os.makedirs(name)
name = name + '\\' + "images" + '\\'
os.makedirs(name)
count = 1
for i in lis:
    src = i
    j = 0
    while (j < len(i)):
        if (i[j] == '\\'):
            dst = i[j:]
            break    
        j = j + 1    
    copyfile(src, dst)
        
        
