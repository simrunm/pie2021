#include <Servo.h>

//
// setup function to initialize hardware and software
int sensorPin = A0;          // analog pin used to connect the sharp sensor
int sensorValue = 0;                 // variable to store the values from s

Servo tiltServo;
Servo panServo;
int panPos = 0; 
int avgSensorValue = 0;
int tiltPos = 0;

void setup(){
  tiltServo.attach(10);
  panServo.attach(9);
  // start the serial port
  int long baudRate = 9600;    // NOTE1: The baudRate for sending & receiving programs must match
  Serial.begin(baudRate);     // NOTE2: Set the baudRate to 115200 for faster communication
}
// pan:start at 75
void loop() 

{  
  panServo.write(115);
//    for (tiltPos = 70; tiltPos <= 120; tiltPos += 2){ 
//      tiltServo.write(tiltPos);
//      delay(1000);
//      avgSensorValue = analogRead(sensorPin);
//      Serial.print(panPos);  // prints a label
//      Serial.print(" ");         // prints a space
//      Serial.print(tiltPos);         // prints a space
//      Serial.print(" ");         // prints a space
//      Serial.println(avgSensorValue);  
//  }
}
  
