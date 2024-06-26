@echo off
echo ディスク容量をチェックしています...

:: チェックするディスクドライブを指定
set drive=C:

:: ディスク容量の表示
wmic logicaldisk where "DeviceID='%drive%'" get DeviceID,FreeSpace,Size

pause
