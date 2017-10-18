import requests
for i in range(1,144):
    link = 'http://www.readcomics.tv/images/manga/bone/1/%s.jpg'%(i)
    data = requests.get(link)
    local = '%s.jpg'%(i)
    with open(local,'wb') as pic:
        pic.write(data.content)
    print i
