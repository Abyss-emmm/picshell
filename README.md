# picshell
基于Python3,用于拼接图片与shell，两种模式，一种是指定文件类型，另一种是指定图片文件
## 使用说明
**-t**：指定文件类型，jpg,png,bmp任选一种
**-i**：指定图片文件路径
**-s**：指定shell文件路径
**-o**：指定图马文件路径
`pic`文件夹内提供图片。
### 指定文件类型
```cmd
python3 picshell.py -t [jpg,png,bmp] -s <webshell> -o <new webshell>
```
### 指定图片文件
```cmd
python3 picshell.py -i <image> -s <webshell> -o <new webshell>
```
