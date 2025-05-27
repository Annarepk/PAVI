from PIL import Image
from PIL.ImageOps import invert

# # files = "abcçdefgğhijklmnoöprsştuüvyz"
# files = ['textBin']
#
# for name in files:
#     filename = f"Laboratory_7/{name}.bmp"
#
#     with Image.open(filename) as img:
#         # img.save('Laboratory_6/' + name + '.png')
#
#         print(f"{name}: {img.mode}")

with Image.open("Laboratory_7/Bin/textBin.bmp") as img:
    imgInv = invert(img)
    imgInv.save("Laboratory_7/textBinInv.bmp")