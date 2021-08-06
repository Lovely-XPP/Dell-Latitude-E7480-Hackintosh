# Dell Latitude E7480 macOS Big Sur 11.4 / Monterey 12.0 (OpenCore)

![Snapshot_21-07-31_10-17-57](https://user-images.githubusercontent.com/66028151/127725797-d5288a2a-b684-49ba-abe4-500dad500f83.png)

## Infomation

<details>  
<summary><strong>Booter</strong></summary>
</br>
OpenCore 0.7.0 / 0.7.1
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

</details>

## Status

<details>  
<summary><strong>What's working</strong></summary>
</br>

- [x] Intel HD 630 Graphics `incuding graphics acceleration`
- [x] All USB ports (Warn: Type-C does not support hot plug, plug it in your computer if you want to use it and turn it on again)
- [x] Internal camera
- [x] WiFi using [AirportBrcmFixup](https://github.com/acidanthera/AirportBrcmFixup)
- [x] Bluetooth using [BrcmFirmareData and BrcmPatchRAM3](https://github.com/acidanthera/BrcmPatchRAM)
- [x] Shutdown/ Reboot/ Sleep/ Wake
- [x] Speakers and headphones jack
- [x] Intel Gigabit Ethernet
- [x] App Store
- [x] (unsure) iMessage and Facetime 
- [x] miniDP and HDMI with digital audio passthrough(If you experience cursor lags, try turning on and off one of the displays.)
- [x] Keyboard and Trackpad(two finger vertical swipes)
- [x] Airdrop , Handoff and Sidecar
- [x] SD Card Reader using [Sinetek-rtsx](https://github.com/cholonam/Sinetek-rtsx)

</details>

<details>  
<summary><strong>What's not working</strong></summary>
</br>

- [ ] Multitouch gestures for ALPS touchpad.

</details>

## For Intel Wireless and Bluetooth

You can either operate in Windows or firstly install macOS (the Wifi and Bluetooth do not influence the entry to the Big Sur).

### Pre-pare
<details>  
<summary><strong>Editing Config.plist tool: ProperTree</strong></summary>
</br>

* Download: [ProperTree](https://github.com/corpnewt/ProperTree)
* Zip: Zip the downloaded files to the Desktop 
* Run ProperTree

  * For Windows user: run ProperTree.bat
  * For macOS user: run ProperTree.command

</details>


### Download & Install kexts

<details>  
<summary><strong>Download links</strong></summary>
</br>

- WiFi using [AirportItlwm](https://github.com/OpenIntelWireless/itlwm)
- Bluetooth using [IntelBluetoothFirmware and IntelBluetoothInjector](https://github.com/OpenIntelWireless/IntelBluetoothFirmware)

</details>

<details>  
<summary><strong>Install </strong></summary>
</br>

- In the dir `\EFI\OC\Kexts\`, remove the files 

  * `BrcmBluetoothInjector.kext`
  * `BrcmFirmwareData.kext`
  * `BrcmPatchRAM3.kext`

- Zip and Copy the listing files to `\EFI\OC\Kexts\`

  * `AirportItlwm.kext`
  * `IntelBluetoothFirmware.kext`
  * `IntelBluetoothInjector.kext` 

- Run ProperTree
- In the menu bar, choose `Files` -> `OC snapshot` -> choose the folder `\EFI\OC`
- Save files
- Reboot(in macOS) or install and enjoy!

</details>


