import os
searchcount = 0
imgcount = 0
dic = {}
def check(ext):
	ext = ext.lower()
	ext = ext[1:]
	if (ext == 'mp3' or ext == 'mp4' or ext == 'avi' or ext == 'jpg' or ext == 'jpeg' or ext == 'png'):
		return True
	return False
def func(path):
	global searchcount
	global imgcount
	searchcount = searchcount + 1
	if (searchcount%100 == 0):
		print "No of searches performed " + str(searchcount)
		print "No of images found " + str(imgcount)
	name,ext = os.path.splitext(path)
	if check(ext):
		if os.path.basename(path) not in dic:
			name = os.path.basename(path)
			dic[name] = path
			imgcount = imgcount + 1
			#fil.write(name)
			#fil.write('\n')
			fil.write(path)
			fil.write('\n')
	if os.path.isdir(path):
		for i in os.listdir(path):
			func(path+'/'+i)    
fil = open("path.txt",'w+')
func('E:')
fil.close()

	
