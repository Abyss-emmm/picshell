# picshell
基于Python3,用于拼接图片与shell，两种模式，一种是指定文件类型，另一种是指定图片文件
## 安装说明
```cmd
pip3 install -r requirements.txt
```

## 使用说明
**-t**：指定文件类型，jpg,png,bmp,gif任选一种

**-i**：指定图片文件路径

**-s**：指定shell文件路径，若文件不存在，则认为输入内容为webshell

**-o**：指定图马文件路径

**--ext**：将webshell写入图片中，仅支持png,jpg,tiff,webp格式的图片

`pic`文件夹内提供图片。

可参考别人收集的[webshell](https://github.com/tennc/webshell)
### 指定文件类型
```cmd
python3 picshell.py -t [jpg,png,bmp,gif] -s <webshell> -o <new webshell>
```
### 指定图片文件
```cmd
python3 picshell.py -i <image> -s <webshell> -o <new webshell>
```

### webshell写入图片内部
```cmd
python3 picshell.py --ext -i <image> -s <webshell> -o <new webshell>
```