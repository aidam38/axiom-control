#include <Arduino.h>

void setup()
{
  Serial.begin(115200);
}

void loop()
{
  Serial.write("HELLO WORLD");
  delay(1000);
}