<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="artwork/sfootball.png" alt="Project logo"></a>
</p>

<h3 align="center">SmartFootball</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()


</div>

---


<p align="center"> SmartFootball
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Prerequisites](#deployment)
- [Installation and Config](#Installation_and_Config)
- [Test](#test)
- [Circuit](#circuit)
- [Dashboard](#dashboard)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

This repo contains circuit, firmware and backend for SmartFootball Project.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites <a name = "Prerequisites"></a>

What things you need to install the software and how to install them.

```
- Raspberry Pi Model 3B, 3B+, 4B or CM4
```

## Installation and Configuration <a name = "Installation_and_Config"></a>

A step by step series that covers how to get the Firmware running.

### Raspberry Pi Firmware Pre-Reqs

1.  Download and install the latest Raspberry Pi OS Desktop image to your SD card
2.  Open the terminal and execute the following command
    ```sudo raspi-config```
3. Then follow the following pictures to enable I2C bus on you raspberry pi

* ![R1](artwork/r1.png)
* ![R2](artwork/r2.png)
* ![R3](artwork/r3.png)
* ![R4](artwork/r4.png)
* ![R5](artwork/r5.png)

* Then do the same for Serial(UART)

* ![R2](artwork/r2_2.jpg)

* And same for SPI, SSH and Camera

### Configuring Raspberry Pi and Running the UI
  1.  Copy FirmwareRPi folder to the desktop of your Raspberry Pi, open the terminal of your Raspberry Pi and execute the following commands

```bash
  - sudo apt-get update
  - sudo apt-get upgrade
  - sudo apt install python3-pip
  - pip3 install paho-mqtt
  - pip3 install imusensor
  - sudo adduser $USER dialout
  - sudo cp imuSrv.service /lib/systemd/system/
  - {TCP Tunnel}
  - sudo apt-get install motion
```
After the installation is complete, type in the command `sudo nano /etc/motion/motion.conf` and press enter.

Then you have to change some settings in the `.conf` file. It might be difficult sometimes to find the settings but use 'ctrl + w' to find it. So follow the steps:

1.  Make sure 'daemon' is ON.
2.  Set 'framerate' anywhere in between 1000 to 1500.
3.  Keep 'Stream_port' to 8081.
4.  'Stream_quality' should be 100.
5.  Change 'Stream_localhost' to OFF.
6.  Change 'webcontrol_localhost' to OFF.
7.  Set 'quality' to 100.
8.  Set 'width' & 'height' to 640 & 480.
9.  Set 'post_capture' to 5.
10. Press ctrl + x to exit. Type y to save and enter to confirm.
11. Again type in the command `sudo nano /etc/default/motion` and press enter.

12. Set ' start_motion_daemon ' to yes. Save and exit.

Then do:

`sudo service motion restart`
`sudo motion` 

Once done, import `flows.json` to the nodered, form `dashboard` folder.
### Installing and Configuring Node-RED on Raspberry Pi

Conifguring NodeRED, MQTT is required only one time.

Open the terminal and execute the following commands

```
- sudo apt install ufw
- sudo ufw enable
- sudo ufw allow tcp http https 1883 8883 1880 80 8080 443
```
##### Installing MQTT(Mosquitto)
Open the terminal and execute the following commands

```
- sudo apt install -y mosquitto mosquitto-clients
- sudo systemctl enable mosquitto.service
- mosquitto -v
```

1.  To run the program just restart the raspberry pi.

This program make use of MQTT to communicate with the webapp.

## ⛏️ Testing <a name = "test"></a>

1.  The Firmware can be tested on Raspberry Pi 3B, 3B+ or 4B with the following modifications
  1.  Connect the sensor as shown in the Circuit Diagram section below.

## 🔌 Circuit Diagram <a name = "circuit"></a>

![GPIOsRPi](Circuit/Circuit_bb.png)


* RPi Zero 2 W GPIOs Pinout

![GPIOsRPi](Circuit/pinout.jpg)



### Circuit



```http
Pins connections
```

| MPU9250 | Raspberry Pi |
| :--- | :--- |
| `SDA` | `2` | 
| `GND` | `GND` |
| `3V3` | `3V3` | 
| `SCL` | `3` | 

| Button Pins | Raspberry Pi |
| :--- | :--- |
| `Pin 1` | `5V` | 
| `Pin 2` | `GND` | 
| `P1` | `29` | 
| `P2` | `31` | 
| `P2` | `33` | 
| `P2` | `35` | 



## Dashboard <a name = "dashboard"></a>


  ```diff
  - In progress.
  ```

You can use the dashboard with the link below:

[)
![dash](artwork/)



## Components Used

1.  [Raspberry Pi Zero 2 W](https://www.amazon.com/CanaKit-Raspberry-Wireless-Complete-Starter/dp/B07CMVDHWB/ref=sr_1_4?crid=3HHNCDL4Q4CQ9&keywords=raspberry+pi+zero+2+w&qid=1672982210&sprefix=raspberry+pi+zero+2+w%2Caps%2C194&sr=8-4)
2. [Raspberry Pi Cam](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_4_mod_primary_new?crid=2OZKT6QUT4DRU&keywords=raspberry+pi+cam&qid=1672982230&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=raspberry+pi+cam%2Caps%2C143&sr=8-4)
3. [IMU MPU9250](https://www.amazon.com/MPU9250-Compass-Acceleration-Gyroscope-Attitude/dp/B09GCF394V/ref=sr_1_2?crid=2LK80QR26XRMQ&keywords=mpu9250&qid=1656626270&sprefix=mpu9250%2Caps%2C177&sr=8-2)

4.  [Small Push Button](https://www.amazon.com/BOJACK-Tactile-Pushbutton-Switches-Momentary/dp/B07ZN1N299/ref=sr_1_7?crid=3AGU6V06CNS03&keywords=small+push+button+two+pin&qid=1656626603&sprefix=small+push+button+two+pin%2Caps%2C175&sr=8-7)


## ⛏️ Built Using <a name = "built_using"></a>

- [Python3](https://www.python.org/) - Raspberry Pi FW
- [Node-RED](https://nodered.org/) - Platform for creating dashbaords and backend logic
- Bash

## ✍️ Authors <a name = "authors"></a>

- [@Nauman3S](https://github.com/Nauman3S) - Development and Deployment
