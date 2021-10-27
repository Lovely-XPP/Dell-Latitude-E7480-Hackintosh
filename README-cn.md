# 戴尔 Latitude E7480 macOS Big Sur 11 / Monterey 12.0 (OpenCore引导)

<div style="align: center">
<img src="https://user-images.githubusercontent.com/66028151/139106659-df5a4237-6c56-4bdf-8f02-7bbeb89fbc4b.png">
</div>
 
## 语言 / Lanuage
简体中文(当前语言)

[English](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/blob/main/README.md)

## 下载
[![Download from https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases](https://img.shields.io/badge/Download-v0.7.4.1-blue)](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases)

## 引导 & 硬件信息

<details>  
<summary><strong>OC引导版本</strong></summary>
</br>
OpenCore 0.7.2 / 0.7.3 / 0.7.4
</details>

<details>  
<summary><strong>测试过/支持的系统版本</strong></summary>
</br>
- Big Sur 11.5.0 - 11.5.2</br>
- Big Sur 11.6 - 11.6.1</br>
- Monterey 12.0 - 12.0.1</br>
</details>

<details>  
<summary><strong>硬件信息</strong></summary>
</br>

| Model           | Dell Latitude E7480                        |
|:----------------|:-------------------------------------------|
| 处理器           | Intel Core i7-7700U                        |
| 图形卡           | 集成显卡：Intel HD Graphics 620           |
| 内存条           | 8GB 2133MHz DDR4 * 2                       |
| 显示器           | 13" 2K (2560x1440) 触摸屏                   |
| 硬盘             | 闪迪 1T M.2 NVMe SSD                        |
| 无线网卡/蓝牙     | 博通 BCM94360Z4                        |
| 摄像头           | 1920x1080 FHD Webcam                       |
| 指纹读取          | 有但不适用于macOS                           |
| 声卡             | 瑞昱 ALC256                             |
| 键盘             | 背光键盘                           |
| 触摸板           | ALPS 触摸板                              |
| SD读卡器         | 瑞昱 RTS525A 读卡器        |

使用小贴士: 
* 对于苹果 macOS 12 Monterey, DW1820A网卡兼容性不那么好，主要是蓝牙驱动，导致隔空投送、接力等服务无法使用，于是换了张BCM9460Z4的网卡，目前无任何不兼容的问题！
* 强烈建议在进入系统以后使用[USBMap](https://github.com/corpnewt/USBMap) 工具进行USB定制！
* 如果你进行了硬件更改（比如网卡更换），同样也建议你使用[USBMap](https://github.com/corpnewt/USBMap) 工具重新进行USB定制！
* 进入系统后，建议重新生成对应机型序列号（需要经过官网查询无效方可使用）！
* 不要开启查找我的Mac功能！
</details>

## 驱动版本

| 驱动          | 版本号                        |
|:----------------|:-------------------------------------------|
|	AirportBrcmFixup	|	2.1.4|
|	AirportItlwm	|	2.1.0|
|	AirportItlwm	|	2.1.0|
|	AlpsT4USB	|	1.0.0d1|
|	AppleALC	|	1.6.5|
|	BlueToolFixup	|	2.6.1|
|	BrcmBluetoothInjector	|	2.6.1|
|	BrcmFirmwareData	|	2.6.1|
|	BrcmPatchRAM3	|	2.6.1|
|	BrightnessKeys	|	1.0.3|
|	CPUFriend	|	1.2.5|
|	CpuTscSync	|	1.0.5|
|	ECEnabler	|	1.0.2|
|	FeatureUnlock	|	1.0.4|
|	HibernationFixup	|	1.4.5|
|	IOElectrify	|	1.0.0|
|	IntelBluetoothFirmware	|	2.0.1|
|	IntelBluetoothInjector	|	2.0.1|
|	IntelMausi	|	1.0.8|
|	Lilu	|	1.5.7|
|	NVMeFix	|	1.1.0|
|	RealtekCardReader	|	0.9.7|
|	RealtekCardReaderFriend	|	1.0.0|
|	RestrictEvents	|	1.0.5|
|	SMCBatteryManager	|	1.2.7|
|	SMCDellSensors	|	1.2.7|
|	SMCLightSensor	|	1.2.7|
|	SMCProcessor	|	1.2.7|
|	SMCSuperIO	|	1.2.7|
|	USBMap	|	1.0|
|	VerbStub	|	1.0.4|
|	VirtualSMC	|	1.2.7|
|	Voodoo PS/2 Controller	|	2.2.6|
|	VoodooI2C	|	2.6.5|
|	VoodooI2CHID	|	1|
|	WhateverGreen	|	1.5.5|


## 工作状态

<details>  
<summary><strong>可用功能</strong></summary>
</br>

- [x] 显卡Intel HD 620 Graphics的正常驱动（包含双硬解码、GPU加速）
- [x] 所有的USB端口都正常工作 (注意：Type-C接口已经部分支持热插拔！但是要使用Type-C接口仍然需要关机后接上再启动！)
- [x] HDMI/Type-C 接口支持音频输出并支持热插拔 
- [x] 内置摄像头
- [x] Wifi 使用[AirportBrcmFixup](https://github.com/acidanthera/AirportBrcmFixup)成功稳定驱动（2.4GHz/5G）
- [x] 蓝牙 使用[BrcmFirmareData and BrcmPatchRAM3](https://github.com/acidanthera/BrcmPatchRAM)驱动（macOS仅需使用其中的BlueToolfixup，配置文件都已经设置好）
- [x] 关机/ 重启/ 睡眠/ 唤醒 (包含 Fn + insert 键睡眠和合盖睡眠)
- [x] 所有Fn键的功能 (需要关闭bios关于Fn键锁：bios -> POST Behavior -> Fn Lock Options)
- [x] 扬声器和耳机插孔
- [x] 外置麦克风和耳麦(仅在Big Sur 11.6 上测试成功，使用的是[combojack](https://github.com/hackintosh-stuff/ComboJack)) 
- [x] Intel 有线网络
- [x] 苹果商店和iCloud账户服务，不要开启查找我的Mac功能！
- [x] (不一定可用，和你的账户也有关系) iMessage 和 Facetime 
- [x] miniDP 和 HDMI （支持音频输入）
- [x] 键盘、触摸屏(触摸屏支持手势)、触摸板（触摸板支持多手势）
- [x] 隔空投送、接力、随航、隔空播放（隔空播放仅限macOS 12）
- [x] SD读卡器使用 [RealtekCardReader](https://github.com/0xFireWolf/RealtekCardReader) 和 [RealtekCardReaderFriend](https://github.com/0xFireWolf/RealtekCardReaderFriend) 驱动，使得SD读卡器原生化。

</details>

<details>  
<summary><strong>不可用功能</strong></summary>
</br>

暂时没有不可用功能

</details>

## 对于 Intel 无线网卡

为了简化操作，已经添加了相应的config-intel-wireless-card.plist，在使用前
* 把原来的`config.plist`删掉
* 把`config-intel-wireless-card.plist`改成`config.plist`


## ComboJack 安装说明

关于声卡ALC256/255的黑苹果混合耳机插孔（输入输出混合插孔）在 https://github.com/hackintosh-stuff/ComboJack

安装请采用这些步骤:
* 克隆ComboJack仓库
* 在终端运行 ComboJack_Installer/install.sh
* 完成。请注意在插入插孔后，会有弹窗提示你选择相应的接口。（建议选耳麦）

## 致谢
* [Acidanthera](https://github.com/Acidanthera) 的 OC包和主要的驱动
* [daliansky](https://github.com/daliansky) 的很棒的SSDTs：[OC-little](https://github.com/daliansky/OC-little)
* [Dortania](https://dortania.github.io/)的OC安装教程
* [the-darkvoid](https://github.com/the-darkvoid)解决了部分Type-C设备的热插拔问题：[IOElectrify](https://github.com/the-darkvoid/macOS-IOElectrify)
* [hackintosh-stuff](https://github.com/hackintosh-stuff)给出了相应声卡（ALC256）对应外置麦克风的解决方案：[combojack](https://github.com/hackintosh-stuff/ComboJack)
* [blankmac](https://github.com/blankmac)给出了触摸板支持多首饰的驱动：[AlpsT4USB](https://github.com/blankmac/AlpsT4USB).
* 所有为这个EFI和黑苹果做出贡献的人

