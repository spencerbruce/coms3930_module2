#include <math.h>

int xyzPins[] = {12, 13, 14};
int greenButton = 25;
int blueButton = 26;
int binary_switch = 15;

void setup() {
  Serial.begin(9600);
  pinMode(xyzPins[2], INPUT_PULLUP);
  pinMode(greenButton, INPUT);
  pinMode(blueButton, INPUT);
  pinMode(binary_switch, INPUT_PULLUP);
}

void loop() {
  int xVal = analogRead(xyzPins[0]);
  int yVal = analogRead(xyzPins[1]);
  int zVal = analogRead(xyzPins[2]);
  int s = analogRead(binary_switch);
  char swit[] = "_";
  char green[] = "_";
  char blue[] = "_";
  if (s < 4090)
    swit[0] = 'S';
  if (digitalRead(greenButton) == LOW) 
    green[0] = 'G';
  if (digitalRead(blueButton) == LOW) 
    blue[0] = 'B';
//  printdetailed(green,blue,xVal,yVal,zVal,swit);
  printnormal(green,blue,xVal,yVal,zVal,swit);
}

float normalize(int x){
  if (x >= 1300 && x <= 2200) 
    return 0;
  if (x < 1820)
    return -1*(1820 - x);
  return (x - 1820);
}

int correct(float x) {
  if (x < 0)
    return (360-((int)(x + 360 + 180)%360))%360;
  else
    return (360-((int)(x + 180))%360)%360;
}

void  printdetailed(char* green, char* blue, int xVal, int yVal, int zVal, char* swit) {
  Serial.print("θ: ");
  if (normalize(yVal) == 0 && normalize(xVal) == 0) 
    Serial.print('_');
  else
    Serial.print(correct(atan2(normalize(yVal), normalize(xVal))* (180.0 / M_PI)));
  Serial.print(" X:");
  Serial.print(xVal);
  Serial.print(" Xn:");
  Serial.print(normalize(xVal));
  Serial.print(" Y:");
  Serial.print(yVal);
  Serial.print(" Yn:");
  Serial.print(normalize(yVal));
  Serial.print(" Z:");
  if (zVal == 0)
    Serial.print("Z");
  else
    Serial.print('_');
  Serial.print(" ");
  Serial.print(blue[0]);
  Serial.print(green[0]);
  Serial.print(swit[0]);
  Serial.print('\n');
  delay(100);
}

void  printnormal(char* green, char* blue, int xVal, int yVal, int zVal, char* swit) {
  if (normalize(yVal) == 0 && normalize(xVal) == 0) 
    Serial.print('_');
  else
    Serial.print(correct(atan2(normalize(yVal), normalize(xVal))* (180.0 / M_PI)));
  Serial.print('\t');
  if (zVal == 0)
    Serial.print("Z");
  else
    Serial.print('_');
  Serial.print("\t");
  Serial.print(blue[0]);
  Serial.print("\t");
  Serial.print(green[0]);
  Serial.print("\t");
  Serial.print(swit[0]);
  Serial.print('\n');
  delay(100);
}
