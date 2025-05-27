include <HX711.h>
#include <WiFi.h>
#include <WifiUdp.h>

const char* ssid = "";
const char* password = "";
const char* laptopIP = "";
const int port = 6969;

#define DOUT 
#define CLK

float cal_factor = ;

void setup()
{
  Serial.begin(115200);
  scale.begin(DOUT, CLK);
  scale.set_scale(calibration_factor);
  scale.tare();

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.print(".")
  }
  Serial.println("WiFi connected!");
  Serial.println(WiFi.localIP());
}
void loop() 
{
  float weight = scale.get_units(2);
  char buffer[32];
  snprintf(buffer, sizeof(buffer), "%.2f", weight); //decimal (weight) string(buffer) mai convert hora
  
  udp.beginPacket(laptopIP, port);
  udp.print(buffer);
  udp.endPacket();

  delay(200);
}
