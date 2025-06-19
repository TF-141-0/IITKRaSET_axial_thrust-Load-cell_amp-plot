#include <WiFi.h>
#include <WiFiUdp.h>
#include "HX711.h"


const char* ssid     = "GSS-2";
const char* password = "esp32www";

const char* laptopIP = "192.168.137.1";
const int port = 9500;  

WiFiUDP udp;

#define DT 18
#define SCK 19
HX711 scale;

float calibration_factor = 8.47;  

void setup() {
  Serial.begin(115200);

  scale.begin(DT, SCK);
  scale.set_scale(calibration_factor);
  scale.tare();  

  WiFi.begin(ssid, password);
  Serial.print("Connecting to Wi-Fi"); //Dbt
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWi-Fi connected.");
  Serial.print("ESP32 IP: ");
  Serial.println(WiFi.localIP());
  Serial.print("Sending to Laptop IP: ");
  Serial.println(laptopIP);
}

void loop()
{
  static unsigned long last_time = 0;
  unsigned long now = millis();

  if (now - last_time >= 12) {  // every 12.5 ms
    last_time = now;

    if (scale.is_ready()) {
      float wei = scale.get_units(1);  
      float Thrust = wei / 100;
      if (abs(Thrust) < 0.05) Thrust = 0;

      char buffer[32];
      snprintf(buffer, sizeof(buffer), "%.2f", Thrust);
      udp.beginPacket(laptopIP, port);
      udp.print(buffer);
      udp.endPacket();

      Serial.println(Thrust);
    }
  }
}

