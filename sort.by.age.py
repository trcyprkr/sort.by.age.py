import os
from time import sleep
list = []
path = r'D:\DCIM\Camera'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
list.append(files)
oldest = files[0]
newest = files[-1]

#print("Oldest:", oldest)
#print("Newest:", newest)
print("All by modified oldest to newest:", list)
sleep(1)  
