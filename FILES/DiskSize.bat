@echo off
echo �f�B�X�N�e�ʂ��`�F�b�N���Ă��܂�...

:: �`�F�b�N����f�B�X�N�h���C�u���w��
set drive=C:

:: �f�B�X�N�e�ʂ̕\��
wmic logicaldisk where "DeviceID='%drive%'" get DeviceID,FreeSpace,Size

pause
