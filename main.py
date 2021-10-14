import os,sys,shutil
import time
import hashlib


# creat dir
os.mkdir("passport")


# get day
day = time.strftime("%d", time.localtime())
day_before = str(int(day)-1)
print(day)
print(day_before)

# get sourse file
sourse_path = "test/index.html"


# get md5 code
md = hashlib.md5()
md.update(day.encode('utf-8'))
print(md.hexdigest())
md5Path = str(day)+md.hexdigest()
print(md5Path)

os.mkdir("passport/"+md5Path)
d_path = "passport/"+md5Path+"/"
shutil.copy(sourse_path,d_path)


md2 = hashlib.md5()
md2.update(day_before.encode('utf-8'))
print(md2.hexdigest())
md5Path2 = str(day_before)+md2.hexdigest()
print(md5Path2)

os.mkdir("passport/"+md5Path2)
d_path2 = "passport/"+md5Path2+"/"
shutil.copy(sourse_path,d_path2)





