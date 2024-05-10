import struct
import numpy as np
from PIL import Image  # PIL就是pillow库


def color565(r, g, b):
    return (r & 0xf8) << 8 | (g & 0xfc) << 3 | b >> 3

def main():
    img = Image.open(name)
    print(img.format, img.size, img.mode)
    img_data = np.array(img)  # 240行240列有3个 240x240x3

    with open(name, "wb") as f:
        for line in img_data:
            for dot in line:
                f.write(struct.pack("H", color565(*dot))[::-1])


if __name__ == '__main__':
    for i in range(1, 19):
        name = "c"+ str(i) + ".png"
        main()
