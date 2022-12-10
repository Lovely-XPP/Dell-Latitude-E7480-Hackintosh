# 戴尔 Latitude E7480 macOS 11 ~ 13(Beta) (OpenCore引导)

## 简介

> 提示: 由于我购入了一台MacBookPro, 所以我不能手动更新这个仓库。因此，我写了一个自动化更新脚本来更新这个仓库。如果你遇到了一些错误或问题，欢迎开一个issue，我会尽可能地解决。感谢大家一直以来的支持。

<div style="align: center">
<img src="https://raw.githubusercontent.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/macOS-13/demo/system_info.png">
</div>

<div style="align: center">
<img src="https://raw.githubusercontent.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/main/demo/OC_info.png">
</div>


## 语言 / Lanuage

简体中文(当前语言)

[English](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/blob/main/README.md)


## 计划
- [x] 添加自动化脚本升级OpenCore和对应的驱动文件
- [x] 添加自动化脚本自动更新README和Changelog说明文件



## 提示

1. 如果遇到雷电设备不支持热插拔（经过@krzysinek测试，***macOS Ventura 13以下请勾选***），请尝试 ***勾选*** `UEFI->Drivers->TbTPowerForce.efi`.
2. 如果使用USB安装macOS卡代码，请尝试 ***勾选*** `UEFI->Quirks->ReleaseUsbOwnership`，感谢@krzysinek (#22).
3. 对于苹果 macOS 12 Monterey, DW1820A网卡兼容性不那么好，主要是蓝牙驱动，导致隔空投送、接力等服务无法使用，于是换了张BCM9460Z4的网卡，目前无任何不兼容的问题！
4. Monterey 12.3 （需要博通网卡）和 iPad OS 15.4 开始支持通用控制，亲测可用！
5. 强烈建议在进入系统以后使用 [USBMap](https://github.com/corpnewt/USBMap) 工具进行USB定制！
6. 如果你进行了硬件更改（比如网卡更换），同样也建议你使用 [USBMap](https://github.com/corpnewt/USBMap) 工具重新进行USB定制！
7. 进入系统后，建议重新生成对应机型序列号（需要经过官网查询无效方可使用）！
8. 不要开启查找我的Mac功能！


## 下载
[![Download from https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases](https://img.shields.io/badge/Download-v0.8.7.0-blue)](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/releases/tag/v0.8.7.0)

## 更新日志: V0.8.7.0

### 发布时间 : 2022.12.08

#### 添加功能 :

1. 更新OC版本至0.8.7并更新了驱动
1. 降级`AlpsHID.kext`以有更稳定的触摸板体验，感谢@RJJvW (#21) 和 @H3xidecimal (#18)

#### 文件变化 :

1. 更新整个EFI文件夹以适配 OC 0.8.7
2. 更新驱动:

| 驱动名称          | 版本号                       | 更新时间       | 更新方式              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AlpsHID	|	1.0.0d1	|	2022-11-21	|	本地编译	|
|	AppleALC	|	1.7.8	|	2022-12-08	|	官方编译	|
|	FeatureUnlock	|	1.1.2	|	2022-12-08	|	官方编译	|
|	HibernationFixup	|	1.4.8	|	2022-12-08	|	官方编译	|
|	IntelBluetoothFirmware	|	2.3.0	|	2022-12-08	|	官方编译	|
|	IntelBluetoothInjector	|	2.3.0	|	2022-12-08	|	官方编译	|
|	Voodoo PS/2 Controller	|	2.3.3	|	2022-12-08	|	官方编译	|
|	WhateverGreen	|	1.6.3	|	2022-12-08	|	官方编译	|


更多版本的更新日志详见 [Changelog_zh.md](https://github.com/Lovely-XPP/Dell-Latitude-E7480-Hackintosh/blob/main/Changelog_zh.md).

## 引导 & 硬件信息

<details>  
<summary><strong>OC引导版本</strong></summary>
</br>
OpenCore  0.8.0 / 0.8.1 / 0.8.2 / 0.8.3 / 0.8.4 / 0.8.5 / 0.8.6 / 0.8.7
</details>
<details>  
<summary><strong>测试过/支持的系统版本</strong></summary>
</br>
- Big Sur 11.0 - 11.7</br>
- Monterey 12.0 - 12.5.1 beta</br>
- Ventura 13.0 beta（我正在使用）</br>
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


</details>

<details>  
<summary><strong>驱动版本</strong></summary>
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

- [ ] 雷电3热拔插

</details>



## 推荐 Bios 设置

打开以下项目：

1. `System Configuration` -> `Integrated NIC` -> `Enabled`

   但是不要勾选:

   - [ ] `Enable UEFI NetWork`

2. `System Configuration` -> `SATA Operation` -> `AHCI`

3. `System Configuration` -> `Thunderbolt Adapter Configuration` -> 打开所有项目并选择 

   `Security level - No security`



关闭以下项目：

1. `Secure Boot` -> `Secure Boot Enable` -> `Disabled`
2. `Intel Software Guard Extension` -> `Intel SGX Enable` -> `Disabled`



## 核显输出4K显示器方法说明

这个部分引用自 [Lorys89-DELL_LATITUDE_7280](https://github.com/Lorys89/DELL_LATITUDE_7280).

1. 打开`config.plist`，在`DeviceProperties`, `PciRoot(0x0)/Pci(0x2,0x0)`中删除 `framebuffer-fbmem` 和 `framebuffer-stolenmem`项


2. 重启电脑，显示 opencore 引导界面后，选择 `modGRUBShell.efi`


3. 将 DVMT PRE 设置为 64 MB

``setup_var 0x795 0x2``

![DMT-PRE](https://raw.githubusercontent.com/Lorys89/DELL_LATITUDE_7280/main/Screenshot/DVMT-PRE.png)


4. 将 DVMT Total GFX Mem 设置为最大值

``setup_var 0x796 0x3``

![DMT-PRE](https://raw.githubusercontent.com/Lorys89/DELL_LATITUDE_7280/main/Screenshot/DVMT-TOT.png)


## 雷电3使用说明

Type-C 口有两个控制器：雷电3控制器和USB控制器。USB控制器已经完全支持（包括热插拔），而雷电3接口仅能在开机时候进行识别，但并不能实现热插拔。如果你需要使用雷电3，请注意一下2点：

- 在启动电脑之前请插入雷电3设备（如果已经启动请关机插入后再开机）
- **不支持**热插拔

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
* [Lorys89](https://github.com/Lorys89) 提供了 DVMT 修改方法以实现4K外接显示器输出在[Lorys89-DELL_LATITUDE_7280](https://github.com/Lorys89/DELL_LATITUDE_7280).
* 所有为这个EFI和黑苹果做出贡献的成员

