const int RELAY_PIN = 8;  
void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, HIGH); 
  Serial.begin(9600);            
}
void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();

    if (cmd == '1') {
      digitalWrite(RELAY_PIN, LOW);   
    }
    else if (cmd == '0') {
      digitalWrite(RELAY_PIN, HIGH);  
  }
}
