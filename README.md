# Dell Latitude E7480 macOS Big Sur 11 / Monterey 12.0 (OpenCore)

<div style="align: center">
<img src="https://user-images.githubusercontent.com/66028151/139106659-df5a4237-6c56-4bdf-8f02-7bbeb89fbc4b.png">
</div>

 
## 语言 / Lanuage
[简体中文](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/blob/main/README-cn.md)

English (Current)

## Download
[![Download from https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases](https://img.shields.io/badge/Download-v0.7.4.1-blue)](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases)

## Infomation

<details>  
<summary><strong>Booter</strong></summary>
</br>
OpenCore 0.7.2 / 0.7.3 / 0.7.4
</details>

<details>  
<summary><strong>MacOS Supported/Tested</strong></summary>
</br>
- Big Sur 11.5.0 - 11.5.2 </br>
- Big Sur 11.6 - 11.6.1 </br>
- Monterey 12.0 - 12.0.1 </br>
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

Tips: 
* For macOS 12 Monterey, DW1820 do not work well (can not use Airdrop, Handoff and Sidercar). Therefore I change it to BCM94360Z4 and it works well!
* Strongly recommand you to re-create USBMap.kext for your own laptop with this [tool](https://github.com/corpnewt/USBMap) 
* If you change your hardware (like wireless), re-create the USBMap.kext as well.
* It is strong recommanded that re-generate a serial number for your own laptop(needed to be check invaluable in apple.com)!
* Do not turn on `Find my mac`!

</details>

<details>  
<summary><strong>Kexts Version</strong></summary>
</br>

| Kexts          | Version                        | Updated Time       | Updated Way              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AirportBrcmFixup	|	2.1.4	|	2021-08-16	|	Compile on Local Machine	|
|	AirportItlwm	|	2.1.0	|	2021-10-27	|	Compile on Local Machine	|
|	AirportItlwm	|	2.1.0	|	2021-10-27	|	Compile on Local Machine	|
|	AlpsT4USB	|	1.0.0d1	|	2021-10-09	|	Official Release	|
|	AppleALC	|	1.6.5	|	2021-10-04	|	Official Release	|
|	BlueToolFixup	|	2.6.1	|	2021-10-27	|	Compile on Local Machine	|
|	BrcmBluetoothInjector	|	2.6.1	|	2021-10-22	|	Official Release	|
|	BrcmFirmwareData	|	2.6.1	|	2021-10-27	|	Compile on Local Machine	|
|	BrcmPatchRAM3	|	2.6.1	|	2021-10-27	|	Compile on Local Machine	|
|	BrightnessKeys	|	1.0.3	|	2021-08-16	|	Compile on Local Machine	|
|	CPUFriend	|	1.2.5	|	2021-08-16	|	Compile on Local Machine	|
|	CpuTscSync	|	1.0.5	|	2021-10-04	|	Official Release	|
|	ECEnabler	|	1.0.2	|	2021-10-27	|	Compile on Local Machine	|
|	FeatureUnlock	|	1.0.4	|	2021-10-22	|	Compile on Local Machine	|
|	HibernationFixup	|	1.4.5	|	2021-10-27	|	Compile on Local Machine	|
|	IOElectrify	|	1.0.0	|	2021-10-10	|	Compile on Local Machine	|
|	IntelBluetoothFirmware	|	2.0.1	|	2021-10-27	|	Compile on Local Machine	|
|	IntelBluetoothInjector	|	2.0.1	|	2021-10-27	|	Compile on Local Machine	|
|	IntelMausi	|	1.0.8	|	2021-08-27	|	Official Release	|
|	Lilu	|	1.5.7	|	2021-10-27	|	Compile on Local Machine	|
|	NVMeFix	|	1.1.0	|	2021-08-23	|	Compile on Local Machine	|
|	RealtekCardReader	|	0.9.7	|	2021-10-27	|	Compile on Local Machine	|
|	RealtekCardReaderFriend	|	1.0.0	|	2021-08-16	|	Compile on Local Machine	|
|	RestrictEvents	|	1.0.5	|	2021-10-04	|	Official Release	|
|	SMCBatteryManager	|	1.2.7	|	2021-09-06	|	Official Release	|
|	SMCDellSensors	|	1.2.7	|	2021-09-06	|	Official Release	|
|	SMCLightSensor	|	1.2.7	|	2021-09-06	|	Official Release	|
|	SMCProcessor	|	1.2.7	|	2021-09-06	|	Official Release	|
|	SMCSuperIO	|	1.2.7	|	2021-09-06	|	Official Release	|
|	USBMap	|	1.0	|	2021-09-06	|	USB Ports Inject	|
|	VerbStub	|	1.0.4	|	2021-06-20	|	Official Release	|
|	VirtualSMC	|	1.2.7	|	2021-09-06	|	Official Release	|
|	Voodoo PS/2 Controller	|	2.2.6	|	2021-10-04	|	Official Release	|
|	VoodooI2C	|	2.6.5	|	2021-02-28	|	Official Release	|
|	VoodooI2CHID	|	1	|	2021-10-10	|	Official Release	|
|	WhateverGreen	|	1.5.5	|	2021-10-27	|	Compile on Local Machine	|

</details>

## Status

<details>  
<summary><strong>What's working</strong></summary>
</br>

- [x] Intel HD 620 Graphics `incuding graphics acceleration`
- [x] All USB ports (Warn: Type-C fully support hot plug)
- [x] HDMI/Type-C display monitor Hot-Plug fully supported(Sleep/dim after lock, audio output support)
- [x] Internal camera
- [x] WiFi （2.4GHz/5G）
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
- [x] Airdrop , Handoff , Sidecar and Airplay(Airplay is only support for macOS12)
- [x] SD Card Reader

</details>

<details>  
<summary><strong>What's not working</strong></summary>
</br>

None so far.

</details>

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
* [the-darkvoid](https://github.com/the-darkvoid) for partly solve thunderbolt(type-C) hot-plug issue in [IOElectrify](https://github.com/the-darkvoid/macOS-IOElectrify)
* [hackintosh-stuff](https://github.com/hackintosh-stuff)for support externel mic/headphone with ALC256 in [combojack](https://github.com/hackintosh-stuff/ComboJack).
* [0xFireWolf](https://github.com/0xFireWolf)for SD card reader support in [RealtekCardReader](https://github.com/0xFireWolf/RealtekCardReader) and [RealtekCardReaderFriend](https://github.com/0xFireWolf/RealtekCardReaderFriend).
* [blankmac](https://github.com/blankmac) for trackpad with multitouch gestures in [AlpsT4USB](https://github.com/blankmac/AlpsT4USB).
* All contributors for this EFI.
