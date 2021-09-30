
#include <Servo.h>

// setup function to initialize hardware and software
int sensorPin = A0; // analog pin used to connect the sharp sensor
int sensorValue = 0;// variable to store the values from s
int panPos = 0; // inital value of the pan angle
int tiltPos = 0; // intital value of tilt angle

void setup(){
  panServo.attach(9);  // attaches the servo on pin 9 to the servo object
  tiltServo.attach(10); // attaches servo on pin 10 
  // start the serial port
  int long baudRate = 9600;    // NOTE1: The baudRate for sending & receiving programs must match
  Serial.begin(baudRate);     // NOTE2: Set the baudRate to 115200 for faster communication
}

void loop() 
{  
  SensorValue = analogRead(sensorPin); // reading the value from the sensor
  Serial.println(SensorValue); // printing the value to serial prot
  delay(500); // a delay so that there is not too much data

  // pans across the letter and for every angle, the tilt servo scans the letter from top to bottom in order to get a full 
  // scan of the letter.
  for (panPos = 75; panPos <= 115; panPos += 3) { 
    panServo.write(panPos);  // tell servo to go to position in variable 'panPos'
    for (tiltPos = 70; tiltPos <= 120; tiltPos += 3){ 
      tiltServo.write(tiltPos); //tell tilt servo to go to position in variable 'panPos'
      SensorValue = analogRead(sensorPin); // read the sensor value
      Serial.print(panPos);  // prints the pan angle
      Serial.print(" ");         // prints a space
      Serial.print(tiltPos);         // prints tilt angle
      Serial.print(" ");         // prints a space
      Serial.println(SensorValue); // prints the sensor value
    }
  }
  
}
