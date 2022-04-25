#include <Wire.h>
#include <Adafruit_BME280.h>

#define SEALEVELPRESSURE_HPA (1022.2)
int pin_num = 7;     //pin that controls the slave address


Adafruit_BME280 bme;

void setup() {
  Serial.begin(9600);
  pinMode(pin_num, OUTPUT);  //we use this pin in order to control the slave address
  digitalWrite(pin_num,LOW); //we start with low at the pin 7 corresponding to GND at the SD0 pin
  if (!bme.begin(0x76)) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    //while (1);
  }
}

void loop() {

  bme.begin(0x76);         // here we define the first address 0x76
  digitalWrite(pin_num,LOW);
  
  delay(1000);
  Serial.print(bme.readTemperature());
  Serial.print(" ");
  Serial.print(bme.readPressure() / 100.0F );
  Serial.print(" ");
  Serial.print(bme.readHumidity());
  Serial.print(" ");
  Serial.println(bme.readAltitude(SEALEVELPRESSURE_HPA));
  delay(1000);
  
  bme.begin(0x77);         // here we define the second address 0x77
  digitalWrite(pin_num,HIGH);
  
  delay(1000); 
  Serial.print(bme.readTemperature());
  Serial.print(" ");
  Serial.print(bme.readPressure() / 100.0F );
  Serial.print(" ");
  Serial.print(bme.readHumidity());
  Serial.print(" ");
  Serial.println(bme.readAltitude(SEALEVELPRESSURE_HPA));

  delay(5000);
}
  
