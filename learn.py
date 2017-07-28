import random
import string
ans = ""
data = str(raw_input("Enter the string you want to generate "))
size = len(data)
stri = ""
for i in range (0,size):
    stri = stri + random.choice(string.ascii_letters)
print "The random string made is"
print stri
print "Watch it become into the string you give"
lis = []
count= 0
for i in range (0,size):
    if (stri[i] != data[i]):
        lis.append(i)
while (len(lis) != 0):
    for i in lis:
        el = random.choice(string.ascii_letters + string.digits + string.whitespace)
        stri = stri[:i] + el + stri[i+1:]
        if (stri[i] == data[i]):
            lis.remove(i)
    print "Generation number is ",
    print count,
    print "String is ",
    print stri
    count = count + 1
