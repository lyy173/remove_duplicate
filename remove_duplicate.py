# 正则化图像
def regularizeImage(img, size = (8, 8)):
    return img.resize(size).convert('L')

# 计算hash值
def getAHashCode(img, size = (8, 8)):
    img = regularizeImage(img)
    pixel = []
    for i in range(size[0]):
        for j in range(size[1]):
            pixel.append(img.getpixel((i, j)))

    mean = sum(pixel) / len(pixel)

    result = []
    for i in pixel:
        if i > mean:
            result.append(1)
        else:
            result.append(0)
    
    return result

def getDHashCode(img, size = (8, 8)):
    img = regularizeImage(img)
    result = []
    for i in range(size[0] - 1):
        for j in range(size[1]):
            current_val = img.getpixel((i, j))
            next_val = img.getpixel((i + 1, j))
            if current_val > next_val:
                result.append(1)
            else:
                result.append(0)
    return result

# 比较hash值
def compHashCode(hc1, hc2):
    cnt = 0
    for i, j in zip(hc1, hc2):
        if i == j:
            cnt += 1
    return cnt

from PIL import Image
import os

if __name__ == "__main__":
    image_hash = {}
    imagepath = r'C:\Users\liang\code\idcard\success_orignal\2_quchong'
    for imagename in os.listdir(imagepath):
        image = Image.open(os.path.join(imagepath,imagename))
        image_hash[imagename] = getDHashCode(image)
    
    delete_name = []
    for imagename,hash in image_hash.items():
        if imagename in delete_name:
            continue
        for targetname,targethash in image_hash.items():
            if targetname in delete_name:
                continue
            if imagename == targetname:
                continue
            if compHashCode(hash,targethash) > 50:
                delete_name.append(targetname)
    for delete in delete_name:
        os.remove(os.path.join(imagepath,delete))
    

    

        
