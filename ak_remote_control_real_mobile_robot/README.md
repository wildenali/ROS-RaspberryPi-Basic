# Remote Control Real Mobile Robot

Exercise how to control the mobile robot with WiFi UDP protocol 
- Mobile Robot
- Arduino
- Electrical Wiring Diagram
- Mechanical Assembly
- Using teleop node to control the mobile robot

References:
- ROS Ultimate Guide to Beginners Guide Hands ON! from Muhammad Luqman Udemy Channel

## Create a Main file
1. Creata a main file called `remote_control.py`
	- `$ cd src`
	- `$ touch remote_control.py`
	- `$ chmod +x remote_control.py`	change the permissions
2. Edit the `remote_control.py` file like below
	```sh
	#!/usr/bin/env python
	# license removed for brevity

	import rospy
	from std_msgs.msg import String
	from geometry_msgs.msg import Twist
	import socket

	message = "0"

	class driver:
		def __init__(self):
			# init ros
			rospy.init_node('car_driver', anonymous=True)
			rospy.Subscriber('/cmd_vel', Twist, self.get_cmd_vel)
			self.get_arduino_message()
		
		# get cmd_vel message, and get linear velocity and angular velocity
		def get_cmd_vel(self, data):
			linear = data.linear.x
			rotation = data.angular.z
			self.send_cmd_to_arduino(int(linear), int(rotation))
			
		# translate x, and angular velocity to PWM signal of each wheels and send to arduino
		def send_cmd_to_arduino(self, linear, rotation):
			global message
			message = "{},{},*".format(linear,rotation)
			print("Linear", linear, "----", "Angular", rotation)
			
			# send by serial
			sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
		
		# receive serial text from arduino and publish it to '/arduino' message
		def get_arduino_message(self):
			global message
			print("MESSAGE", message)
			pub = rospy.Publisher('arduino', String, queue_size=10)
			r = rospy.Rate(10)
			while not rospy.is_shutdown():
				pub.publish(message)
				r.sleep()

	if __name__ == '__main__':
		UDP_IP = "192.168.0.22"		# esp866 ip and port
		UDP_PORT = 8888
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		
		try:
			driver()
		except rospy.ROSInterruptException:
			pass
	```
3. Make sure the python script get installed properly and use the right python interpreter
	- Open CMakelists.txt
	- Uncomment and edit the line of code like below
		```sh
		catkin_install_python(PROGRAMS
			src/remote_control.py
			DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
		)
		```
4. Build the node
	- `$ cd ~/catkin_ws/`
	- `$ catkin_make`
5. Run the node
	- `$ cd ~/catkin_ws/`
	- `$ roscore`
	- Open a new tab and type `$ rosrun ak_remote_control_real_mobile_robot remote_control.py`
	- Close the all terminal to stop it

## Install teleop_twist_keyboard
`sudo apt-get install ros-kinetic-teleop-twist-keyboard`

## Create a Arduino file to receive a message and move the robot
1. Create a arduino file called `control_robot.ino`
2. Edit the `control_robot.ino` file like following below
	```sh
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
	```
3. Upload the file to esp8266 (nodemcu or wemos)
4. Assembly the robot
5. Turn on the robot

## Running the Project
	- `$ cd ~/catkin_ws/`
	- `$ roscore`
	- Open a new tab and type `$ rosrun ak_remote_control_real_mobile_robot remote_control.py`
	- Open a new tab and type `$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py`
	- On the teleop terminal try to push button i or j or l or m, see what happen to the robot
