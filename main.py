# -*- conding:utf-8 -*-

from tqdm import tqdm
import zipfile
import time
import json
import sys
import os


LICENSE = """~~~~ 欢迎使用备份小助手，全程无需任何操作，你就静静地看着就好！ ~~~~
本程序遵从 MIT 开源许可协议\n
版权所有 (c) 2021, SHENGYUKing\n
特此向任何得到本软件副本或相关文档的人授权：被授权人有权使用、复制、修改、
合并、出版、发布、散布、再授权和/或贩售软件及软件的副本，及授予被供应人
同等权利，只需服从以下义务：\n
在软件和软件的所有副本中都必须包含以上版权声明和本许可声明。\n
该软件是"按原样"提供的，没有任何形式的明示或暗示，包括但不限于为特定目的
和不侵权的适销性和适用性的保证担保。在任何情况下，作者或版权持有人，都无
权要求任何索赔，或有关损害赔偿的其他责任。无论在本软件的使用上或其他买卖
交易中， 是否涉及合同，侵权或其他行为。

关于本软件的用法，建议直接联系相关人士获取，一听就懂，包教包会，为了便于
发布所以直接采用pyinstaller对本程序以.exe单文件形式进行了封装，需要源
代码的可访问本人的GitHub获取https://github.com/SHENGYUKing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
CONFIG_FILE = "BackupHelper.json"
COMPRESSED_MODE = {
    "ZIP_STORED": 0,
    "ZIP_DEFLATED": 8,
    "ZIP_BZIP2": 12,
    "ZIP_LZMA": 14
}


def readConfig(cfgFile, curDir):
    try:
        with open(os.path.join(curDir, cfgFile), "r", encoding="utf-8") as cfg:
            json_cfg = json.load(cfg)
            return json_cfg['BackupDirectory'], json_cfg['CompressedMode']
    except Exception as e:
        print(e)
        return -1


def checkBackupDirs(backupList, absDirs):
    if backupList == -1:
        print("读取配置文件发生错误，请检查BackupHelper.json是否存在或被错误修改！")
        os.system("pause")
        sys.exit(0)
    elif len(backupList) == 0:
        print("配置文件中待备份列表为空，请先按格式填入需要备份的文件夹名称！")
        os.system("pause")
        sys.exit(0)
    else:
        currentDirs = os.listdir(absDirs)
        dictDirs = {x: True for x in currentDirs}
        errorList = []
        backupDirs = []
        for backupDir in backupList:
            try:
                _ = dictDirs[backupDir]
                backupDirs.append(os.path.join(absDirs, backupDir))
            except KeyError:
                errorList.append(backupDir)

        print("当前需要备份的文件夹为：")
        for p in backupList:
            print(p)
        print("总计 %d 个" % len(backupList))

        if len(backupDirs) != 0:
            print("其中成功检测到总计 %d 份" % len(backupDirs))
            if len(errorList) != 0:
                print("其中检测失败总计 %d 份" % len(errorList))
                for p in errorList:
                    print(p)
                print("请检查上述文件是否存在于当前文件夹下！")
                os.system("pause")
                sys.exit(0)
            return backupDirs
        else:
            print("当前文件夹内不存在这些文件夹，请检查本程序和配置文件是否置于正确位置！")
            os.system("pause")
            sys.exit(0)


def checkCompressedMode(compressedMode):
    valid_mode = ["ZIP_STOREED", "ZIP_DEFLATED", "ZIP_BZIP2", "ZIP_LZMA"]
    try:
        compressedMode = compressedMode[0]
        if isinstance(compressedMode, str):
            if compressedMode in valid_mode:
                print("当前压缩模式为：", compressedMode)
                return compressedMode
            else:
                print("读取到错误的压缩模式（模式拼写错误），将使用默认模式（ZIP_DEFLATED）进行压缩！")
                return "ZIP_DEFLATED"
        else:
            print("读取到错误的压缩模式（模式格式错误），将使用默认模式（ZIP_DEFLATED）进行压缩！")
            return "ZIP_DEFLATED"
    except IndexError:
        print("压缩模式设置为空，将使用默认模式（ZIP_DEFLATED）进行压缩！")
        return "ZIP_DEFLATED"


def writeDirToZip(absDirs, absZip, compressedMode):
    try:
        with zipfile.ZipFile(absZip, "w") as target:
            for Dir in tqdm(absDirs):
                for DirTree in os.walk(Dir):
                    for files in DirTree[2]:
                        target.write("".join((DirTree[0], "\\", files)), compress_type=COMPRESSED_MODE[compressedMode])
        print("~~~~~~~~~~~~~~~ 压缩已完成！期待下次使用，再见！ ~~~~~~~~~~~~~~")
        os.system("pause")
        sys.exit(0)
    except Exception as e:
        print(e)
        print("由于发生了上述故障导致压缩进程异常结束，若已经生成压缩包则该压缩包无效！")
        os.system("pause")
        sys.exit(0)


def main():
    print(LICENSE)

    absDirs = os.path.abspath(sys.argv[0])
    absZip = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) + "_" + absDirs.split("\\")[-2] + ".zip"
    absDirs = "\\".join(absDirs.split("\\")[:-1]) + "\\"
    print("当前文件夹绝对路径为:", absDirs)

    backupList, compressedMode = readConfig(CONFIG_FILE, absDirs)
    backupDirs = checkBackupDirs(backupList, absDirs)
    compressedMode = checkCompressedMode(compressedMode)

    absZip = os.path.join(absDirs, absZip)
    writeDirToZip(backupDirs, absZip, compressedMode)


if __name__ == "__main__":
    main()
