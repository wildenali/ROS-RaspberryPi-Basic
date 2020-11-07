#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

const int INbPin1 = D2;
const int INaPin1 = D1;
const int INaPin2 = D4;
const int INbPin2 = D3;

//4321
//psrb esp
//17 18 19 20
//rbps driver

WiFiUDP Udp;

const char* ssid = "101 residence_fm";
const char* password = "101littleangel";
unsigned int localPort = 8888;
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];

void setup() {
  pinMode(INaPin1, OUTPUT);
  pinMode(INbPin1, OUTPUT);
  pinMode(INaPin2, OUTPUT);
  pinMode(INaPin2, OUTPUT);
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(500);
  }
  Serial.print("\nConnected! IP address: ");
  Serial.println(WiFi.localIP());
  Serial.printf("UDP serer on port %d\n", localPort);
  Udp.begin(localPort);
}

void loop() {
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    Serial.print("Received packet of size ");
    Serial.println(packetSize);
    Serial.print("From ");
    IPAddress remote  = Udp.remoteIP();
    for(int i=0; i<4; i++){
      Serial.print(remote[i], DEC);
      if(i<3) {Serial.print(".");}
    }

    Serial.print(", port ");
    Serial.println(Udp.remotePort());

    // read the packet into packetBuffer
    Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
    Serial.println("Contents: ");
    String directions = "";
    for(int i=0; i<=UDP_TX_PACKET_MAX_SIZE; i++){
      if(packetBuffer[i] == '*'){
        move_bot(directions);
        break;
      }
      directions += packetBuffer[i];
    }
  }
  delay(10);
}

void move_bot(String a){
  int commaIndex = a.indexOf(',');
  int secondCommaIndex = a.indexOf(',', commaIndex + 1);
  String firstValue = a.substring(0, commaIndex);
  String secondValue = a.substring(commaIndex + 1, secondCommaIndex);
  int linear = firstValue.toInt();
  int angular = secondValue.toInt();
  
  Serial.print("Linear: ");     Serial.println(linear);
  Serial.print("Angular: ");    Serial.println(angular);
  Serial.println("-------------------------------------");

  if(linear > 0 && angular == 0){
    // Forward
    Serial.println("FORWARD");
    digitalWrite(INaPin1, HIGH);
    digitalWrite(INaPin2, HIGH);
    digitalWrite(INbPin1, LOW);
    digitalWrite(INbPin2, LOW);
    delay(2000);
    stop();
  }
  else if(linear < 0 && angular == 0){
    // Reverse
    Serial.println("REVERSE");
    digitalWrite(INaPin1, LOW);
    digitalWrite(INaPin2, LOW);
    digitalWrite(INbPin1, HIGH);
    digitalWrite(INbPin2, HIGH);
    delay(2000);
    stop();
  }
  else if(linear == 0 && angular > 0){
    // Left
    Serial.println("LEFT");
    digitalWrite(INaPin1, HIGH);
    digitalWrite(INaPin2, LOW);
    digitalWrite(INbPin1, LOW);
    digitalWrite(INbPin2, HIGH);
    delay(2000);
    stop();
  }
  else if(linear == 0 && angular < 0){
    // Right
    Serial.println("RIGHT");
    digitalWrite(INaPin1, LOW);
    digitalWrite(INaPin2, HIGH);
    digitalWrite(INbPin1, HIGH);
    digitalWrite(INbPin2, LOW);
    delay(2000);
    stop();
  }
  else{
    stop();
  }
}

void stop(){
    // STOP
  digitalWrite(INaPin1, LOW);
  digitalWrite(INaPin2, LOW);
  digitalWrite(INbPin1, LOW);
  digitalWrite(INbPin2, LOW);
}
