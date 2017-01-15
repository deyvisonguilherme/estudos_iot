const int LED = 13;

void setup() {
  Serial.begin(9600);
  pinMode(LED,OUTPUT);
}
 
void loop() {
   if (Serial.available()){
    switch(Serial.read()){
      case '0':
        digitalWrite(LED,LOW);
      break;
      case '1':
        digitalWrite(LED,HIGH);
      break;
    }
  }
}
