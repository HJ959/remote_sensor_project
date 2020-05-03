/*
 * Created by Henry James
 * https://henryjames.space
 * 
 * Programme to read sensor data and 
 * print to serial for Pi to read, 
 * part of remote sensor project.
 */

#define moisture A0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorValue = analogRead(moisture);

  Serial.println(sensorValue);
  delay(1000);
  
}
