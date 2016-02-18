#include <RTClib.h>
#include <Wire.h>

char scommand = 0;
char tbuf[10];

RTC_DS3231 RTC;

void setup() {
  Serial.begin(9600);
  while(!Serial) { }
  Wire.begin();
  RTC.begin();
}

void loop() {
  if (Serial.available() > 0) {
    scommand = Serial.read();
    if (scommand == 'w' || scommand == 'W') { 
      Serial.readBytes(tbuf, 10);
      uint32_t t = 0;
      for (int i=0; i < 10; i++) {
        t = (t*10) + (tbuf[i] - '0');
      }
      RTC.adjust(DateTime(t));
      Serial.print("!");
    }

    else if (scommand == 'r' || scommand == 'R') {
      DateTime n = RTC.now();
      uint32_t t = n.unixtime();
      Serial.print(t);
    }

    else {
      Serial.println("x");
    }
  }

}
