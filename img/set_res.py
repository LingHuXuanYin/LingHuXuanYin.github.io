from PIL import Image
import os,shutil

srcFile = "./top_img.jpg"
dstFile = "./top_img.jpg"
if os.path.isfile(srcFile) and srcFile.endswith(".jpg"):
    try:
        #打开原图片缩小后保存，可以用if srcFile.endswith(".jpg")或者split，splitext等函数等针对特定文件压缩
        sImg=Image.open(srcFile)
        w,h=sImg.size
        dImg=sImg.resize((int(w/2),int(h/2)),Image.ANTIALIAS)  #设置压缩尺寸和选项，注意尺寸要用括号
        dImg.save(dstFile) #也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的
        print (dstFile+" 成功！")
    except Exception:
        print(dstFile+"失败！")