/*
 * Created by Henry James
 * https://henryjames.space
 * 
 * Programme to read sensor data and 
 * print to serial for Pi to read, 
 * part of remote sensor project.
 */

#define moisture A0
#define temp A1
#define IR 2

float tempValue;
int moistValue;
float tempC;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(INPUT, IR);
}

void loop() {
  // put your main code here, to run repeatedly:
  moistValue = analogRead(moisture);
  tempValue = analogRead(temp);

  int IR_read = digitalRead(IR);

  // roughly calibrate the analogue input every 2 steps are 

  Serial.println(IR_read);
  delay(1000);
  
}
