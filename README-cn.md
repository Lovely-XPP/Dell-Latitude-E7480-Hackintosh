# 戴尔 Latitude E7480 macOS Big Sur 11 / Monterey 12 (OpenCore引导)

<div style="align: center">
<img src="https://user-images.githubusercontent.com/66028151/153699782-042a7d2a-df92-421c-a940-1c3e62960ae4.png">
</div>


<div style="align: center">
<img src="https://user-images.githubusercontent.com/66028151/145524637-d3c351bd-7ae5-48b5-9f9d-080d97101d1e.png">
</div>

## 语言 / Lanuage
简体中文(当前语言)

[English](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/blob/main/README.md)

## 下载

[![Download from https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases](https://img.shields.io/badge/Download-v0.7.7.0-blue)](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases/download/v0.7.8.0/EFI.zip)

## 更新日志：V0.7.8.0

### 发布时间： 2021.02.12

#### 添加功能 :
1. 更新OC版本至0.7.8并更新了驱动
2. 支持通用控制（需要macOS 12.3，博通网卡，iPad OS 15.4，亲测可用）

#### 文件变化 :

1. 整个EFI文件夹以适配OC 0.7.8
2. 更新官方编译的驱动：

| 驱动名称          | 版本号                       | 更新时间       | 更新方式              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AirportBrcmFixup	|	2.1.4	|	2022-02-08	|	官方编译	|
|	AppleALC	|	1.6.9	|	2022-02-08	|	官方编译	|
|	CpuTscSync	|	1.0.6	|	2022-02-08	|	官方编译	|
|	FeatureUnlock	|	1.0.6	|	2022-02-08	|	官方编译	|
|	Lilu	|	1.6.0	|	2022-02-08	|	官方编译	|
|	RestrictEvents	|	1.0.7	|	2022-02-08	|	官方编译	|
|	WhateverGreen	|	1.5.7	|	2022-02-08	|	官方编译	|

更多版本的更新日志详见 [Changelog_zh.md](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/blob/main/Changelog_zh.md).

## 引导 & 硬件信息

<details>  
<summary><strong>OC引导版本</strong></summary>
</br>
OpenCore 0.7.5 / 0.7.6 / 0.7.7 / 0.7.8
</details>

<details>  
<summary><strong>测试过/支持的系统版本</strong></summary>
</br>
- Big Sur 11.5.0 - 11.5.2</br>
- Big Sur 11.6 - 11.6.1</br>
- Monterey 12.0 - 12.3 beta</br>
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
* Monterey 12.3 （需要博通网卡）和 iPad OS 15.4 开始支持通用控制，亲测可用！
* 强烈建议在进入系统以后使用 [USBMap](https://github.com/corpnewt/USBMap) 工具进行USB定制！
* 如果你进行了硬件更改（比如网卡更换），同样也建议你使用 [USBMap](https://github.com/corpnewt/USBMap) 工具重新进行USB定制！
* 进入系统后，建议重新生成对应机型序列号（需要经过官网查询无效方可使用）！
* 不要开启查找我的Mac功能！
</details>

<details>  
<summary><strong>驱动版本</strong></summary>
</br>

| 驱动名称          | 版本号                       | 更新时间       | 更新方式              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AirportBrcmFixup	|	2.1.4	|	2022-02-08	|	官方编译	|
|	AirportItlwm	|	2.1.0	|	2022-02-10	|	官方编译	|
|	AlpsT4USB	|	1.0.0d1	|	2022-02-10	|	官方编译	|
|	AppleALC	|	1.6.9	|	2022-02-08	|	官方编译	|
|	BlueToolFixup	|	2.6.1	|	2022-02-10	|	官方编译	|
|	BrcmBluetoothInjector	|	2.6.1	|	2022-02-10	|	官方编译	|
|	BrcmFirmwareData	|	2.6.1	|	2022-02-10	|	官方编译	|
|	BrcmPatchRAM3	|	2.6.1	|	2022-02-10	|	官方编译	|
|	BrightnessKeys	|	1.0.3	|	2022-02-10	|	本地编译	|
|	CPUFriend	|	1.2.5	|	2022-02-10	|	本地编译	|
|	CpuTscSync	|	1.0.6	|	2022-02-08	|	官方编译	|
|	ECEnabler	|	1.0.2	|	2022-02-10	|	本地编译	|
|	FeatureUnlock	|	1.0.6	|	2022-02-08	|	官方编译	|
|	HibernationFixup	|	1.4.5	|	2022-02-10	|	官方编译	|
|	IntelBluetoothFirmware	|	2.1.0	|	2022-02-10	|	官方编译	|
|	IntelBluetoothInjector	|	2.1.0	|	2022-02-10	|	官方编译	|
|	IntelMausi	|	1.0.8	|	2022-02-10	|	官方编译	|
|	Lilu	|	1.6.0	|	2022-02-08	|	官方编译	|
|	NVMeFix	|	1.1.0	|	2022-02-10	|	本地编译	|
|	RealtekCardReader	|	0.9.7	|	2022-02-10	|	本地编译	|
|	RealtekCardReaderFriend	|	1.0.0	|	2022-02-10	|	本地编译	|
|	RestrictEvents	|	1.0.7	|	2022-02-08	|	官方编译	|
|	SMCBatteryManager	|	1.2.8	|	2022-02-10	|	官方编译	|
|	SMCDellSensors	|	1.2.8	|	2022-02-10	|	官方编译	|
|	SMCLightSensor	|	1.2.8	|	2022-02-10	|	官方编译	|
|	SMCProcessor	|	1.2.8	|	2022-02-10	|	官方编译	|
|	SMCSuperIO	|	1.2.8	|	2022-02-10	|	官方编译	|
|	USBPorts	|	1.0	|	2022-02-10	|	USB 端口注入	|
|	VerbStub	|	1.0.4	|	2022-02-10	|	官方编译	|
|	VirtualSMC	|	1.2.8	|	2022-02-10	|	官方编译	|
|	Voodoo PS/2 Controller	|	2.2.7	|	2022-02-10	|	官方编译	|
|	VoodooI2C	|	2.6.5	|	2022-02-10	|	官方编译	|
|	VoodooI2CHID	|	1	|	2022-02-10	|	官方编译	|
|	WhateverGreen	|	1.5.7	|	2022-02-08	|	官方编译	|
</details>

## 工作状态

<details>  
<summary><strong>可用功能</strong></summary>
</br>

- [x] 显卡Intel HD 620 Graphics的正常驱动（包含双硬解码、GPU加速）
- [x] 所有的USB端口都正常工作
- [x] HDMI/Type-C 接口支持音频输出并支持热插拔 
- [x] 内置摄像头
- [x] Wifi（2.4GHz/5G）
- [x] 蓝牙
- [x] 关机/ 重启/ 睡眠/ 唤醒 （包含 Fn + insert 键睡眠和合盖睡眠）
- [x] 所有Fn键的功能 （需要关闭bios关于Fn键锁：bios -> POST Behavior -> Fn Lock Options）
- [x] 扬声器和耳机插孔
- [x] 外置麦克风和耳麦 （需要与[combojack](https://github.com/hackintosh-stuff/ComboJack)配合使用）
- [x] Intel 有线网络
- [x] 苹果商店和iCloud账户服务，不要开启查找我的Mac功能！
- [x] (不一定可用，和你的账户也有关系) iMessage 和 Facetime 
- [x] miniDP 和 HDMI （支持音频输入）
- [x] 键盘、触摸屏(触摸屏支持手势)、触摸板（触摸板支持多手势）
- [x] 隔空投送、接力、随航、隔空播放、通用控制（这些功能仅适用于博通网卡，且隔空播放仅限macOS 12，通用控制仅限macOS 12.3及以上）
- [x] SD读卡器

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
* [Acidanthera](https://github.com/Acidanthera) 的 OC 包和主要的驱动
* [daliansky](https://github.com/daliansky) 的很棒的SSDTs在 [OC-little](https://github.com/daliansky/OC-little)
* [Dortania](https://dortania.github.io/)的OC安装教程
* [the-darkvoid](https://github.com/the-darkvoid) 解决了部分Type-C设备的热插拔问题在 [IOElectrify](https://github.com/the-darkvoid/macOS-IOElectrify)
* [hackintosh-stuff](https://github.com/hackintosh-stuff) 给出了相应声卡（ALC256）对应外置麦克风的解决方案在 [combojack](https://github.com/hackintosh-stuff/ComboJack)
* [blankmac](https://github.com/blankmac) 给出了触摸板支持多手势的驱动在 [AlpsT4USB](https://github.com/blankmac/AlpsT4USB).
* [0xFireWolf](https://github.com/0xFireWolf) 提供了原生化SD读卡器的驱动在 [RealtekCardReader](https://github.com/0xFireWolf/RealtekCardReader) 和 [RealtekCardReaderFriend](https://github.com/0xFireWolf/RealtekCardReaderFriend)
* 所有为这个EFI和黑苹果做出贡献的成员

