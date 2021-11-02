# Changelog / 更新日志

## V0.7.5.0

### 发布时间： 2021.11.2

#### 添加功能 :
1. 更新OC版本至0.7.5并更新了驱动

#### 文件变化 :

1. 整个EFI文件夹以适配OC0.7.5
2. 更新官方编译的驱动：

| Kexts          | Version                        | Updated Time       | Updated Way              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AppleALC	|	1.6.6	|	2021-11-01	|	官方编译	|
|	BlueToolFixup	|	2.6.1	|	2021-11-01	|	官方编译	|
|	BrcmBluetoothInjector	|	2.6.1	|	2021-11-01	|	官方编译	|
|	BrcmFirmwareData	|	2.6.1	|	2021-11-01	|	官方编译	|
|	BrcmPatchRAM3	|	2.6.1	|	2021-11-01	|	官方编译	|
|	HibernationFixup	|	1.4.5	|	2021-11-01	|	官方编译	|
|	Lilu	|	1.5.7	|	2021-11-01	|	官方编译	|
|	Voodoo PS/2 Controller	|	2.2.7	|	2021-11-01	|	官方编译	|
|	WhateverGreen	|	1.5.5	|	2021-11-01	|	官方编译	|

-------------------------------------

## V0.7.4.3

### 发布时间： 2021.10.30

#### 添加的功能:
1. 完全支持``Thunderbult 3`` / ``Type-C ``端口 

#### 文件变化:

1. 添加了 ``TbtForcePower.efi``
2. 删除了 ``ACPI/SSDT-THUNDERBOLT`` 和 ``Kexts/IOElectrify.kext``
3. 将 ``USBMap.kext`` 替换为 ``USBPorts.kext``
4. 编辑了 ``config.plist`` 和 ``config-Intel-wirelss-card``

-----------------------------------------------------

## V0.7.4.2

#### 添加的功能:
1. 删除``config.plist``中无用的条目
2. 清理了OC引导主题文件夹
3. 添加了``Linux``引导(支持``Ext4`` / ``Btrfs``)
4. 添加了个性化的引导图标

#### 文件变化:

1. 添加了 ``btrfs_x64.efi`` 和 ``ext4_x64.efi``
2. 删除了 ``Resources/image/blackosx/BsxImacYellow``
3. 编辑了 ``config.plist`` 和 ``config-Intel-wirelss-card``
