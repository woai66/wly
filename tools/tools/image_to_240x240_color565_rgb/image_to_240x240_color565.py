import struct
import numpy as np
from PIL import Image  # PIL就是pillow库


#如提示PNG图片为RGBA格式，则在函数中加入a参数
#def color565(r, g, b):
def color565(r, g, b,a):
    return (r & 0xf8) << 8 | (g & 0xfc) << 3 | b >> 3


def main():
    img = Image.open("hzcu.png")
    print(img.format, img.size, img.mode)
    img_data = np.array(img)  # 240行240列有3个 240x240x3

    with open("hzcu.dat", "wb") as f:
        for line in img_data:
            for dot in line:
                f.write(struct.pack("H", color565(*dot))[::-1])


if __name__ == '__main__':
    main()
