# Cozmo 

<img src="cozmo.jpg" alt="drawing" height="250"/>

<div style="background-color:rgba(225, 240, 255, 1);">

> # ✨ NEWS!
>
> André Silva shared with us his master theses project with Cozmo!
>
> Explore the project github: [Conflict Model](https://github.com/joanacfcampos/ConflictModel.git)

</div>

## What is Cozmo?

Cozmo is a small, intelligent robot developed by Anki that combines robotics, AI, and expressive personality to create an engaging interactive experience. Unlike a simple toy, Cozmo can recognize faces, play games, explore its environment, and respond to user input with a lively personality. It’s designed to be both fun and educational—an ideal platform for learning about coding, robotics, and artificial intelligence.


### Cozmo hardware

Cozmo components are:
- 1 Camera
- 1 OLED display (face)
- 3 motors (lift + 2 treads)
- 2 treaded wheels
- 1 Speaker
- 1 Button
- Sensors (cliff, IMU, encoders)
- Wi-Fi hotspot


> [!CAUTION]
> All equipment underwent thorough testing and verification prior to its availability to students. Kindly exercise caution and ensure the return of each item enclosed in the box in the **same condition** as it was borrowed.

## What you need to use Cozmo?

- 1 Cozmo
- 1 charging dock
- 3 Interactive Cube   

## How to quickly start with Cozmo?

### First you must configure the set-up

1. Assure that you are using a python version between 3.8 and 3.11 or create your virtual environment with one of those.

2. Create a virtual environment.
> [!WARNING]
> It is good practice to create a virtual environment for each of your projects! 

3. Download at least one sample file from the [Examples folder from PyCozmo github](https://github.com/zayfod/pycozmo/tree/master/examples). We suggest the [go_to_pose.py](https://github.com/zayfod/pycozmo/blob/master/examples/go_to_pose.py) script.

4. Install the communication library called [PyCozmo](https://github.com/zayfod/pycozmo)
```
pip install pycozmo 
```

5. Download PyCozmo resources:
```
cd <your_venv_name>/Scripts
python pycozmo_resources.py download
```

### Connect your computer to Cozmo

1. Turn Cozmo on by pressing the button on its back for a few seconds. A Wi-Fi network name and password will appear on Cozmo's screen.

2. On your computer, open the Wi-Fi setting and connect to Cozmo's network using the password displayed.

### Run the sample code

1. Run the sample code
```
python go_to_pose.py
```

>[!TIP]
> Read and try the examples that the developers of PyCozmo have available at the [Examples folder](https://github.com/zayfod/pycozmo/tree/master/examples)




