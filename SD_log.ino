#include <SPI.h>
#include <SD.h>
#include "HX711.h"

#define DOUT 
#define CLK 
#define SD_CS 5  // Chip pin for SD card module

HX711 scale;
File logFile;
float calib_factor = ;

void setup() {
  Serial.begin(115200);
  scale.begin(DOUT, CLK);
  scale.set_scale(calib_factor);
  scale.tare();

  if (!SD.begin(SD_CS)) {
    Serial.println("SD card initialization failed!");
    while (1);
  }
  Serial.println("SD card ready.");

  // Open file for appending
  logFile = SD.open("/weights.csv", FILE_WRITE);
  if (logFile) {
    logFile.println("Time(ms),Weight(kg)");
    logFile.close();
  } else {
    Serial.println("Failed to open file!");
  }
}

void loop() {
  float weight = scale.get_units(5);
  unsigned long t = millis();

  logFile = SD.open("/weights.csv", FILE_WRITE);
  if (logFile) {
    logFile.print(t);
    logFile.print(",");
    logFile.println(weight, 2); // 2 decimal places
    logFile.close();
    Serial.println("Logged: " + String(weight));
  } else {
    Serial.println("File open failed.");
  }

  delay(100); 
}
