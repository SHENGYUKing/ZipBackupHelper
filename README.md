# ZipBackupHelper - 压缩备份小助手

In daily study and work,  I regularly need to zip and pack some of directories in my personal file,  but every time always need to go through the "Check Directories -> Single Right-click -> Bandizip -> Rename" process. Although the truth is that it doesn't take me much time, wouldn't it be nice to have a  gadget that could do all of this with a single double-click? So I don't just keep it in my mind, but also make it in Python!

在日常学习和工作中，我经常需要定期对个人文件夹下的某些文件进行压缩打包备份，但是每次总是需要经历“复选文件夹 -> 右键单击 -> 压缩打包 -> 重命名”的过程。虽然实际操作时间可能没花费多大的功夫，但是如果能有一款小工具可以只用双击一下就能完成上述的所有工作岂不是更好？所以我便不止停留于想，而且还把它用Python做了出来！

---

## Requirements - 语言版本与模块需求

### base:

>  Python 3.8.12

### module:

> tqdm 4.62.3    
> zipfile (in-built)    
> time (in-built)    
> json (in-built)    
> sys (in-built)    
> os (in-built)    

---

## Directory - 文件夹结构

- test1: dir, files for testing
- test2: dir, files for testing
- test3: dir, files for testing
- BackupHelper.json: .json file, config file for main.py, need to be placed in the same directory as main.py or main.exe
- main.py: .py file, the main program written by Python
- package.zip: .zip file, the zip-package containing .exe file already compiled and packaged with pyinstaller
- sf.ico: .ico file, my favorite logo

test1、test2、test3均为测试用例，仅供开发使用；BackupHelper.json为配置文件需要和main.py或main.exe（之后可以重命名.exe文件，不影响正常使用）放置在统一目录下，后续用户可根据自己的需要对其进行修改；main.py是本工具的主程序Python代码，遵从MIT开源协议；package.zip是为了便于用户使用已经打包好的工具软件，打包中使用了pyinstaller的单文件模式；sf.ico使我最喜欢使用的工具图标，后续可能根据开发热情和需求形成一整个“咸鱼办公小玩意儿”系列！

---

## Using - 使用说明

1. Put the .exe and .josn in the same directory. 
   将.exe和.json文件放在同一个工作目录下

2. Read ***Description*** in BackupHelper.json, and modify  ***BackupDirectory***. 
   阅读.json文件中的描述并根据指导修改当前配置

3. Double-click the .exe and you will ... 
   双击.exe程序然后看看会发生啥...

PS: Please leave me a message if something goes wrong during this process.
       如果在此过程中发生了什么问题欢迎给我留言。
