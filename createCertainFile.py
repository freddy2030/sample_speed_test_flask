import os
import random

def genSizeFile(fileSize):
    #file path
    filePath = os.path.join("./upload", str(fileSize) + "M.txt")
    fileSize = fileSize * 1024 * 1024
    # 生成固定大小的文件
    # date size
    ds=0
    with open(filePath, "w", encoding="utf8") as f:
        f.truncate()
        while ds<fileSize:
            f.write(str(round(random.uniform(-1000, 1000),2)))
            f.write("\n")
            ds=os.path.getsize(filePath)
    print(ds)
    # print(os.path.getsize(filePath))

# start here.
genSizeFile(10)
