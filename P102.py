import os
import shutil
from_dir = "C:/Users/29rra/Downloads"
to_dir = "C:/Users/29rra/Downloads/new"
list_of_files = os.listdir(from_dir)
#print (list_of_files)
#list = os.listdir(source)
for i in list_of_files:
    name, ext = os.path.splitext(i)
    if (ext==""):
        continue
    if (ext in [".gif", ".png"]):
        #os.chdir(destination)
        #os.mkdir("gif")
        #dest="C:/Coding/Python/C102_assets-main/gif"
        path1=from_dir+"/"+i
        print(path1)
        path2=to_dir + '/' + "new"
        path3=to_dir + '/' + "Document_Files" + '/' + i
        #shutil.move(path1, path2)
    #if os.path.exists(path2):
        #print("Moving" + i + ".....")
        #shutil.move(path1, path3)
    #else:
        os.makedirs(path2)
        print("Moving" + i + ".....")
        shutil.move(path1, path3)