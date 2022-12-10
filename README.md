# Dell Latitude E7480 macOS 11 ~ 13(beta) (OpenCore)

## Introduce

> Tip: I have bought a MacBookPro, so I can not maintain this repo manully any more. Therefore, I wrote a scrip to update this repo actomatically. If you encount error when using it, please open an issue, I will try my best to fix it. Thanks for your support.

<div style="align: center">
<img src="https://raw.githubusercontent.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/macOS-13/demo/system_info.png">
</div>

<div style="align: center">
<img src="https://raw.githubusercontent.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/main/demo/OC_info.png">
</div>

## 语言 / Lanuage

[简体中文](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/blob/main/README_zh.md)

English (Current)


## To Do
- [x] Automatically update OpenCorePkg and Kexts by a script
- [x] Automatically generate update info and update ReadMe



## Note

1. If you meet hot-plug issue with thunderbolt devices, try ***Enable*** `UEFI->Drivers->TbTPowerForce.efi `.
2. If crashed in installing macOS from USB, try ***Enable*** `UEFI->Quirks->ReleaseUsbOwnership`, thanks @krzysinek (#22).
3. For macOS 12 Monterey, DW1820 do not work well (can not use Airdrop, Handoff and Sidercar). Therefore I change it to BCM94360Z4 and it works well!
4. Monterey 12.3 and iPad OS 15.4 start to support Universal Control (also need BoardCom wireless card), works for me.
5. Strongly recommand you to re-create USBMap.kext for your own laptop with this [tool](https://github.com/corpnewt/USBMap).
6. If you change your hardware (like wireless), re-create the USBMap.kext as well.
7. It is strong recommanded that re-generate a serial number for your own laptop (needed to be check invaluable in apple.com) !
8. Do not turn on `Find my mac`!



## Download
[![Download from https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases](https://img.shields.io/badge/Download-v0.8.7.0-blue)](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases/tag/v0.8.7.0)

## ChangeLog: V0.8.7.0

### Publish date : 2022.12.08

#### Add Features :

1. Update kexts and OC boot version to  0.8.7
1. Downgrade `AlpsHID.kext` for stable use, thanks @RJJvW (#21) and @H3xidecimal (#18)

#### Files Changed :

1. All the EFI folder to adapt OC 0.8.7
2. Update kexts with official Release:

| Kexts          | Version                        | Updated Time       | Updated Way              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AlpsHID	|	1.0.0d1	|	2022-11-21	|	Compile on Local Machine	|
|	AppleALC	|	1.7.8	|	2022-12-08	|	Official Release	|
|	FeatureUnlock	|	1.1.2	|	2022-12-08	|	Official Release	|
|	HibernationFixup	|	1.4.8	|	2022-12-08	|	Official Release	|
|	IntelBluetoothFirmware	|	2.3.0	|	2022-12-08	|	Official Release	|
|	IntelBluetoothInjector	|	2.3.0	|	2022-12-08	|	Official Release	|
|	Voodoo PS/2 Controller	|	2.3.3	|	2022-12-08	|	Official Release	|
|	WhateverGreen	|	1.6.3	|	2022-12-08	|	Official Release	|


For more information, see the [Changelog.md](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/blob/main/Changelog.md).

## Infomation

<details>  
<summary><strong>Booter</strong></summary>
</br>
OpenCore  0.8.0 / 0.8.1 / 0.8.2 / 0.8.3 / 0.8.4 / 0.8.5 / 0.8.6 / 0.8.7
</details>

<details>  
<summary><strong>MacOS Supported/Tested</strong></summary>
</br>
- Big Sur 11.0 - 11.7 </br>
- Monterey 12.0 - 12.5.1 beta</br>
- Ventura 13.0 beta (I am using)</br>
</details>

<details>  
<summary><strong>My Hardware</strong></summary>
</br>

| Model              | Dell Latitude E7480                        |
|:-------------------|:-------------------------------------------|
| Processor          | Intel Core i7-7700U                        |
| Graphics           | Integrated Intel HD Graphics 620           |
| Memory             | 8GB 2133MHz DDR4 * 2                       |
| Display            | 13" 2K (2560x1440) with ELAN Touchscreen   |
| Storage            | Sandisk 1T M.2 NVMe SSD                    |
| WLAN + Bluetooth   | Broadcom BCM94360Z4                        |
| Camera             | 1920x1080 FHD Webcam                       |
| Fingerprint Reader | No                                         |
| Soundcard          | Realtek ALC256                             |
| Keyboard           | Backlit Keyboard                           |
| Trackpad           | ALPS Touchpad                              |
| microSD Card Reader| Realtek RTS525A microSD card reader        |

</details>

<details>  
<summary><strong>Kexts Version</strong></summary>
</br>

| Kexts          | Version                        | Updated Time       | Updated Way              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AirportBrcmFixup	|	2.1.7	|	2022-12-08	|	Official Release	|
|	AirportItlwm	|	2.2.0	|	2022-11-07	|	Official Release	|
|	AlpsHID	|	1.0.0d1	|	2021-12-05	|	Official Release	|
|	AppleALC	|	1.7.8	|	2022-12-08	|	Official Release	|
|	BlueToolFixup	|	2.6.5	|	2022-12-08	|	Official Release	|
|	BrcmBluetoothInjector	|	2.6.5	|	2022-12-08	|	Official Release	|
|	BrcmFirmwareData	|	2.6.5	|	2022-12-08	|	Official Release	|
|	BrcmPatchRAM3	|	2.6.5	|	2022-12-08	|	Official Release	|
|	BrightnessKeys	|	1.0.3	|	2022-12-08	|	Official Release	|
|	CpuTscSync	|	1.1.0	|	2022-12-08	|	Official Release	|
|	ECEnabler	|	1.0.3	|	2022-12-08	|	Official Release	|
|	FeatureUnlock	|	1.1.2	|	2022-12-08	|	Official Release	|
|	HibernationFixup	|	1.4.8	|	2022-12-08	|	Official Release	|
|	IntelBluetoothFirmware	|	2.3.0	|	2022-12-08	|	Official Release	|
|	IntelBluetoothInjector	|	2.3.0	|	2022-12-08	|	Official Release	|
|	IntelMausi	|	1.0.8	|	2022-12-08	|	Official Release	|
|	Lilu	|	1.6.3	|	2022-12-08	|	Official Release	|
|	NVMeFix	|	1.1.1	|	2022-12-08	|	Official Release	|
|	RealtekCardReader	|	0.9.7	|	2022-11-07	|	Official Release	|
|	RestrictEvents	|	1.1.0	|	2022-12-08	|	Official Release	|
|	SMCBatteryManager	|	1.3.1	|	2022-12-08	|	Official Release	|
|	SMCDellSensors	|	1.3.1	|	2022-12-08	|	Official Release	|
|	SMCLightSensor	|	1.3.1	|	2022-12-08	|	Official Release	|
|	SMCProcessor	|	1.3.1	|	2022-12-08	|	Official Release	|
|	SMCSuperIO	|	1.3.1	|	2022-12-08	|	Official Release	|
|	USBMap	|	1.0	|	2022-11-07	|	USB Ports Inject	|
|	VerbStub	|	1.0.4	|	2022-11-07	|	Official Release	|
|	VirtualSMC	|	1.3.1	|	2022-12-08	|	Official Release	|
|	Voodoo PS/2 Controller	|	2.3.3	|	2022-12-08	|	Official Release	|
|	VoodooI2CHID	|	1	|	2022-11-07	|	Official Release	|
|	WhateverGreen	|	1.6.3	|	2022-12-08	|	Official Release	|
|	RealtekCardReaderFriend	|	1.0.2	|	2022-11-07	|	Official Release	|
|	VoodooI2C	|	2.7	|	2022-12-08	|	Official Release	|

</details>

## Status



<details>  
<summary><strong>What's working</strong></summary>
</br>

- [x] Intel HD 620 Graphics `incuding graphics acceleration`
- [x] All USB ports
- [x] HDMI/Type-C display monitor Hot-Plug fully supported(Sleep/dim after lock, audio output support)
- [x] Internal camera
- [x] WiFi （2.4 GHz / 5 GHz）
- [x] Bluetooth
- [x] Shutdown/ Reboot/ Sleep/ Wake (include Fn + insert and LID device to sleep)
- [x] All fn key work (You need to setting on bios first. Go to POST Behavior -> Fn Lock Options. Check Fn Lock and Lock mode disable/standard)  
- [x] Speakers and headphones jack
- [x] External mic/Headphone mic jack(Working with [combojack](https://github.com/hackintosh-stuff/ComboJack)) 
- [x] Intel Gigabit Ethernet
- [x] App Store
- [x] (unsure, associated with your apple account) iMessage and Facetime 
- [x] miniDP and HDMI with digital audio passthrough(If you experience cursor lags, try turning on and off one of the displays.)
- [x] Keyboard and Trackpad (support Multitouch gestures)
- [x] Airdrop , Handoff , Sidecar, Airplay and Universal Control (These features are only for Broadcom wireless card, besides, Airplay is only support for macOS 12 and Universal Control need macOS 12.3)
- [x] SD Card Reader

</details>

<details>  
<summary><strong>What's not working</strong></summary>
</br>

- [ ] Thunderbolt 3 hot-plug

</details>



## Recommended Bios Setup

Enable:

1. `System Configuration` -> `Integrated NIC` -> `Enabled`

   But not tick the entry:

   - [ ] `Enable UEFI NetWork`

2. `System Configuration` -> `SATA Operation` -> `AHCI`

3. `System Configuration` -> `Thunderbolt Adapter Configuration` -> Enable all entries and select 

   `Security level - No security`
   
   

Disable:

1. `Secure Boot` -> `Secure Boot Enable` -> `Disabled`
2. `Intel Software Guard Extension` -> `Intel SGX Enable` -> `Disabled`



## IGPU 4K output Enabled

This part is credited from [Lorys89-DELL_LATITUDE_7280](https://github.com/Lorys89/DELL_LATITUDE_7280).

1. Open `config.plist` and delete `framebuffer-fbmem` and `framebuffer-stolenmem` in `DeviceProperties`, `PciRoot(0x0)/Pci(0x2,0x0)`

2. Restart and at the opencore boot GUI, choose the `modGRUBShell.efi`


3. For set DVMT PRE Allocated to 64 MB

``setup_var 0x795 0x2``


![DMT-PRE](https://raw.githubusercontent.com/Lorys89/DELL_LATITUDE_7280/main/Screenshot/DVMT-PRE.png)



4. For set DVMT Total GFX Mem to MAX

``setup_var 0x796 0x3``


![DMT-PRE](https://raw.githubusercontent.com/Lorys89/DELL_LATITUDE_7280/main/Screenshot/DVMT-TOT.png)




## Thunderbolt 3 Usage

Type-C port has 2 controllers: Thunderbolt 3 controller and USB controller. USB controller is fully supported (including hot-plug), but Thunderbolt only works when you plug in the device before start up and it does not support hot-plug, because it regonize the thunderbolt device as PCI device. If you want to use Thunderbolt, here is the points:

- Plug in the Thunderbolt device before start up
- Hot-plug **NOT** Supported


## For Intel Wireless and Bluetooth

Now, I add a config for Intel wireless card kexts. The method to use it is as below

* Delete the existing `config.plist`
* Change `config-intel-wireless-card.plist` into `config.plist`

## ComboJack Installation

Hackintosh combojack support for alc256/alc255 from https://github.com/hackintosh-stuff/ComboJack

Follow this step:
* Clone combojack repository
* Run ComboJack_Installer/install.sh in terminal and reboot
* Done. When you attach a headphone there will be a popup asking about headphone type.

## Credits
* [Acidanthera](https://github.com/Acidanthera) for oc package and main kexts.
* [daliansky](https://github.com/daliansky) for awsome SSDTs in [OC-little](https://github.com/daliansky/OC-little).
* [Dortania](https://dortania.github.io/) for installation and other guides.
* [the-darkvoid](https://github.com/the-darkvoid) for partly solve thunderbolt(type-C) hot-plug issue in [IOElectrify](https://github.com/the-darkvoid/macOS-IOElectrify).
* [hackintosh-stuff](https://github.com/hackintosh-stuff) for support externel mic/headphone with ALC256 in [combojack](https://github.com/hackintosh-stuff/ComboJack).
* [0xFireWolf](https://github.com/0xFireWolf) for SD card reader support in [RealtekCardReader](https://github.com/0xFireWolf/RealtekCardReader) and [RealtekCardReaderFriend](https://github.com/0xFireWolf/RealtekCardReaderFriend).
* [blankmac](https://github.com/blankmac) for trackpad with multitouch gestures in [AlpsT4USB](https://github.com/blankmac/AlpsT4USB).
* [Lorys89](https://github.com/Lorys89) for providing DVMT fixed up method for 4K Monitor output in [Lorys89-DELL_LATITUDE_7280](https://github.com/Lorys89/DELL_LATITUDE_7280).
* All contributors for this EFI.
