/*
 * Created by Henry James
 * https://henryjames.space
 * 
 * Programme to read sensor data and 
 * print to serial for Pi to read, 
 * part of remote sensor project.
 */
////////////////////////////////////////////////////////////////////
#define temp A0
#define moisture A1
////////////////////////////////////////////////////////////////////
int moistValue;
int  Kelvin, Celsius;
////////////////////////////////////////////////////////////////////
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(temp, INPUT);
  pinMode(moisture, INPUT);
}
////////////////////////////////////////////////////////////////////
void loop() {
  delay(1000);

  // Read analog voltage and convert it to Kelvin (0.489 = 500/1023)
  Kelvin = analogRead(temp) * 0.489;  
  
  // Convert Kelvin to degree Celsius  
  Celsius = Kelvin - 273;               
  
  if (Celsius < 0) {
    // Absolute value
    Celsius = abs(Celsius);     
  }

  moistValue = analogRead(moisture);

  Serial.print("Temp: ");
  Serial.print(Celsius);
  Serial.print(", Moisture: ");
  Serial.println(moistValue);
}
////////////////////////////////////////////////////////////////////
