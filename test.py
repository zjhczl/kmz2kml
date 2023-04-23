import zipfile
import re
import os


def unZip(filePath):

    f = zipfile.ZipFile(filePath, 'r')  # 压缩文件位置
    for file in f.namelist():
        f.extract(file, "./")               # 解压位置
    f.close()


def readFile(filePath):

    file_object = open(filePath, 'r', encoding='utf-8')  # 创建一个文件对象，也是一个可迭代对象
    try:
        all_the_text = file_object.read()  # 结果为str类型
        return all_the_text
    finally:
        file_object.close()


def kmz2Kml(kmzPath):

    unZip(kmzPath)
    txt = readFile('doc.kml')
    T = readFile("T.kml")
    rule = re.compile(' <outerBoundaryIs>(.*?)</outerBoundaryIs>')
    coors = re.findall(rule, txt)[0]
    T = T.replace(
        "<LinearRing><coordinates></coordinates></LinearRing>", coors)
    f = open(kmzPath.replace("kmz", "kml"), 'w', encoding='utf-8')
    f.write(T)
    f.close()


kmzs = os.listdir("./kmz")
for kmz in kmzs:
    if "kmz" in kmz:
        print("./kmz/"+kmz+"-->"+("./kmz/"+kmz).replace("kmz", "kml"))
        kmz2Kml("./kmz/"+kmz)
