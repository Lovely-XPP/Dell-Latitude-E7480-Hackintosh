import os
import sys
import shutil
from biplist import *

os.chdir(sys.path[0])
root = os.path.abspath('..')

# set the files path
BCM_origin = 'config_BCM.plist'
BCM_destination = os.path.join(root, 'EFI/OC/config.plist')
Intel_origin = 'config-Intel-wirelss-card.plist'
Intel_destination = os.path.join(root, 'EFI/OC/config-Intel-wirelss-card.plist')

origin_plist = readPlist("config.plist")
writePlist(origin_plist, "config.plist", binary=False)

# Change the Platform Info (Serial number)
plat_info = origin_plist['PlatformInfo']
generic = plat_info['Generic']
generic['MLB'] = 'C02801108GUJH4RA8'
generic['SystemSerialNumber'] = 'C02W20ZAJHCC'
generic['SystemUUID'] = 'E8740DC8-849B-4D95-B3DE-8CEC4BE37CF8'

# change kexts settings
kernel = origin_plist['Kernel']
for element in kernel['Add']:
    if element['BundlePath'] == 'IOElectrify.kext':
        element['Enabled'] = True

BCM_config = origin_plist.copy()
writePlist(BCM_config, "config_BCM.plist", binary=False)

# change kexts for Intel wireless card user
for element in kernel['Add']:
    if element['BundlePath'] == 'AirportItlwm-Monterey.kext':
        element['Enabled'] = True
    
    if element['BundlePath'] == 'AirportItlwm.kext':
        element['Enabled'] = True
    
    if element['BundlePath'] == 'IntelBluetoothInjector.kext':
        element['Enabled'] = True

    if element['BundlePath'] == 'IntelBluetoothFirmware.kext':
        element['Enabled'] = True

    if element['BundlePath'] == 'IntelBluetoothFirmware.kext':
        element['Enabled'] = True
    
    if element['BundlePath'] == 'AirportBrcmFixup.kext':
        element['Enabled'] = False

    if element['BundlePath'] == 'AirportBrcmFixup.kext/Contents/PlugIns/AirPortBrcmNIC_Injector.kext':
        element['Enabled'] = False

    if element['BundlePath'] == 'AirportBrcmFixup.kext/Contents/PlugIns/AirPortBrcm4360_Injector.kext':
        element['Enabled'] = False

    if element['BundlePath'] == 'BrcmBluetoothInjector.kext':
        element['Enabled'] = False
    
    if element['BundlePath'] == 'BrcmFirmwareData.kext':
        element['Enabled'] = False
    
    if element['BundlePath'] == 'BrcmPatchRAM3.kext':
        element['Enabled'] = False

    if element['BundlePath'] == 'FeatureUnlock.kext':
        element['Enabled'] = False


# change the boot-args for Intel wireless card user
nvram = origin_plist['NVRAM']
nvram_add = nvram['Add']
boot_args = nvram_add['7C436110-AB2A-4BBB-A880-FE41995C9F82']
boot_args['boot-args'] = 'alcid=56 igfxonln=1'

Intel_config = origin_plist.copy()
writePlist(Intel_config, "config-Intel-wirelss-card.plist", binary=False)

# move the config files
shutil.move(BCM_origin, BCM_destination)
shutil.move(Intel_origin, Intel_destination)
