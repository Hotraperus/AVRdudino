-patmega2560
%~dp0
-PCOM3


avrdudinocmd.bat C:\Users\hotra\AppData\Local\Temp\arduino_build_100951/Prime_numbers.ino.hex -patmega2560 -PCOM3

%~dp0hardware\tools\avr/bin/avrdude -C%~dp0\hardware\tools\avr/etc/avrdude.conf -v %2 -cwiring %3 -b115200 -D -Uflash:w:%1:i 

