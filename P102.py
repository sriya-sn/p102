import os
import shutil

path = os.getcwd()
print(path)
#os.mkdir("black")
files = os.listdir("/Users/poornimaponnuswamy/Desktop")
print(files)
exist = os.path.exists("/Users/poornimaponnuswamy/Desktop/abc")
print(exist)
name,ext=os.path.splitext("/Users/poornimaponnuswamy/Desktop/abc.png")
print("the name of the file is ",name)
print("the ext of the file is",ext)



source = "/Users/poornimaponnuswamy/Downloads/abc"
destination = "/Users/poornimaponnuswamy/Desktop"
files = os.listdir(source)
for i in files:
    name, ext = os.path.splitext(i)
    if ext == "":
        continue
    if ext in['.txt','.doc','.docx','.pdf']:
        path1 = source + '/' + i
        path2 = destination + '/' + "Document_Files"
        path3 = destination + '/' + "Document_Files" + '/' + i

        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("creating and moving")
            shutil.move(path1,path3)
        