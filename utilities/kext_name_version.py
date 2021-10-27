import os
import sys
from biplist import *

os.chdir(sys.path[0])
root = os.path.abspath('..')
kext_name = []
kext_version = []
for kext in os.listdir(os.path.join(root,'EFI/OC/Kexts')):
    if kext == ".DS_Store":
        continue
    domain = os.path.abspath(os.path.join(root, 'EFI/OC/Kexts'))
    kext = os.path.join(domain, kext)
    plist = os.path.join(kext, 'Contents/Info.plist')
    plist = readPlist(plist)
    kext_name.append(plist['CFBundleName'])
    kext_version.append(plist['CFBundleVersion'])
for i in range(len(kext_name)):
    for j in range(len(kext_name)-i-1):
        if kext_name[j] > kext_name[j+1]:
            temp1 = kext_name[j+1]
            temp2 = kext_version[j+1]
            kext_name[j+1] = kext_name[j]
            kext_version[j+1] = kext_version[j]
            kext_name[j] = temp1
            kext_version[j] = temp2
file = open('kexts.txt', 'w')
for i in range(len(kext_name)):
    str = '|\t' + kext_name[i] + '\t|\t' + kext_version[i] + '|\n'
    file.write(str)

