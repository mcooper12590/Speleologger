This library is modified from MrAlvin's (https://github.com/MrAlvin) RTClib
implementation and contains code from the original JeeLab RTClib.

The modifications are entirely trimming of code that is not needed for the
Speleologger, which only uses the DS3231 real time clock. Also trimmed are
much of the DateTime function, as timestamps are logged as UNIX time, and
are converted by the Python datalogger scripts. 

Basic functions  (see examples of how to use):
  .begin
  .adjust
  .isrunning
  .now

DS3231 specific functions:
  .getTemperature
  .getA1Time
  .getA2Time
  .setA1Time
  .setAlarm1Simple
  .setA2Time
  .setAlarm2Simple
  .turnOnAlarm
  .turnOffAlarm
  .checkAlarmEnabled
  .checkIfAlarm
  
  
  
Credits:
---------
- MrAlvin's DS3231 RTClib code https://github.com/MrAlvin

- Code by JeeLabs http://news.jeelabs.org/code/
  Released to the public domain! Enjoy!

-  Merged read/write RAM memory functions from:  
   github.com/dmalec/RTClib   by  MrAlvin 2012-02-27
   
-  Merged DS3231 & DS3234 functions from: 
   github/coobro/RTClib  by  MrAlvin 2012-02-27

       Alarm code for DS3231 (Chronodot) heavily used/modified 
	   from Eric Ayars DS3231 library  by  Coobro
    
	   Eric Ayars code is located at: 
	   http://hacks.ayars.org/2011/04/ds3231-real-time-clock.html

