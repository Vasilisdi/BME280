#include <Wire.h>
#include <Adafruit_BME280.h>

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme;

void setup() {
  Serial.begin(9600);

  if (!bme.begin()) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
}

void loop() {

  Serial.print(bme.readTemperature());
  Serial.print(" ");
  Serial.print(bme.readPressure() / 100.0F );
  Serial.print(" ");
  Serial.println(bme.readHumidity());
//  int measurements[] = {
//    bme.readTemperature(),bme.readPressure() / 100.0F , bme.readHumidity()
//  };
//  for(int i = 0; i < sizeof(measurements) - 1; i++)
//  {
//    Serial.println(measurements[i]);
//  }

  delay(5000);
}
  
