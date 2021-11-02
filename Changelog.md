# Changelog / 更新日志

## V0.7.5.0

### Pubilsh date ： 2021.11.2

#### Add Features :
1. update kexts and OC boot version to 0.7.5

#### Files Changed:

1. All the EFI folder to adapt OC 0.7.5
2. update kexts with offical Release:

| Kexts          | Version                        | Updated Time       | Updated Way              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AppleALC	|	1.6.6	|	2021-11-01	|	Official Release	|
|	BlueToolFixup	|	2.6.1	|	2021-11-01	|	Official Release	|
|	BrcmBluetoothInjector	|	2.6.1	|	2021-11-01	|	Official Release	|
|	BrcmFirmwareData	|	2.6.1	|	2021-11-01	|	Official Release	|
|	BrcmPatchRAM3	|	2.6.1	|	2021-11-01	|	Official Release	|
|	HibernationFixup	|	1.4.5	|	2021-11-01	|	Official Release	|
|	Lilu	|	1.5.7	|	2021-11-01	|	Official Release	|
|	Voodoo PS/2 Controller	|	2.2.7	|	2021-11-01	|	Official Release	|
|	WhateverGreen	|	1.5.5	|	2021-11-01	|	Official Release	|

-----------------------------------------------------

## V0.7.4.3

### Pubilsh date ： 2021.10.30

#### Add Features :
1. ``Thunderbult 3`` / ``Type-C`` port fully supported

#### Files Changed:

1. Add ``TbtForcePower.efi``
2. Delete ``ACPI/SSDT-THUNDERBOLT`` and ``Kexts/IOElectrify.kext``
3. Replace ``USBMap.kext`` with ``USBPorts.kext``
4. Edit ``config.plist`` and ``config-Intel-wirelss-card``

-----------------------------------------------------


## V0.7.4.2

### Pubilsh date ： 2021.10.29

#### Add Features :
1. Delete the useless entries in ``config.plist``
2. Clean Resource folder
3. Add Linux boot support (Ext4 / Btrfs)
4. Add startup UI icons

#### Files Changed:

1. Add ``btrfs_x64.efi`` and ``ext4_x64.efi``
2. Delete ``Resources/image/blackosx/BsxImacYellow``
3. Edit ``config.plist`` and ``config-Intel-wirelss-card``
