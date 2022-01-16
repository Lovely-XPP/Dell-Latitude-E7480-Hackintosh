# Changelog / 更新日志

## V0.7.7.0
### Pubilsh date ： 2021.01.16

#### Add Features :
1. Update kexts and OC boot version to 0.7.7

#### Files Changed:

1. All the EFI folder to adapt OC 0.7.7
2. Update kexts with official Release:

| Kexts          | Version                        | Updated Time       | Updated Way              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AirportItlwm	|	2.1.0	|	2021-12-31	|	Official Release	|
|	AppleALC	|	1.6.8	|	2022-01-10	|	Official Release	|
|	FeatureUnlock	|	1.0.5	|	2022-01-10	|	Official Release	|
|	IntelBluetoothFirmware	|	2.1.0	|	2022-01-01	|	Official Release	|
|	IntelBluetoothInjector	|	2.1.0	|	2022-01-01	|	Official Release	|
|	Lilu	|	1.5.9	|	2022-01-10	|	Official Release	|
|	RestrictEvents	|	1.0.6	|	2022-01-10	|	Official Release	|
|	WhateverGreen	|	1.5.6	|	2022-01-10	|	Official Release	|



-----------------------------------------------------


## V0.7.6.0
### Pubilsh date ： 2021.12.10

#### Add Features :
1. Update kexts and OC boot version to 0.7.6

#### Files Changed:

1. All the EFI folder to adapt OC 0.7.6
2. Update kexts with official Release:

| Kexts          | Version                        | Updated Time       | Updated Way              |
|:----------------|:-------------------------------------------|:---------------|:----------------|
|	AirportItlwm-Monterey	|	2.1.0	|	2021-12-10	|	Compile on Local Machine	|
|	AirportItlwm	|	2.1.0	|	2021-12-10	|	Compile on Local Machine	|
|	AppleALC	|	1.6.7	|	2021-12-06	|	Official Release	|
|	FeatureUnlock	|	1.0.4	|	2021-12-06	|	Official Release	|
|	IntelBluetoothFirmware	|	2.1.0	|	2021-12-10	|	Compile on Local Machine	|
|	IntelBluetoothInjector	|	2.1.0	|	2021-12-10	|	Compile on Local Machine	|
|	Lilu	|	1.5.8	|	2021-12-06	|	Official Release	|
|	SMCBatteryManager	|	1.2.8	|	2021-12-06	|	Official Release	|
|	SMCDellSensors	|	1.2.8	|	2021-12-06	|	Official Release	|
|	SMCLightSensor	|	1.2.8	|	2021-12-06	|	Official Release	|
|	SMCProcessor	|	1.2.8	|	2021-12-06	|	Official Release	|
|	SMCSuperIO	|	1.2.8	|	2021-12-06	|	Official Release	|
|	VirtualSMC	|	1.2.8	|	2021-12-06	|	Official Release	|


-----------------------------------------------------

## V0.7.5.0

### Pubilsh date ： 2021.11.2

#### Add Features :
1. Update kexts and OC boot version to 0.7.5

#### Files Changed:

1. All the EFI folder to adapt OC 0.7.5
2. Update kexts with official Release:

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
