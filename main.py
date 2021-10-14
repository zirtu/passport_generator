import os,sys,shutil
import time
import hashlib


day = time.strftime("%d", time.localtime())
print(day)
sourse_path = "test/index.html"


md = hashlib.md5()
md.update(day.encode('utf-8'))
print(md.hexdigest())

md5Path = md.hexdigest()+str(day)
print(md5Path)

os.mkdir(md5Path)
d_path = md5Path+"/"
shutil.copy(sourse_path,d_path)


