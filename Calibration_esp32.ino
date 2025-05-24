#include "HX711.h"

#define DT 18 
#define SCK 19 

HX711 scale;

float calibration_factor = 1.0; 

void setup() {
  Serial.begin(115200);
  scale.begin(DT, SCK);           // Initialization
  scale.set_scale(calibration_factor);  
  scale.tare();                   // Tare to 0
}

void loop() {
  if (scale.is_ready()) {
    float weight = scale.get_units(2); 
    if (abs(weight) < 0.05) weight = 0;   // threshold small drift
    Serial.println(weight);
  }
  delay(200);
}
