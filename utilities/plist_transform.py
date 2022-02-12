import os
import sys
import shutil
from plistlib import *

# set work dir and read the origin config
os.chdir(sys.path[0])
root = os.path.abspath('..')
with open("config.plist", 'rb') as pl:
    origin_plist = load(pl)

# set the files path
BCM_origin = 'config_BCM.plist'
BCM_destination = os.path.join(root, 'EFI/OC/config.plist')
Intel_origin = 'config-Intel-wirelss-card.plist'
Intel_destination = os.path.join(root, 'EFI/OC/config-Intel-wirelss-card.plist')

# Change the Devices Propertries
devices = origin_plist['DeviceProperties']
devices['Add'] = {
    'PciRoot(0x0)/Pci(0x1C,0x0)/Pci(0x0,0x0)': 
    {   
        'AAPL,slot-name': 'Built-in', 
        'device_type': 'Media Controller', 
        'model': 'Realtek RTS525A microSD card reader', 
        'name': 'multimedia', 
        'pci-aspm-default': b'\x02\x01\x00\x00'
    }, 
    'PciRoot(0x0)/Pci(0x2,0x0)': 
    {
        'AAPL,ig-platform-id': b'\x00\x00\x16Y', 
        'disable-agdc': b'\x01\x00\x00\x00', 
        'enable-hdmi-dividers-fix': b'\x01\x00\x00\x00', 
        'enable-hdmi20': b'\x01\x00\x00\x00', 
        'force-online': b'\x01\x00\x00\x00', 
        'framebuffer-con0-alldata': b'\x00\x00\x08\x00\x02\x00\x00\x00\x98\x00\x00\x00', 
        'framebuffer-con0-enable': b'\x01\x00\x00\x00', 
        'framebuffer-con1-alldata': b'\x01\x05\t\x00\x00\x08\x00\x00\x87\x01\x00\x00', 
        'framebuffer-con1-enable': b'\x01\x00\x00\x00', 
        'framebuffer-con2-alldata': b'\x02\x04\n\x00\x00\x04\x00\x00\x87\x01\x00\x00', 
        'framebuffer-con2-enable': b'\x01\x00\x00\x00', 
        'framebuffer-fbmem': b'\x00\x00\x90\x00', 
        'framebuffer-patch-enable': b'\x01\x00\x00\x00', 
        'framebuffer-stolenmem': b'\x00\x000\x01', 
        'model': 'Intel HD Graphics 620', 
        'pci-aspm-default': b'\x02\x00\x00\x00'
    }
}

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
with open("config_BCM.plist", 'wb') as pl_BCM:
    dump(BCM_config, pl_BCM, fmt=FMT_XML, sort_keys=True, skipkeys=False)

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
with open("config-Intel-wirelss-card.plist", 'wb') as pl_Intel:
    dump(Intel_config, pl_Intel, fmt=FMT_XML, sort_keys=True, skipkeys=False)

# move the config files
shutil.move(BCM_origin, BCM_destination)
shutil.move(Intel_origin, Intel_destination)
