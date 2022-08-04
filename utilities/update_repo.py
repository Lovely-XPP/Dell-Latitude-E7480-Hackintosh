import json
import os
import sys
import shutil, copy
import zipfile
import time
import platform
import requests
from plistlib import *


class UpdateRepo:
    def __init__(self) -> None:
        self.root = os.path.abspath(sys.path[0])
        self.kext = ""
        self.update_kext = ""
        self.kext_zh = ""
        self.update_kext_zh = ""
        self.changelog = ""
        self.changelog_zh = ""
        self.readme = ""
        self.readme_zh = ""
        self.oc_ver = ""
        self.url = 'https://raw.githubusercontent.com/dortania/build-repo/builds/config.json'
        self.bootloader = ""
        self.kexts_list = []
        self.remote = {}
        self.local = {}
        self.install = 0

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
        if progress >= 0:
            print("> Download Database")
            return
        if progress >= 1:
            print(self.Colors("- Download Database", fcolor='green'))
            print("> Update OpenCorePkg and Main Kexts")
            return
        if progress >= 2:
            print(self.Colors("- Download Database", fcolor='green'))
            print(self.Colors("- Update OpenCorePkg and Main Kexts", fcolor='green'))
            print("> Update Release Info")
            return
        print(self.Colors("- Download Database", fcolor='green'))
        print(self.Colors("- Update OpenCorePkg and Main Kexts", fcolor='green'))
        print(self.Colors("- Update Release Info", fcolor='green'))
        print(self.Colors("- All Done", fcolor='green'))


    def update_kexts(self) -> None:
        root = self.root
        kext_name = []
        kext_version = []
        kext_time = []
        kext_type = []
        kext_type_zh = []
        first_time = 0
        multiple = 0
        for kext in os.listdir(os.path.join(root, 'update_kexts')):
            if kext == ".DS_Store":
                continue
            if kext[:len("AirportItlwm")] == "AirportItlwm":
                if first_time == 1:
                    multiple = multiple + 1
                    continue
                first_time = 1
            domain = os.path.abspath(os.path.join(self.root, 'update_kexts'))
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
            self.oc_ver + "\n2. Update kexts with official Release:\n\n" + \
            self.update_kext
        self.changelog = changelog[0] + "更新日志\n\n##" + new + "\n\n-----------------------------------------------------" + changelog[1]

        readme = os.path.abspath(os.path.join(root, 'README.md'))
        with open(readme, 'r') as file:
            readme = file.read()
            file.close()
        readme = readme.split("OpenCore  ")
        pre_ver = readme[1].split('\n', 1)
        readme = readme[0] + "OpenCore  " + pre_ver[0] + " / " + self.oc_ver + "\n" + pre_ver[1]
        readme = readme.split("## ChangeLog")
        tmp = readme[1].split("For more information")
        tmp = "For more infomation" + tmp[1]
        readme = readme[0] + "## ChangeLog: " + new + "\n\n" + tmp
        readme = readme.split("## Download")
        tmp = readme[1].split("EFI.zip)", 1)
        tmp = tmp[1]
        download = "[![Download from https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases](https://img.shields.io/badge/Download-v" + self.oc_ver + ".0-blue)](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases/download/" + "V" + self.oc_ver + ".0/EFI.zip)"
        self.readme = readme[0] + "## Download\n" + download + "\n" + tmp

        changelog = os.path.abspath(os.path.join(root, 'Changelog_zh.md'))
        with open(changelog, 'r') as file:
            changelog = file.read()
            file.close()
        changelog = changelog.split('更新日志')
        new = "V" + self.oc_ver + ".0\n\n### 发布时间 : " + now + \
            "\n\n#### 添加功能 :\n\n1. 更新OC版本至" + self.oc_ver + "并更新了驱动" + \
            "\n\n#### 文件变化 :\n\n1. 更新整个EFI文件夹以适配 OC " + \
            self.oc_ver + "\n2. 更新驱动:\n\n" + \
            self.update_kext
        self.changelog_zh = changelog[0] + "更新日志\n\n##" + new + "\n\n-----------------------------------------------------" + changelog[1]
        readme = os.path.abspath(os.path.join(root, 'README_zh.md'))

        with open(readme, 'r') as file:
            readme = file.read()
            file.close()
        readme = readme.split("OpenCore  ")
        pre_ver = readme[1].split('\n', 1)
        readme = readme[0] + "OpenCore  " + pre_ver[0] + " / " + self.oc_ver + "\n" + pre_ver[1]
        readme = readme.split("## 更新日志")
        tmp = readme[1].split("更多版本的更新日志")
        tmp = "更多版本的更新日志" + tmp[1]
        readme = readme[0] + "## 更新日志: " + new + "\n\n" + tmp
        readme = readme.split("## 下载")
        tmp = readme[1].split("EFI.zip)", 1)
        tmp = tmp[1]
        download = "[![Download from https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases](https://img.shields.io/badge/Download-v" + self.oc_ver + ".0-blue)](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases/download/" + "V" + self.oc_ver + ".0/EFI.zip)"
        self.readme_zh = readme[0] + "## Download\n" + download + "\n" + tmp
    
    
    def download_database(self):
        r = requests.get(self.url)
        path = os.path.abspath(os.path.join(self.root, "database.json"))
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
        

    def get_remote_data(self):
        remote = {}
        kexts_list = []
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

        for i in kexts_list:
            info = row_data[i]

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
            if kext0[0:14] == 'IntelBluetooth' or kext0 == 'IntelBTPatcher':
                try:
                    local['IntelBluetoothFirmware']['kexts'].append(kext)
                except:
                    self.install += 1
                    local['IntelBluetoothFirmware'] = {'kexts': [kext]}
                continue

            # BrcmPatchRAM
            if kext0[0:4] == 'Brcm' or kext0 == 'BlueToolFixup':
                try:
                    local['BrcmPatchRAM']['kexts'].append(kext)
                except:
                    self.install += 1
                    local['BrcmPatchRAM'] = {'kexts': [kext]}
                continue

            # VirtualSMC
            if kext0[0:3] == 'SMC' or kext0[-3:-1] == 'SMC':
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
            for key2 in up_plist[key].keys():
                if key2 == "Add" or key2 == "Delete" or key2 == "Patch":
                    up_plist[key][key2] = src_plist[key][key2]
                    continue
                try:
                    if key == "PlatformInfo":
                        if key2 in src_plist[key].keys():
                            up_plist[key][key2] = src_plist[key][key2]
                            continue
                        del_platform_info.append(key2)
                        continue
                    for key3 in up_plist[key][key2].keys():
                        try:
                            up_plist[key][key2][key3] = src_plist[key][key2][key3]
                        except:
                            continue
                except:
                    try:
                        up_plist[key][key2] = src_plist[key][key2]
                    except:
                        continue

        # delete no need platform information
        for platform_info in del_platform_info:
            up_plist["PlatformInfo"].pop(platform_info)

        # save new config
        with open(save_config, 'wb') as new_plist:
            dump(up_plist, new_plist, fmt=FMT_XML,
                 sort_keys=True, skipkeys=False)


    def update_oc_interface(self, kext, progress):
        os.system('clear')
        self.title()
        print(self.Colors("- Update OpenCorePkg Done", fcolor='green'))
        print("> Update Kexts Package")
        print("")
        progress1 = progress[0] + 1
        progress2 = progress[1]
        ratio = float(progress1*4 + progress2 - 4)/self.install/4
        sym_nums = 60
        sym_progress = int(sym_nums*ratio)
        space = sym_nums - sym_progress
        print("[" + str(progress1-1) +"/" + str(self.install) + "]  " + str(round(ratio*100,2)) + " %  [" + "="*sym_progress + " "*space + "]")
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
        root = os.path.abspath(os.path.join(root, ".."))
        tmp_path = os.path.abspath(os.path.join(self.root, 'cache/'))
        if not os.path.exists(tmp_path):
            os.mkdir(tmp_path)
        tmp = os.path.abspath(os.path.join(tmp_path, 'OpenCorePkg.zip'))

        # download
        print(self.Colors("[Info] Downloading OpenCorePkg...", fcolor='green'))
        headers = {"Auth": "{abcd}", "accept": "*/*",
                   "accept-encoding": "gzip;deflate;br"}
        response = requests.request("GET", oc['link'], headers=headers)
        with open(tmp, "wb") as f:
            f.write(response.content)
        print("")
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
        oc_efi_source = os.path.abspath(
            os.path.join(root, 'EFI/OC/OpenCore.efi'))
        oc_efi_update = os.path.abspath(
            os.path.join(tmp_path, 'X64/EFI/OC/OpenCore.efi'))
        shutil.copy(oc_efi_update, oc_efi_source)
        print(self.Colors("[Info] Update Core Done", fcolor='green'))

        # Drivers update
        print(self.Colors(
            "[Info] Updating OpenCorePkg Drivers...", fcolor='green'))
        drivers = []
        oc_drivers_source = os.path.abspath(
            os.path.join(root, 'EFI/OC/Drivers/'))
        oc_drivers_update = os.path.abspath(
            os.path.join(tmp_path, 'X64/EFI/OC/Drivers/'))
        for driver in os.listdir(oc_drivers_update):
            drivers.append(driver)
        for driver in os.listdir(oc_drivers_source):
            if driver[0] == '.':
                continue
            if driver not in drivers:
                print(self.Colors("[Warning] Driver " + driver +
                      " is not in Official Drivers folders, update skipped", fcolor='yellow'))
                continue
        print(self.Colors("[Info] Update Drivers Done", fcolor='green'))

        # Tools update
        print(self.Colors(
            "[Info] Updating OpenCorePkg Tools...", fcolor='green'))
        tools = []
        oc_tools_source = os.path.abspath(
            os.path.join(root, 'EFI/OC/Tools/'))
        oc_tools_update = os.path.abspath(
            os.path.join(tmp_path, 'X64/EFI/OC/Tools/'))
        for driver in os.listdir(oc_tools_update):
            tools.append(driver)
        for driver in os.listdir(oc_tools_source):
            if driver[0] == '.':
                continue
            if driver not in tools:
                print(self.Colors("[Warning] Tool " + driver +
                      " is not in Official Tools folders, update skipped", fcolor='yellow'))
                continue
        print(self.Colors("[Info] Update Tools Done", fcolor='green'))

        # check plist
        ocvalidate_path = os.path.abspath(os.path.join(
            tmp_path, 'Utilities/ocvalidate/ocvalidate'))
        plist_path = os.path.abspath(
            os.path.join(root, 'EFI/OC/Config.plist'))
        if not os.path.exists(plist_path):
            plist_path = os.path.abspath(
                os.path.join(root, 'EFI/OC/config.plist'))
        if not os.path.exists(plist_path):
            print(self.Colors(
                "[Warning] config plist not found, check skipped", fcolor='yellow'))
        else:
            os.popen('chmod +x ' + ocvalidate_path)
            ocvalidate_path_sys = ocvalidate_path.replace(' ', '\ ')
            plist_path_sys = plist_path.replace(' ', '\ ')
            v = os.popen(ocvalidate_path_sys + ' ' + plist_path_sys).read()
            if "No issues found" in v:
                print(self.Colors(
                    "[Info] **** Config plist check Done, No issues Found! ****", fcolor='green'))
            else:
                update_config = os.path.abspath(os.path.join(
                    sys.path[0], "cache/OpenCorePkg/Docs/SampleCustom.plist"))
                source_config = plist_path
                save_config = os.path.abspath(os.path.join(
                    sys.path[0], "cache/OpenCorePkg/Config.plist"))
                self.update_oc_config(
                    update_config, source_config, save_config)
                shutil.copy(save_config, source_config)
                v2 = os.popen(ocvalidate_path_sys + ' ' +
                              save_config.replace(' ', '\ ')).read()
                if "No issues found" in v2:
                    print(self.Colors(
                        "[Info] **** Config update automatically and check Done, No issues Found! ****", fcolor='green'))
                    print(self.Colors(
                        "[Warning] **** Automatically plist update is not reliable all the time, please check and save your backup EFI in backup_EFI folder ****", fcolor='yellow'))
                else:
                    v = v2.split(self.remote[self.bootloader]['version'] + '!')
                    v = v[1].strip()
                    v = v.split('Completed validating')
                    v1 = v[0].strip()
                    v1 = v1.replace('\n', '\n\t')
                    v1 = '\t' + v1
                    v2 = v[1].split('. Found ')
                    v2 = 'Found ' + v2[1]
                    v2 = v2.replace('.', ':')
                    print(self.Colors(
                        "[Error] Config plist update automatically and check Done, Errors still occur: " + v2 + ' ', fcolor='red'))
                    print(self.Colors(v1, fcolor='yellow'))
                    print(self.Colors(
                        "[Warning] Please read instruction from the official website to update your config.plist or recover EFI from backup.", fcolor='yellow'))

        # clean cache
        print(self.Colors("[Info] Cleaning cache...", fcolor='green'))
        shutil.rmtree(tmp_path)
        print(self.Colors("[Info] Clean Done", fcolor='green'))

        input("Press [Enter] to continue...")

        # update kexts
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
                response = requests.request(
                    "GET", self.remote[kext]['link'], headers=headers)
                with open(tmp, "wb") as f:
                    f.write(response.content)
                progress[1] = progress[1] + 1
            except:
                err.append(kext)
                continue
            self.update_oc_interface(kext, progress)

            try:
                tmp_path0 = os.path.abspath(
                    os.path.join(tmp_path,  kext + '/'))
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
                    source = os.path.abspath(
                        os.path.join(root, 'EFI/OC/Kexts/'))
                    update = os.path.abspath(os.path.join(tmp_path0, k))
                    source = source.replace(' ', '\ ')
                    os.system('cp -rf ' + update + ' ' + source)
                progress[1] = progress[1] + 1
            except:
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
        for i in self.local.keys():
            if i == self.bootloader:
                continue
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
            for i in self.local.keys():
                if i == self.bootloader:
                    continue
                if i in err:
                    if first_time == 0:
                        print(self.Colors(
                            "These Kext Package(s) Update Unsuccessfully:", fcolor='red'))
                        first_time = 1
                    if len(i) < 11:
                        print(self.Colors("   " + i, fcolor='yellow'))
                    else:
                        print(self.Colors("   " + i), fcolor='yellow')
            print("")
        input("Press [Enter] to continue...")
    

    def main(self):
        progress = 0
        self.main_interface(progress)
        self.download_database()
        progress += 1
        self.main_interface(progress)
        self.update_OpenCore()
        progress += 1
        self.main_interface(progress)
        self.generate_changelog_readme(progress)
        progress += 1
        self.main_interface(progress)
        

if __name__ == "__main__":
    # 实例化类
    uprepo = UpdateRepo()

    # run script
    uprepo.main()
