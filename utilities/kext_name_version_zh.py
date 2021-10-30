import os
import sys
import time
from biplist import *

os.chdir(sys.path[0])
root = os.path.abspath('..')
kext_name = []
kext_version = []
kext_time = []
kext_type = []
for kext in os.listdir(os.path.join(root,'EFI/OC/Kexts')):
    if kext == ".DS_Store":
        continue
    domain = os.path.abspath(os.path.join(root, 'EFI/OC/Kexts'))
    kext_full = os.path.join(domain, kext)
    plist = os.path.join(kext_full, 'Contents/Info.plist')
    k_time = os.stat(plist).st_mtime
    k_time = time.strftime('%Y-%m-%d', time.localtime(k_time))
    kext_time.append(k_time)
    plist = readPlist(plist)
    kext_name.append(plist['CFBundleName'])
    kext_version.append(plist['CFBundleVersion'])
    if kext == 'USBPorts.kext':
        kext_type.append('USB 端口注入')
        continue
    build_version = plist['BuildMachineOSBuild']
    build_version = build_version[0:2]
    if build_version == '21':
        kext_type.append('本地编译')
    else:
        kext_type.append('官方编译')
for i in range(len(kext_name)):
    for j in range(len(kext_name)-i-1):
        if kext_name[j] > kext_name[j+1]:
            temp1 = kext_name[j+1]
            temp2 = kext_version[j+1]
            temp3 = kext_time[j+1]
            temp4 = kext_type[j+1]
            kext_name[j+1] = kext_name[j]
            kext_version[j+1] = kext_version[j]
            kext_time[j+1] = kext_time[j]
            kext_type[j+1] = kext_type[j]
            kext_name[j] = temp1
            kext_version[j] = temp2
            kext_time[j] = temp3
            kext_type[j] = temp4
file = open('kexts_zh.txt', 'w')
for i in range(len(kext_name)):
    str = '|\t' + kext_name[i] + '\t|\t' + kext_version[i] + '\t|\t' + kext_time[i] + '\t|\t' + kext_type[i] + '\t|\n'
    file.write(str)
