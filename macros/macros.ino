int buttonState1 = 500;
int buttonState2 = 500;
boolean doublecheck = false;

void setup() {
  Serial.begin(9600);
  pinMode(A1,INPUT);
  pinMode(A0,INPUT);
}

void loop() {
  buttonState1 = analogRead(A0);
  buttonState2 = analogRead(A1);

  if (buttonState1 == 0) {
    Serial.println(1);
    doublecheck = true;
  } else if(buttonState1 == 1023) {
    Serial.println(2);
    doublecheck = true;
  } else if (buttonState2 == 0) {
    Serial.println(3);
    doublecheck = true;
  } else if(buttonState2 == 1023) {
    Serial.println(4);
    doublecheck = true;
  } else if((buttonState1 > 0 & buttonState1 < 450) | (buttonState1 > 600 & buttonState1 < 1023) | (buttonState2 > 0 & buttonState2 < 450) | (buttonState2 > 600 & buttonState2 < 1023)) {
    Serial.println(0);
  } else if(doublecheck){
    Serial.println(0);
    doublecheck = false;
  }
  
  delay(100);
}
