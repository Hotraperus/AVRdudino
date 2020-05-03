%~dp0avrdude -C%~dp0avrdude.conf -v %2 -cwiring %3 -b115200 -D -Uflash:w:%1:i 
exit