
//      ******************************************************************
//      *                                                                *
//      *                                                                *
//      *     Example Arduino program that transmits data to a laptop    *
//      *                                                                *
//      *                                                                *
//      ******************************************************************


#include <Servo.h>

//
// setup function to initialize hardware and software
int sensorPin = A0;          // analog pin used to connect the sharp sensor
int sensorValue = 0;                 // variable to store the values from s
int panPos = 0; 
int avgSensorValue = 0;
int tiltPos = 0;

void setup(){
//  panServo.attach(9);  // attaches the servo on pin 9 to the servo object
//  tiltServo.attach(10);
  // start the serial port
  int long baudRate = 9600;    // NOTE1: The baudRate for sending & receiving programs must match
  Serial.begin(baudRate);     // NOTE2: Set the baudRate to 115200 for faster communication
}
// pan:75-115, tilt 70-120
void loop() 
{  
  avgSensorValue = analogRead(sensorPin);
  Serial.println(avgSensorValue); 
  delay(500);

//  for (panPos = 75; panPos <= 115; panPos += 3) { // goes from 0 degrees to 180 degrees    
//    panServo.write(panPos);  // tell servo to go to position in variable 'pos'
//    for (tiltPos = 70; tiltPos <= 120; tiltPos += 3){ 
//      tiltServo.write(tiltPos);
//      delay(1000);
////      for (int i = 0; i <=10; i += 1){
////        sensorValue = sensorValue + analogRead(sensorPin); // reads the value of the sharp sensor
////      }
//      avgSensorValue = analogRead(sensorPin);
//      Serial.print(panPos);  // prints a label
//      Serial.print(" ");         // prints a space
//      Serial.print(tiltPos);         // prints a space
//      Serial.print(" ");         // prints a space
//      Serial.println(avgSensorValue);  
//      // delay after sending data so the serial connection is not over run
//    }
//  }
  
}
