# Dell Latitude E7480 macOS 11 ~ 13(beta) (OpenCore)

<div style="align: center">
<img src="https://raw.githubusercontent.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/macOS-13/demo/system_info.png">
</div>

<div style="align: center">
<img src="https://raw.githubusercontent.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/main/demo/OC_info.png">
</div>

## 语言 / Lanuage
[简体中文](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/blob/main/README-cn.md)

English (Current)


## To Do
- [x] Add macOS 13 support

## Download
[![Download from https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases](https://img.shields.io/badge/Download-v0.8.2.1-blue)](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases/download/V0.8.2.1/EFI.zip)

## ChangeLog：V0.8.2.1

### Publish date ： 2021.07.22

#### Add Features :

1. Add Thunderbolt 3 support (not fully support)

Tip: Type-C port has 2 controllers: Thunderbolt 3 controller and USB 3.1 controller. Before the release, USB 3/3.1 is fully supported (including hot-plug), but Thunderbolt is not support. This release is only fix the thunderbolt port, but it does not support hot-plug, because it regonize the thunderbolt device as PCI device. If you want to use Thunderbolt, here is the points:

- Plug in the Thunderbolt device before start up
- Hot-plug NOT Supported

#### Files Changed:

1. Inject Thunderbolt Information


For more information, see the [Changelog.md](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/blob/main/Changelog.md).

## Infomation

<details>  
<summary><strong>Booter</strong></summary>
</br>
OpenCore  0.8.0 / 0.8.1 / 0.8.2
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

Tips: 
* For macOS 12 Monterey, DW1820 do not work well (can not use Airdrop, Handoff and Sidercar). Therefore I change it to BCM94360Z4 and it works well!
* Monterey 12.3 and iPad OS 15.4 start to support Universal Control (also need BoardCom wireless card), works for me.
* Strongly recommand you to re-create USBMap.kext for your own laptop with this [tool](https://github.com/corpnewt/USBMap).
* If you change your hardware (like wireless), re-create the USBMap.kext as well.
* It is strong recommanded that re-generate a serial number for your own laptop (needed to be check invaluable in apple.com) !
* Do not turn on `Find my mac`!

</details>

<details>  
<summary><strong>Kexts Version</strong></summary>
</br>

| Kexts          | Version                        | Updated Time       | Updated Way              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AirportBrcmFixup	|	2.1.6	|	2022-06-09	|	Official Release	|
|	AirportItlwm	|	2.2.0	|	2022-06-22	|	Compile on Local Machine	|
|	AlpsHID	|	1.3	|	2022-06-11	|	Official Release	|
|	AppleALC	|	1.7.3	|	2022-06-08	|	Official Release	|
|	BlueToolFixup	|	2.6.3	|	2022-06-09	|	Official Release	|
|	BrcmBluetoothInjector	|	2.6.3	|	2022-06-09	|	Official Release	|
|	BrcmFirmwareData	|	2.6.3	|	2022-06-09	|	Official Release	|
|	BrcmPatchRAM3	|	2.6.3	|	2022-06-09	|	Official Release	|
|	BrightnessKeys	|	1.0.3	|	2021-08-16	|	Official Release	|
|	CpuTscSync	|	1.0.8	|	2022-04-18	|	Official Release	|
|	ECEnabler	|	1.0.2	|	2021-10-27	|	Official Release	|
|	FeatureUnlock	|	1.0.9	|	2022-06-09	|	Official Release	|
|	HibernationFixup	|	1.4.6	|	2022-06-09	|	Official Release	|
|	IntelBluetoothFirmware	|	2.1.0	|	2021-12-10	|	Official Release	|
|	IntelBluetoothInjector	|	2.1.0	|	2021-12-10	|	Official Release	|
|	IntelMausi	|	1.0.8	|	2021-08-27	|	Official Release	|
|	Lilu	|	1.6.1	|	2022-06-22	|	Compile on Local Machine	|
|	NVMeFix	|	1.1.0	|	2022-06-09	|	Official Release	|
|	RealtekCardReader	|	0.9.7	|	2022-02-23	|	Official Release	|
|	RealtekCardReaderFriend	|	1.0.2	|	2022-02-23	|	Official Release	|
|	RestrictEvents	|	1.0.7	|	2022-02-08	|	Official Release	|
|	SMCBatteryManager	|	1.3.0	|	2022-06-07	|	Official Release	|
|	SMCDellSensors	|	1.3.0	|	2022-06-07	|	Official Release	|
|	SMCLightSensor	|	1.3.0	|	2022-06-07	|	Official Release	|
|	SMCProcessor	|	1.3.0	|	2022-06-07	|	Official Release	|
|	SMCSuperIO	|	1.3.0	|	2022-06-07	|	Official Release	|
|	USBMap	|	1.0	|	2022-03-18	|	USB Ports Inject	|
|	VerbStub	|	1.0.4	|	2021-11-05	|	Official Release	|
|	VirtualSMC	|	1.3.0	|	2022-06-07	|	Official Release	|
|	Voodoo PS/2 Controller	|	2.2.8	|	2022-03-08	|	Official Release	|
|	VoodooI2C	|	2.6.5	|	2021-02-28	|	Official Release	|
|	VoodooI2CHID	|	1	|	2021-12-05	|	Official Release	|
|	WhateverGreen	|	1.6.0	|	2022-06-11	|	Official Release	|



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

## Thunderbolt 3 Usage

Type-C port has 2 controllers: Thunderbolt 3 controller and USB controller. USB controller is fully supported (including hot-plug), but Thunderbolt only works when your pulg in your device before start up and it does not support hot-plug, because it regonize the thunderbolt device as PCI device. If you want to use Thunderbolt, here is the points:

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
* All contributors for this EFI.
