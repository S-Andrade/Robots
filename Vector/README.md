# Vector

<img src="vector.jpg" alt="drawing" height="250"/>


## What is Vector?

Vector is a small, intelligent, and expressive robot developed by Anki. Designed as both a companion and a programmable device, Vector uses a combination of sensors, cameras, and AI algorithms to perceive its environment and interact with people in real time. It can recognize faces, respond to voice commands navigate autonomously, and even express emotions through animated eyes and body language.


### Vector hardware

Vector components are:
- 1 Camera
- 1 Color display (face)
- 4 Motors (2 tread motors + 1 lift motor + 1 head motor)
- 2 Treaded wheels
- 1 Speaker
- 4 Microphones (far-field array)
- 1 Button (on its back)
- 1 Capacitive touch sensor (around the back button)
- Wi-Fi
- Bluetooth

> [!CAUTION]
> All equipment underwent thorough testing and verification prior to its availability to students. Kindly exercise caution and ensure the return of each item enclosed in the box in the **same condition** as it was borrowed.

## What you need to use Vector?

- 1 Vector
- 1 charging dock
- 1 Interactive Cube   
- 1 Router
- 1 Networking cable

## How to quickly start with Vector?

>[!IMPORTANT]
>The original Vector software was discontinued by the company that created it. Therefore, in this guide, we’ll use a community-maintained fork of the original  software.

### First you must configure the set-up
 
1. Turn on and connect the router to a ethernet socket with a networking cable.
**You need to be connected to the internet**, so you can connect to the servers that help run vector's code.
>[!NOTE]
> On Lab 0 no ethernet sockets are not available, so during lab classes the router will be supplied with Ethernet by the professor computer, but if you come to the lab before hours one of your team members must be the one sharing the ethernet connection throughout their computer <br>
> If no one is using the router, you can use your own hotspot instead. If the router is on the robot will automatically connect to the router, and we have not found a way to change the network connection of vector. 

2. Connect your computer to the router's network
>[!IMPORTANT]
> **Your computer must be connected to the same network than the robot**. Make sure that you are connected to the network that you are going to use before continue this guide.

3. Install and run [Wire-Pod](https://github.com/kercre123/wire-pod), which is a open-source server that replaces Anki’s original cloud services. 

4. Assure that you are using a python version between 3.8 and 3.11 or create your virtual environment with one of those.

5. Create a virtual environment.
> [!WARNING]
> It is good practice to create a virtual environment for each of your projects! 

6. Install the [python vector sdk](https://github.com/kercre123/wirepod-vector-python-sdk) that works with the wire-pod
```
pip install wirepod_vector_sdk 
```

7. Run the configuration tool
```
python -m anki_vector.configure
```
>[!TIP]
> Read and follow the directions that the script explains. At some point it will ask for the serial number of vector, it's in the bottom of the robot.

8. Download at least on sample file from the [tutorials folder form the sdk github](https://github.com/kercre123/wirepod-vector-python-sdk/tree/master/examples/tutorials). We suggest the [01_hello_world.py](https://github.com/kercre123/wirepod-vector-python-sdk/blob/master/examples/tutorials/01_hello_world.py)

### Connect Vector to your computer 

1. Turn on your computer bluetooth 

2. Open a browser window on https://wpsetup.keriganc.com/html/main.html
>[!WARNING]
> The developers of this software only assure that this setup tool works on **Google Chrome**, but it might work on other browsers.

3. Place Vector on its charging dock and press the button twice. A key icon will appear on Vector’s screen. 

4. In your browser, click “Pair with Vector” 

5. A code will appear on Vector’s screen, enter this code into the browser to complete the pairing process.

6. Follow the on-screen steps to connect Vector to the router network. 

7. Vector may perform a short update, though all robots are already updated, so this step might be skipped. 

8. Click on the button “Activate” on your screen.

9. Fill up the configuration setting that follows, and in the end it will say that you are successfully connected to vector

### Run the sample code
1. Run the sample code
```
python 01_hello_world.py
```

>[!TIP]
> Read and try the examples that the developers of vector sdk have available at the [Tutorials folder](https://github.com/kercre123/wirepod-vector-python-sdk/tree/master/examples/tutorials)