import os
import sys
import time
import platform
from plistlib import *

os.chdir(sys.path[0])
root = os.path.abspath('./')
kext_name = []
kext_version = []
kext_time = []
kext_type = []
kext_type_zh = []

# 获取本地 MacOS 版本
kernel = platform.system()
if kernel != "Darwin":
    print("The script is only supported for MacOS !")
    exit()
t = os.popen('sw_vers').read()
t = t.split('BuildVersion:')
t = t[1]
t = t.strip()
system_ver = t

for kext in os.listdir(os.path.join(root,'update_kexts')):
    if kext == ".DS_Store":
        continue
    print(kext)
    domain = os.path.abspath(os.path.join(root, 'update_kexts'))
    kext_full = os.path.join(domain, kext)
    plist = os.path.join(kext_full, 'Contents/Info.plist')
    k_time = os.stat(plist).st_mtime
    k_time = time.strftime('%Y-%m-%d', time.localtime(k_time))
    kext_time.append(k_time)
    with open(plist, 'rb') as pl:
        plist = load(pl)
    kext_name.append(plist['CFBundleName'])
    kext_version.append(plist['CFBundleVersion'])
    build_version = plist['BuildMachineOSBuild']
    if build_version[0:4] == system_ver[0:4]:
        kext_type.append('Compile on Local Machine')
        kext_type_zh.append('本地编译')
    else:
        kext_type.append('Official Release')
        kext_type_zh.append('官方编译')
for i in range(len(kext_name)):
    for j in range(len(kext_name)-i-1):
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

file = open('update_kexts.txt', 'w')
str0 = '| Kexts          | Version                        | Updated Time       | Updated Way              |\n'
str1 = '|:----------------|:-------------------------------------------|:---------------|:----------------|\n'
file.write(str0)
file.write(str1)
for i in range(len(kext_name)):
    str = '|\t' + kext_name[i] + '\t|\t' + kext_version[i] + '\t|\t' + kext_time[i] + '\t|\t' + kext_type[i] + '\t|\n'
    file.write(str)
file.close()


file = open('update_kexts_zh.txt', 'w')
str0 = '| 驱动名称          | 版本号                       | 更新时间       | 更新方式              |\n'
str1 = '|:----------------|:-------------------------------------------|:---------------|:----------------|\n'
file.write(str0)
file.write(str1)
for i in range(len(kext_name)):
    str = '|\t' + kext_name[i] + '\t|\t' + kext_version[i] + '\t|\t' + kext_time[i] + '\t|\t' + kext_type_zh[i] + '\t|\n'
    file.write(str)
file.close()
