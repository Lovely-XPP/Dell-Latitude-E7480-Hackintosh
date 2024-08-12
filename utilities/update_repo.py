import json
import os
import sys
import shutil, copy
import zipfile
import time
import platform
import requests
import hashlib
from plistlib import *

import warnings
warnings.filterwarnings("ignore")

class UpdateRepo:
    def __init__(self) -> None:
        self.ver = "V1.07"
        self.mode = 0
        self.root = os.path.abspath(sys.path[0])
        self.kext = ""
        self.update_kext = ""
        self.update_config = ""
        self.kext_zh = ""
        self.update_kext_zh = ""
        self.changelog = ""
        self.changelog_zh = ""
        self.readme = ""
        self.readme_zh = ""
        self.release_info = ""
        self.oc_ver0 = ""
        self.oc_ver = ""
        self.url = 'https://raw.githubusercontent.com/dortania/build-repo/builds/config.json'
        self.bootloader = ""
        self.kexts_list = []
        self.remote = {}
        self.local = {}
        self.install = 0
        self.config_info = []
        self.update_kext_info = []

        # get MacOS Version
        kernel = platform.system()
        if kernel != "Darwin":
            print("The script is only supported for MacOS !")
            exit()
        t = os.popen('sw_vers').read()
        t = t.split('BuildVersion:')
        t = t[1]
        t = t.strip()
        self.system_ver = t


    def Colors(self, text, fcolor=None, bcolor=None, style=None):
        '''
        User-Defined print text format
        '''
        # Font Color
        fg = {
            'black': '\33[30m',
            'red': '\33[31m',
            'green': '\33[32m',
            'yellow': '\33[33m',
            'blue': '\33[34m',
            'magenta': '\33[35m',
            'cyan': '\33[36m',
            'white': '\33[37m',
            'end': '\33[0m'
        }
        # Background Color
        bg = {
            'black': '\33[40m',
            'red': '\33[41m',
            'green': '\33[42m',
            'yellow': '\33[43m',
            'blue': '\33[44m',
            'magenta': '\33[45m',
            'cyan': '\33[46m',
            'white': '\33[47m',
        }
        #
        st = {
            'bold': '\33[1m',  # Highlight
            'url': '\33[4m',  # Underline
            'blink': '\33[5m',
            'seleted': '\33[7m',
        }

        if fcolor in fg:
            text = fg[fcolor]+text+fg['end']
        if bcolor in bg:
            text = bg[bcolor] + text + fg['end']
        if style in st:
            text = st[style] + text + fg['end']
        return text


    def title(self, size=85):
        title_name = "OpenCore Updater For Dell-Latitude-E7480-Hackintosh"
        l = len(title_name) + len(self.ver) + 1
        title_name = title_name + ' ' + self.Colors(self.ver, fcolor='green')
        if (size % 2) != (l % 2):
            size = size + 1
        print("#"*size)
        space = int(size/2) - int(l/2) - 1
        print("#" + " "*space + title_name + " "*space + "#")
        print("#"*size)
        print("")

    
    def main_interface(self, progress):
        os.system("clear")
        self.title()
        if progress < 1:
            print("> Download Database")
            print("")
            return
        if progress < 2:
            print(self.Colors("- Download Database", fcolor='green'))
            print("> Update OpenCorePkg and Main Kexts")
            print("")
            return
        if self.mode == 1:
            if progress < 3:
                print(self.Colors("- Download Database", fcolor='green'))
                print(self.Colors("- Update OpenCorePkg and Main Kexts", fcolor='green'))
                print("> Update Release Info")
                print("")
                return
            if progress < 4:
                print(self.Colors("- Download Database", fcolor='green'))
                print(self.Colors("- Update OpenCorePkg and Main Kexts", fcolor='green'))
                print(self.Colors("- Update Release Info", fcolor='green'))
                print(self.Colors("> Write README & Changelog"))
                print("")
                return
            if progress < 5:
                print(self.Colors("- Download Database", fcolor='green'))
                print(self.Colors("- Update OpenCorePkg and Main Kexts", fcolor='green'))
                print(self.Colors("- Update Release Info", fcolor='green'))
                print(self.Colors("- Write README & Changelog", fcolor='green'))
                print(self.Colors("> Compress EFI Folder"))
                print("")
                return
            if progress < 6:
                print(self.Colors("- Download Database", fcolor='green'))
                print(self.Colors("- Update OpenCorePkg and Main Kexts", fcolor='green'))
                print(self.Colors("- Update Release Info", fcolor='green'))
                print(self.Colors("- Write README & Changelog", fcolor='green'))
                print(self.Colors("- Compress EFI Folder", fcolor='green'))
                print(self.Colors("> Push & Release"))
                print("")
                return
            print(self.Colors("- Download Database", fcolor='green'))
            print(self.Colors("- Update OpenCorePkg and Main Kexts", fcolor='green'))
            print(self.Colors("- Update Release Info", fcolor='green'))
            print(self.Colors("- Write README & Changelog", fcolor='green'))
            print(self.Colors("- Compress EFI Folder", fcolor='green'))
            print(self.Colors("- Push & Release", fcolor='green'))
            print(self.Colors("- All Done", fcolor='green'))
            print("")
            return
        if progress < 4:
            print(self.Colors("- Download Database", fcolor='green'))
            print(self.Colors("- Update OpenCorePkg and Main Kexts", fcolor='green'))
            print(self.Colors(": Update Release Info, Skipped", fcolor='yellow'))
            print(self.Colors(": Write README & Changelog, Skipped", fcolor='yellow'))
            print(self.Colors(": Compress EFI Folder, Skipped", fcolor='yellow'))
            print(self.Colors("> Push"))
            print("")
            return
        print(self.Colors("- Download Database", fcolor='green'))
        print(self.Colors("- Update OpenCorePkg and Main Kexts", fcolor='green'))
        print(self.Colors(": Update Release Info, Skipped", fcolor='yellow'))
        print(self.Colors(": Write README & Changelog, Skipped", fcolor='yellow'))
        print(self.Colors(": Compress EFI Folder, Skipped", fcolor='yellow'))
        print(self.Colors("- Push", fcolor='green'))
        print(self.Colors("- All Done", fcolor='green'))
        print("")


    def update_kexts(self) -> None:
        root = os.path.abspath(os.path.join(self.root, '..'))
        kext_name = []
        kext_version = []
        kext_time = []
        kext_type = []
        kext_type_zh = []
        header = self.oc_ver0
        header = header.replace('.', '-')
        header_len = len(header)
        info_path = os.path.abspath(os.path.join(self.root, "info"))
        kext_info_path = os.path.join(info_path, "kext")
        for roots, dirs, files in os.walk(kext_info_path):
            for file in files:
                if file[0:header_len] == header:
                    source_file = os.path.join(roots, file)
                    with open(source_file, 'r') as f:
                        update_kext_info = f.readlines()
                        f.close()
        for kext in update_kext_info:
            kext = kext.strip()
            kext = kext + ".kext"
            domain = os.path.abspath(os.path.join(root, 'EFI/OC/Kexts'))
            kext_full = os.path.join(domain, kext)
            plist = os.path.join(kext_full, 'Contents/Info.plist')
            k_time = os.stat(plist).st_mtime
            k_time = time.strftime('%Y-%m-%d', time.localtime(k_time))
            kext_time.append(k_time)
            with open(plist, 'rb') as pl:
                plist = load(pl)
            kext_name.append(plist['CFBundleName'])
            kext_version.append(plist['CFBundleVersion'])
            if kext == 'USBPorts.kext' or kext == 'USBMap.kext':
                kext_type.append('USB Ports Inject')
                kext_type_zh.append('USB 端口注入')
                continue
            build_version = plist['BuildMachineOSBuild']
            if build_version[0:4] == self.system_ver[0:4]:
                kext_type.append('Compile on Local Machine')
                kext_type_zh.append('本地编译')
            else:
                kext_type.append('Official Release')
                kext_type_zh.append('官方编译')

        all_kexts = len(kext_name)
        for i in range(all_kexts):
            for j in range(all_kexts-i-1):
                if kext_name[j] > kext_name[j+1]:
                    temp1 = kext_name[j+1]
                    temp2 = kext_version[j+1]
                    temp3 = kext_time[j+1]
                    temp4 = kext_type[j+1]
                    temp5 = kext_type_zh[j+1]
                    kext_name[j+1] = kext_name[j]
                    kext_version[j+1] = kext_version[j]
                    kext_time[j+1] = kext_time[j]
                    kext_type[j+1] = kext_type[j]
                    kext_type_zh[j+1] = kext_type_zh[j]
                    kext_name[j] = temp1
                    kext_version[j] = temp2
                    kext_time[j] = temp3
                    kext_type[j] = temp4
                    kext_type_zh[j] = temp5
        
        str0 = '| Kexts          | Version                        | Updated Time       | Updated Way              |\n'
        str1 = '|:----------------|:-------------------------------------------|:---------------|:----------------|\n'
        self.update_kext = str0 + str1
        for i in range(len(kext_name)):
            stri = '|\t' + kext_name[i] + '\t|\t' + kext_version[i] + '\t|\t' + kext_time[i] + '\t|\t' + kext_type[i] + '\t|\n'
            self.update_kext = self.update_kext + stri
        
        str0 = '| 驱动名称          | 版本号                       | 更新时间       | 更新方式              |\n'
        str1 = '|:----------------|:-------------------------------------------|:---------------|:----------------|\n'
        self.update_kext_zh = str0 + str1
        for i in range(len(kext_name)):
            stri = '|\t' + kext_name[i] + '\t|\t' + kext_version[i] + '\t|\t' + kext_time[i] + '\t|\t' + kext_type_zh[i] + '\t|\n'
            self.update_kext_zh = self.update_kext_zh + stri


    def kexts(self) -> None:
        root = os.path.abspath(os.path.join(self.root, '..'))
        kext_name = []
        kext_version = []
        kext_time = []
        kext_type = []
        kext_type_zh = []
        first_time = 0
        multiple = 0
        for kext in os.listdir(os.path.join(root, 'EFI/OC/Kexts')):
            if kext == ".DS_Store":
                continue
            if kext[:len("AirportItlwm")] == "AirportItlwm":
                if first_time == 1:
                    multiple = multiple + 1
                    continue
                first_time = 1
            domain = os.path.abspath(os.path.join(root, 'EFI/OC/Kexts'))
            kext_full = os.path.join(domain, kext)
            plist = os.path.join(kext_full, 'Contents/Info.plist')
            k_time = os.stat(plist).st_mtime
            k_time = time.strftime('%Y-%m-%d', time.localtime(k_time))
            kext_time.append(k_time)
            with open(plist, 'rb') as pl:
                plist = load(pl)
            kext_name.append(plist['CFBundleName'])
            kext_version.append(plist['CFBundleVersion'])
            if kext == 'USBPorts.kext' or kext == 'USBMap.kext':
                kext_type.append('USB Ports Inject')
                kext_type_zh.append('USB 端口注入')
                continue
            build_version = plist['BuildMachineOSBuild']
            if build_version[0:4] == self.system_ver[0:4]:
                kext_type.append('Compile on Local Machine')
                kext_type_zh.append('本地编译')
            else:
                kext_type.append('Official Release')
                kext_type_zh.append('官方编译')

        all_kexts = len(kext_name) - multiple
        for i in range(all_kexts):
            for j in range(all_kexts-i-1):
                if kext_name[j] > kext_name[j+1]:
                    temp1 = kext_name[j+1]
                    temp2 = kext_version[j+1]
                    temp3 = kext_time[j+1]
                    temp4 = kext_type[j+1]
                    temp5 = kext_type_zh[j+1]
                    kext_name[j+1] = kext_name[j]
                    kext_version[j+1] = kext_version[j]
                    kext_time[j+1] = kext_time[j]
                    kext_type[j+1] = kext_type[j]
                    kext_type_zh[j+1] = kext_type_zh[j]
                    kext_name[j] = temp1
                    kext_version[j] = temp2
                    kext_time[j] = temp3
                    kext_type[j] = temp4
                    kext_type_zh[j] = temp5

        str0 = '| Kexts          | Version                        | Updated Time       | Updated Way              |\n'
        str1 = '|:----------------|:-------------------------------------------|:---------------|:----------------|\n'
        self.kext = str0 + str1
        for i in range(len(kext_name)):
            stri = '|\t' + kext_name[i] + '\t|\t' + kext_version[i] + '\t|\t' + kext_time[i] + '\t|\t' + kext_type[i] + '\t|\n'
            self.kext = self.kext + stri

        str0 = '| 驱动名称          | 版本号                       | 更新时间       | 更新方式              |\n'
        str1 = '|:----------------|:-------------------------------------------|:---------------|:----------------|\n'
        self.kext_zh = str0 + str1
        for i in range(len(kext_name)):
            stri = '|\t' + kext_name[i] + '\t|\t' + kext_version[i] + '\t|\t' + kext_time[i] + '\t|\t' + kext_type_zh[i] + '\t|\n'
            self.kext_zh = self.kext_zh + stri


    def generate_changelog_readme(self):
        self.update_kexts()
        self.kexts()
        root = os.path.abspath(os.path.join(self.root, '..'))
        now = time.localtime()
        now = time.strftime("%Y.%m.%d", now)
        changelog = os.path.abspath(os.path.join(root, 'Changelog.md'))
        with open(changelog, 'r') as file:
            changelog = file.read()
            file.close()
        changelog = changelog.split('更新日志')
        new = "V" + self.oc_ver + ".0\n\n### Publish date : " + now + \
            "\n\n#### Add Features :\n\n1. Update kexts and OC boot version to  " + \
            self.oc_ver + "\n\n#### Files Changed :\n\n1. All the EFI folder to adapt OC " + \
            self.oc_ver + "\n2. Update kexts with official Release:\n\n" + self.update_kext
        self.changelog = changelog[0] + "更新日志\n\n## " + new + "\n\n-----------------------------------------------------" + changelog[1]
        self.release_info = "# V" + self.oc_ver + ".0\n\n## Publish date : " + now + \
            "\n\n### Add Features :\n\n1. Update kexts and OC boot version to  " + \
            self.oc_ver + "\n\n### Files Changed :\n\n1. All the EFI folder to adapt OC " + \
            self.oc_ver + "\n2. Update kexts with official Release:\n\n" + \
            self.update_kext 
        if len(self.update_config) > 0:
            new = new + "\n\n" + "Config Change:\n" + self.update_config 
        new = new + "\n\n-----------------------------------------------------\n\n"

        readme = os.path.abspath(os.path.join(root, 'README.md'))
        with open(readme, 'r') as file:
            readme = file.read()
            file.close()
        readme = readme.split("OpenCore  ")
        pre_ver = readme[1].split('\n', 1)
        readme = readme[0] + "OpenCore  " + pre_ver[0] + " / " + self.oc_ver + "\n" + pre_ver[1]
        readme = readme.split("## Download")
        tmp = readme[1].split("releases/tag/", 1)
        tmp = tmp[1].split("\n", 1)
        tmp = tmp[1]
        download = "[![Download from https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases](https://img.shields.io/badge/Download-v" + self.oc_ver +  ".0-blue)](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases/tag/v" + self.oc_ver + ".0)"
        readme = readme[0] + "## Download\n" + download + "\n" + tmp
        readme = readme.split("## ChangeLog")
        tmp = readme[1].split("For more information")
        tmp = "For more information" + tmp[1]
        readme = readme[0] + "## ChangeLog: " + new + "\n\n" + tmp

        readme = readme.split("<summary><strong>Kexts Version</strong></summary>")
        tmp = readme[1].split("## Status")
        tmp = "\n</details>\n\n## Status\n" + tmp[1]
        readme = readme[0] + "<summary><strong>Kexts Version</strong></summary>\n</br>\n\n" + self.kext + tmp

        self.readme = readme

        changelog = os.path.abspath(os.path.join(root, 'Changelog_zh.md'))
        with open(changelog, 'r') as file:
            changelog = file.read()
            file.close()
        changelog = changelog.split('更新日志')
        new = "V" + self.oc_ver + ".0\n\n### 发布时间 : " + now + \
            "\n\n#### 添加功能 :\n\n1. 更新OC版本至" + self.oc_ver + "并更新了驱动" + \
            "\n\n#### 文件变化 :\n\n1. 更新整个EFI文件夹以适配 OC " + \
            self.oc_ver + "\n2. 更新驱动:\n\n" + self.update_kext_zh
        self.changelog_zh = changelog[0] + "更新日志\n\n## " + new + "\n\n-----------------------------------------------------" + changelog[1]
        self.release_info = self.release_info + "# V" + self.oc_ver + ".0\n\n## 发布时间 : " + now + \
            "\n\n### 添加功能 :\n\n1. 更新OC版本至" + self.oc_ver + "并更新了驱动" + \
            "\n\n### 文件变化 :\n\n1. 更新整个EFI文件夹以适配 OC " + \
            self.oc_ver + "\n2. 更新驱动:\n\n" + self.update_kext_zh
        if len(self.update_config) > 0:
            new = new + "\n\n" + "配置文件变化:\n" + self.update_config 
        
        readme = os.path.abspath(os.path.join(root, 'README_zh.md'))
        with open(readme, 'r') as file:
            readme = file.read()
            file.close()
        if self.mode == 1:
            readme = readme.split("OpenCore  ")
            pre_ver = readme[1].split('\n', 1)
            readme = readme[0] + "OpenCore  " + pre_ver[0] + " / " + self.oc_ver + "\n" + pre_ver[1]
            readme = readme.split("## 下载")
            tmp = readme[1].split("releases/tag/", 1)
            tmp = tmp[1].split("\n", 1)
            tmp = tmp[1]
            download = "[![Download from https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases](https://img.shields.io/badge/Download-v" + self.oc_ver +  ".0-blue)](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases/tag/" +  "v" + self.oc_ver + ".0)"
            readme = readme[0] + "## 下载\n" + download + "\n" + tmp
        readme = readme.split("## 更新日志")
        tmp = readme[1].split("更多版本的更新日志")
        tmp = "更多版本的更新日志" + tmp[1]
        readme = readme[0] + "## 更新日志: " + new + "\n\n" + tmp

        readme = readme.split("<summary><strong>驱动版本</strong></summary>")
        tmp = readme[1].split("## 工作状态")
        tmp = "\n</details>\n\n## 工作状态" + tmp[1]
        readme = readme[0] + \
            "<summary><strong>驱动版本</strong></summary>\n</br>\n\n" + self.kext + tmp

        self.readme_zh = readme
    
    
    def download_database(self):
        r = requests.get(self.url, verify = False)
        path = os.path.abspath(os.path.join(self.root, "database.json"))
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
        

    def get_remote_data(self):
        remote = {}
        kexts_list = []
        readme = os.path.abspath(os.path.join(self.root, '../README.md'))
        with open(readme, 'r') as file:
            readme = file.read()
            file.close()
        readme = readme.split("OpenCore  ")
        pre_ver = readme[1].split('\n', 1)
        pre_ver = pre_ver[0].split('/')
        pre_ver = pre_ver[-1].strip()
        self.oc_ver0 = pre_ver
        pre_ver = pre_ver.split('.')
        ver = pre_ver.copy()
        if pre_ver[-1] == '9':
            ver[-1] = '0'
            ver[-2] = str(int(pre_ver[-2]) + 1)
        else:
            ver[-1] = str(int(ver[-1]) + 1)
        if ver[-2] == '10':
            ver[-2] = '0'
            ver[-3] = str(int(pre_ver[-3]) + 1)
        oc_ver = ''
        for ver0 in ver:
            oc_ver = oc_ver + ver0 + '.'
        oc_ver = oc_ver.strip('.')
        self.oc_ver = oc_ver

        path = os.path.abspath(os.path.join(self.root, "database.json"))
        with open(path, 'r') as f:
            row_data = json.load(f)
            f.close()
        for key in row_data.keys():
            try:
                if row_data[key]['type'].lower() == "bootloader":
                    self.bootloader = key
                if row_data[key]['type'].lower() == "kext":
                    kexts_list.append(key)
            except:
                continue
        self.kexts_list = kexts_list
        kexts_list.append(self.bootloader)

        for i in kexts_list:
            k = 0
            info = row_data[i]
            info_all = info['versions']
            info = info_all[k]
            if i == self.bootloader:
                oc_ver = info['version']
                while oc_ver != self.oc_ver and oc_ver != self.oc_ver0:
                    info = info_all[k]
                    oc_ver = info['version']
                    k += 1
                if k > 0:
                    self.mode = 1

            # download link
            link = info['links']

            remote[i] = {'link': link['release']}
        self.remote = remote


    def get_local_data(self):
        local = {}

        # kexts
        path = os.path.abspath(os.path.join(self.root, '../EFI/OC/Kexts'))
        for kext in os.listdir(path):
            kext0 = kext.split('.')
            kext0 = kext0[0]

            # IntelBluetoothFirmware
            if kext0[0:14].lower() == 'intelbluetooth' or kext0.lower() == 'intelbtpatcher':
                try:
                    local['IntelBluetoothFirmware']['kexts'].append(kext)
                except:
                    self.install += 1
                    local['IntelBluetoothFirmware'] = {'kexts': [kext]}
                continue

            # BrcmPatchRAM
            if kext0[0:4].lower() == 'brcm' or kext0.lower() == 'bluetoolfixup':
                try:
                    local['BrcmPatchRAM']['kexts'].append(kext)
                except:
                    self.install += 1
                    local['BrcmPatchRAM'] = {'kexts': [kext]}
                continue

            # VirtualSMC
            if kext0[0:3].upper() == 'SMC' or kext0.upper() == 'VIRTUALSMC':
                try:
                    local['VirtualSMC']['kexts'].append(kext)
                except:
                    self.install += 1
                    local['VirtualSMC'] = {'kexts': [kext]}
                continue

            # VoodooPS2
            if kext0 == "VoodooPS2Controller":
                self.install += 1
                local['VoodooPS2'] = {'kexts': [kext]}
                continue

            # other not in kexts_list: skip
            if kext0 not in self.kexts_list:
                continue

            # in kexts_list: save time and kext name
            local[kext0] = {'kexts': [kext]}
            self.install += 1
        self.local = local


    def update_oc_config(self, update_config, source_config, save_config):
        del_keys = []
        del_platform_info = []
        update_info = []

        # read update plist
        with open(update_config, 'rb') as pl:
            custom_plist = load(pl)
            up_plist = copy.deepcopy(custom_plist)
        # read source plist
        with open(source_config, 'rb') as pl:
            source_plist = load(pl)
            src_plist = copy.deepcopy(source_plist)

        # clean warning section
        for key in up_plist.keys():
            if key[0] == '#':
                del_keys.append(key)
                continue
        for del_key in del_keys:
            up_plist.pop(del_key)

        for key in up_plist.keys():
            # deviceproperties
            if key.lower() == "deviceproperties":
                up_plist[key] = src_plist[key]
                continue
            for key2 in up_plist[key].keys():
                # platforminfo
                if key.lower() == "platforminfo":
                    if key2 in src_plist[key].keys():
                        up_plist[key][key2] = src_plist[key][key2]
                        continue
                    del_platform_info.append(key2)
                    continue
                # nvram
                if key.lower() == "nvram":
                    if key2 in src_plist[key].keys():
                        up_plist[key][key2] = src_plist[key][key2]
                        continue
                # others entry
                # list copy directly
                if isinstance(up_plist[key][key2], list):
                    try:
                        # if list contains dict, check if some keys are missing
                        if isinstance(up_plist[key][key2][0], dict):
                            add = []
                            example = up_plist[key][key2][0]
                            up_plist[key][key2] = src_plist[key][key2]
                            for entry in up_plist[key][key2]:
                                for key3 in example.keys():
                                    if key3.lower() == "loadearly":
                                        entry[key3] = False
                                    if key3 not in entry.keys():
                                        add.append(key3)
                                        entry[key3] = example[key3]
                            add = list(set(add))
                            if len(add) > 0:
                                for key3 in add:
                                    info = "[Config: Add Entry] " + \
                                        str(key) + "->" + str(key2) + \
                                        "->" + str(key3) + ":  "
                                    info = info + str(example[key3])
                                    update_info.append(info)
                            continue
                        up_plist[key][key2] = src_plist[key][key2]
                    except IndexError:
                        up_plist[key][key2] = src_plist[key][key2]
                # dict copy
                if isinstance(up_plist[key][key2], dict):
                    keys = src_plist[key][key2].keys()
                    keys_up = up_plist[key][key2].keys()
                    # check delete entry
                    for key3 in keys:
                        if key3 not in keys_up:
                            info = "[Delete Entry] " + \
                                str(key) + "->" + str(key2) + \
                                "->" + str(key3) + ":  "
                            info = info + str(src_plist[key][key2][key3])
                            update_info.append(info)
                    for key3 in keys_up:
                        # if add entry, keep the default key-value
                        if key3 not in keys:
                            info = "[Add Entry] " + \
                                str(key) + "->" + str(key2) + \
                                "->" + str(key3) + ":  "
                            info = info + str(up_plist[key][key2][key3])
                            update_info.append(info)
                            continue
                        # if change entry type, keep the default key-value
                        if type(up_plist[key][key2][key3]) != type(src_plist[key][key2][key3]):
                            info = "[Change Entry] " + \
                                str(key) + "->" + str(key2) + \
                                "->" + str(key3) + ":  "
                            info = info + \
                                str(src_plist[key][key2][key3]) + \
                                " -> " + str(up_plist[key][key2][key3])
                            update_info.append(info)
                            continue
                        up_plist[key][key2][key3] = src_plist[key][key2][key3]
                    continue
                # other type
                # if change entry type, keep the default key-value
                if type(up_plist[key][key2]) != type(src_plist[key][key2]):
                    info = "[Change Entry] " + \
                        str(key) + "->" + str(key2) + ":  "
                    info = info + \
                        str(src_plist[key][key2]) + \
                        " -> " + str(up_plist[key][key2])
                    update_info.append(info)
                    continue
                up_plist[key][key2] = src_plist[key][key2]

        # delete no need platform information
        for platform_info in del_platform_info:
            up_plist["PlatformInfo"].pop(platform_info)

        # save new config
        with open(save_config, 'wb') as new_plist:
            dump(up_plist, new_plist, fmt=FMT_XML,sort_keys=True, skipkeys=False)

        # display config update info
        for info in update_info:
            info_header = self.Colors("[Config Update] ", fcolor="cyan")
            info = info_header + info
            print(info)
        
        # save info for release txt
        self.config_info = update_info

        

    def update_oc_interface(self, kext, progress):
        os.system('clear')
        self.title()
        print(self.Colors("- Update OpenCorePkg Done", fcolor='green'))
        print("> Update Kexts Package")
        print("")
        progress1 = progress[0]
        progress2 = progress[1]
        ratio = float(progress1*4 + progress2 - 4)/self.install/4
        sym_nums = 60
        sym_progress = int(sym_nums*ratio)
        space = sym_nums - sym_progress
        print("[" + str(progress1) +"/" + str(self.install) + "]  " + str(round(ratio*100,2)) + " %  [" + "="*sym_progress + " "*space + "]")
        print("")
        print("Updating Kext Package: " + self.Colors(kext, fcolor='yellow') + "\n" + "These kext(s) will be update: ")
        for k in self.local[kext]['kexts']:
            print(self.Colors("\t" + k, fcolor='yellow'))
        print("")
        if progress2 >= 0:
            print(self.Colors("[Info] Downloading Kext Package: " + kext, fcolor='green'))
        if progress2 >= 1:
            print(self.Colors("[Info] Download Kext Package: " + kext + " Done", fcolor='green'))
            print(self.Colors("[Info] Extracting Kext Package: " + kext, fcolor='green'))
        if progress2 >= 2:
            print(self.Colors("[Info] Extract Kext Package: " + kext + " Done", fcolor='green'))
            print(self.Colors("[Info] Updating Kext Package: " + kext, fcolor='green'))
        if progress2 >= 3:
            print(self.Colors("[Info] Update Kext Package: " + kext + " Done", fcolor='green'))
            print(self.Colors("[Info] Cleaning Cache: " + kext, fcolor='green'))
        if progress2 >= 4:
            print(self.Colors("[Info] Clean Cache: " + kext + " Done", fcolor='green'))

    
    def update_OpenCore(self):
        self.get_remote_data()
        self.get_local_data()
        oc = self.remote[self.bootloader]
        root = os.path.abspath(os.path.join(self.root, ".."))
        tmp_path = os.path.abspath(os.path.join(self.root, 'cache/'))
        if not os.path.exists(tmp_path):
            os.mkdir(tmp_path)
        tmp = os.path.abspath(os.path.join(tmp_path, 'OpenCorePkg.zip'))

        # download
        print(self.Colors("[Info] Downloading OpenCorePkg...", fcolor='green'))
        headers = {"Auth": "{abcd}", "accept": "*/*",
                   "accept-encoding": "gzip;deflate;br"}
        response = requests.request("GET", oc['link'], headers=headers, verify=False)
        with open(tmp, "wb") as f:
            f.write(response.content)
        print(self.Colors("[Info] Download Done", fcolor='green'))

        # extract zip
        print(self.Colors("[Info] Extract OpenCorePkg...", fcolor='green'))
        tmp_path = os.path.abspath(os.path.join(tmp_path, 'OpenCorePkg/'))
        ys = zipfile.ZipFile(tmp)
        ys.extractall(tmp_path)
        ys.close()
        os.remove(tmp)
        print(self.Colors("[Info] Extract Done", fcolor='green'))

        # OpenCore.efi update
        print(self.Colors(
            "[Info] Updating OpenCorePkg Core...", fcolor='green'))
        oc_efi_source = os.path.abspath(os.path.join(root, 'EFI/OC/OpenCore.efi'))
        oc_efi_update = os.path.abspath(os.path.join(tmp_path, 'X64/EFI/OC/OpenCore.efi'))
        shutil.copy(oc_efi_update, oc_efi_source)
        print(self.Colors("[Info] Update Core Done", fcolor='green'))

        # Drivers update
        print(self.Colors(
            "[Info] Updating OpenCorePkg Drivers...", fcolor='green'))
        drivers = []
        oc_drivers_source = os.path.abspath(os.path.join(root, 'EFI/OC/Drivers/'))
        oc_drivers_update = os.path.abspath(os.path.join(tmp_path, 'X64/EFI/OC/Drivers/'))
        for driver in os.listdir(oc_drivers_update):
            drivers.append(driver)
        for driver in os.listdir(oc_drivers_source):
            if driver[0] == '.':
                continue
            if driver not in drivers:
                print(self.Colors("[Warning] Driver " + driver +
                      " is not in Official Drivers folders, update skipped", fcolor='yellow'))
                continue
            source_driver = os.path.abspath(os.path.join(oc_drivers_source, driver))
            update_driver = os.path.abspath(os.path.join(oc_drivers_update, driver))
            shutil.copy(update_driver, source_driver)
        print(self.Colors("[Info] Update Drivers Done", fcolor='green'))

        # Tools update
        print(self.Colors(
            "[Info] Updating OpenCorePkg Tools...", fcolor='green'))
        tools = []
        oc_tools_source = os.path.abspath(os.path.join(root, 'EFI/OC/Tools/'))
        oc_tools_update = os.path.abspath(os.path.join(tmp_path, 'X64/EFI/OC/Tools/'))
        for tool in os.listdir(oc_tools_update):
            tools.append(tool)
        for tool in os.listdir(oc_tools_source):
            if tool[0] == '.':
                continue
            if tool not in tools:
                print(self.Colors("[Warning] Tool " + tool +
                      " is not in Official Tools folders, update skipped", fcolor='yellow'))
                continue
            source_tool = os.path.abspath(os.path.join(oc_tools_source, tool))
            update_tool = os.path.abspath(os.path.join(oc_tools_update, tool))
            shutil.copy(update_tool, source_tool)
        print(self.Colors("[Info] Update Tools Done", fcolor='green'))

        # check plist
        ocvalidate_path = os.path.abspath(os.path.join(tmp_path, 'Utilities/ocvalidate/ocvalidate'))
        os.system('chmod +x ' + ocvalidate_path)
        for file in os.listdir(os.path.abspath(os.path.join(root, 'EFI/OC/'))):
            if file.split(".")[-1] == "plist":
                print(self.Colors("[Info] Found config file: " + file, fcolor='green'))
                print(self.Colors("[Info] Checking config file: " + file, fcolor='green'))
                plist_path = os.path.abspath(os.path.join(root, 'EFI/OC/'+ file))
                ocvalidate_path_sys = ocvalidate_path.replace(' ', '\ ')
                plist_path_sys = plist_path.replace(' ', '\ ')
                v = os.popen(ocvalidate_path_sys + ' ' + plist_path_sys).read()
                if "No issues found" in v:
                    print(self.Colors("[Info] **** " + file + " check Done, No issues Found! ****", fcolor='green'))
                else:
                    update_config = os.path.abspath(os.path.join(sys.path[0], "cache/OpenCorePkg/Docs/SampleCustom.plist"))
                    source_config = plist_path
                    save_config = os.path.abspath(os.path.join(sys.path[0], "cache/OpenCorePkg/config.plist"))
                    self.update_oc_config(update_config, source_config, save_config)
                    shutil.copy(save_config, source_config)
                    v2 = os.popen(ocvalidate_path_sys + ' ' +
                                save_config.replace(' ', '\ ')).read()
                    if "No issues found" in v2:
                        print(self.Colors(
                            "[Info] **** " + file + " update automatically and check Done, No issues Found! ****", fcolor='green'))
                        print(self.Colors(
                            "[Warning] **** Automatically plist update is not reliable all the time, please check and save your backup EFI in backup_EFI folder ****", fcolor='yellow'))
                    else:
                        v = v2.split(self.oc_ver + '!')
                        v = v[1].strip()
                        v = v.split('Completed validating')
                        v1 = v[0].strip()
                        v1 = v1.replace('\n', '\n\t')
                        v1 = '\t' + v1
                        v2 = v[1].split('. Found ')
                        v2 = 'Found ' + v2[1]
                        v2 = v2.replace('.', ':')
                        print(self.Colors(
                            "[Error] " + file + " update automatically and check Done, Errors still occur: " + v2 + ' ', fcolor='red'))
                        print(self.Colors(v1, fcolor='yellow'))
                        print(self.Colors(
                            "[Warning] Please read instruction from the official website to update your " + file + " or recover EFI from backup.", fcolor='yellow'))

        # clean cache
        print(self.Colors("[Info] Cleaning cache...", fcolor='green'))
        shutil.rmtree(tmp_path)
        print(self.Colors("[Info] Clean Done", fcolor='green'))

        input("Press [Enter] to continue...")

        # update kexts
        update_kexts = []
        tmp_path = os.path.abspath(os.path.join(self.root, 'cache/'))
        if not os.path.exists(tmp_path):
            os.mkdir(tmp_path)
        tmp_path = os.path.abspath(os.path.join(tmp_path, 'Kexts/'))
        if not os.path.exists(tmp_path):
            os.mkdir(tmp_path)
        progress = [0, 0]
        err = []
        for kext in self.local.keys():
            if kext == self.bootloader:
                continue
            progress[0] = progress[0] + 1
            progress[1] = 0
            self.update_oc_interface(kext, progress)

            try:
                tmp = os.path.abspath(os.path.join(tmp_path, kext + '.zip'))
                headers = {"Auth": "{abcd}", "accept": "*/*",
                           "accept-encoding": "gzip;deflate;br"}
                response = requests.request("GET", self.remote[kext]['link'], headers=headers, verify=False)
                with open(tmp, "wb") as f:
                    f.write(response.content)
                progress[1] = progress[1] + 1
            except:
                err.append(kext)
                continue
            self.update_oc_interface(kext, progress)

            try:
                tmp_path0 = os.path.abspath(os.path.join(tmp_path,  kext + '/'))
                ys = zipfile.ZipFile(tmp)
                ys.extractall(tmp_path0)
                ys.close()
                os.remove(tmp)
                progress[1] = progress[1] + 1
            except:
                err.append(kext)
                continue
            self.update_oc_interface(kext, progress)

            try:
                for k in self.local[kext]['kexts']:
                    source = os.path.abspath(os.path.join(root, 'EFI/OC/Kexts/'))
                    update = os.path.abspath(os.path.join(tmp_path0, k))
                    source_plist = os.path.join(source, k + "/Contents/Info.plist")
                    source_sha = hashlib.md5(open(source_plist, 'r').read().encode('utf8')).hexdigest()
                    if kext.upper() == "VIRTUALSMC":
                        update = os.path.abspath(os.path.join(tmp_path0, "Kexts/" + k))
                    update_plist = os.path.join(update, "Contents/Info.plist")
                    update_sha = hashlib.md5(open(update_plist, 'r').read().encode('utf8')).hexdigest()
                    update = update.replace(' ', '\ ')
                    if source_sha != update_sha:
                        update_kexts.append(kext)
                    source = source.replace(' ', '\ ')
                    os.system('cp -rf ' + update + ' ' + source)
                   
                progress[1] = progress[1] + 1
            except :
                err.append(kext)
                continue

            try:
                shutil.rmtree(tmp_path0)
                progress[1] = progress[1] + 1
            except:
                err.append(kext)
                continue
            self.update_oc_interface(kext, progress)

        os.system('clear')
        self.title()
        first_time = 0
        if len(update_kexts) + len(err) == 0:
            print(self.Colors("All Kexts are up-to-date", fcolor='green'))
            print("")
            print(self.Colors("Writing Update Information...", fcolor="green"))
            self.write_info()
            print(self.Colors("Write Done", fcolor="green"))
            print("")
            input("Press [Enter] to continue...")
            return
        
        # save info for release txt
        update_every_kexts = []
        update_kexts_success = update_kexts
        for i in update_kexts:
            if i not in err:
                if first_time == 0:
                    if len(err) > 0:
                        print(self.Colors(
                            "These Kext Package(s) Update Successfully:", fcolor='magenta'))
                    else:
                        print(self.Colors(
                            "All Kext Packages Update Successfully:", fcolor='magenta'))
                    first_time = 1
                if len(i) < 11:
                    print(self.Colors("   " + i, fcolor='blue'))
                else:
                    print(self.Colors("   " + i, fcolor='blue'))
        print("")
        if len(err) > 0:
            first_time = 0
            for i in err:
                if first_time == 0:
                    print(self.Colors(
                        "These Kext Package(s) Update Unsuccessfully:", fcolor='red'))
                    first_time = 1
                if len(i) < 11:
                    print(self.Colors("   " + i, fcolor='yellow'))
                else:
                    print(self.Colors("   " + i, fcolor='yellow'))
            print("")
        # save kext data
        for kext in update_kexts_success:
            for k in self.local[kext]['kexts']:
                k = k.split(".")
                k = k[0].strip()
                update_every_kexts.append(k)
        self.update_kext_info = update_every_kexts
        print(self.Colors("Writing Update Information...", fcolor="green"))
        self.write_info()
        print(self.Colors("Write Done", fcolor="green"))
        print("")
        input("Press [Enter] to continue...")
    
    
    def write_info(self):
        # mkdir info folders
        info_path = os.path.abspath(os.path.join(self.root, "info"))
        kext_info_path = os.path.join(info_path, "kext")
        config_info_path = os.path.join(info_path, "config")
        if not os.path.exists(info_path):
            os.mkdir(info_path)
        if not os.path.exists(kext_info_path):
            os.mkdir(kext_info_path)
        if not os.path.exists(config_info_path):
            os.mkdir(config_info_path)
        
        # generate filename & read data
        header = self.oc_ver0
        header = header.replace('.', '-')
        header_len = len(header)
        filename = header + '.txt'
        kext_data_origin = []
        config_data_origin = []
        for root, dirs, files in os.walk(kext_info_path):
            for file in files:
                if file[0:header_len] == header:
                    source_file = os.path.join(root, filename)
                    with open(source_file, 'r') as f:
                        kext_data_origin = f.readlines()
                        f.close()

        for root, dirs, files in os.walk(config_info_path):
            for file in files:
                if file[0:header_len] == header:
                    source_file = os.path.join(root, filename)
                    with open(source_file, 'r') as f:
                        config_data_origin = f.readlines()
                        f.close()
                
        kext_filename = os.path.join(kext_info_path, filename)
        config_filename = os.path.join(config_info_path, filename)

        # save info
        kext_data = []
        config_data = []
        for item in kext_data_origin:
            item = item.strip()
            if item == '' or item == '\n':
                continue
            kext_data.append(item)
        for item in config_data_origin:
            item = item.strip()
            if item == '' or item == '\n':
                continue
            config_data.append(item)
        kext_data = kext_data + self.update_kext_info
        config_data = config_data + self.config_info
        kext_data = list(set(kext_data))
        kext_data.sort()

        # save info
        with open(kext_filename, 'w') as f:
            for item in kext_data:
                f.write(item + "\n")
            f.close()
        with open(config_filename, 'w') as f:
            for item in config_data:
                f.write(item + "\n")
            f.close()
        if len(config_data) > 0:
            update_config = "```\n"
            for item in config_data:
                update_config = update_config + item + "\n"
            update_config = update_config + '```'
            self.update_config = update_config


    def write_files(self):
        files = {}
        files['Changelog.md'] = self.changelog
        files['Changelog_zh.md'] = self.changelog_zh
        files['README.md'] = self.readme
        files['README_zh.md'] = self.readme_zh
        root = os.path.abspath(os.path.join(self.root, '..'))
        backup_path = os.path.abspath(os.path.join(root, 'backup'))
        if not os.path.exists(backup_path):
            os.mkdir(backup_path)
        for file in files.keys():
            if file.split(".")[-1] == "md":
                full_path = os.path.abspath(os.path.join(root, file))
                shutil.copy(full_path, backup_path)
                with open(full_path, 'w') as f:
                    f.write(files[file])
                    f.close()
        release_info_path = os.path.abspath(os.path.join(self.root, 'Release_info.txt'))
        with open(release_info_path, 'w') as f:
            f.write(self.release_info)
            f.close()
        

    def compress_EFI(self):
        root = os.path.abspath(os.path.join(self.root, ".."))
        dist = os.path.abspath(os.path.join(root, "EFI.zip"))
        zip = zipfile.ZipFile(dist, "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(os.path.join(root, 'EFI')):
            fpath = path.replace(root, '')
            for filename in filenames:
                source_file = os.path.join(fpath, filename)
                zip.write(os.path.join(path, filename), source_file)


    def git_push(self):
        repo_path = os.path.abspath(os.path.join(self.root, '..'))
        commit_message = "Daily Update"
        os.system("cd " + repo_path + " && git add ." + " && git commit -m '" + commit_message + "' ")
        os.system("cd " + repo_path + " && git push")
        print("")
        input("Press [Enter] to continue...")


    def git_release(self):
        repo_path = os.path.abspath(os.path.join(self.root, '..'))
        tag = "v" + self.oc_ver + ".0"
        release_message = "OC " + self.oc_ver
        commit_message = "Update to " + release_message
        os.system("cd " + repo_path + " && git add ." + " && git commit -m '" + commit_message + "' ")
        os.system("cd " + repo_path + " && git push")
        os.system("cd " + repo_path + " && git tag -a " + tag + " -m '" + release_message + "'")
        os.system("cd " + repo_path + " && git push origin " + tag)
        input("Press [Enter] to continue...")
            

    def main(self):
        progress = 0
        self.main_interface(progress)
        try:
            self.download_database()
        except:
            print(self.Colors("NetWork Error !", fcolor="red"))
            exit()
        progress += 1
        self.main_interface(progress)
        self.update_OpenCore()
        progress += 1
        self.main_interface(progress)
        if self.mode == 1:
            self.generate_changelog_readme()
            progress += 1
            self.main_interface(progress)
            self.write_files()
            progress += 1
            self.main_interface(progress)
            self.compress_EFI()
            progress += 1
            self.main_interface(progress)
            self.git_release()
        else:
            progress += 1
            self.main_interface(progress)
            push = input(self.Colors("Comfirm to Push (1 to confirm else cancel): ", fcolor="yellow"))
            if str(push) == "1":
                self.git_push()
        progress += 1
        self.main_interface(progress)
        

if __name__ == "__main__":
    uprepo = UpdateRepo()

    # run script
    uprepo.main()
