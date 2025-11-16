import sys
from morseapi import MorseRobot

# This is the Bluetooth Address on my computer: D7:A1:50:13:3B:F3
# It might be the same for you, but you'll have to verify

def run(bot_address):
    with MorseRobot(bot_address) as robot:

        # Connecting sometimes fails, so we will try 5 times
        for _ in range(5):
            try:
                robot.connect()
                break
            except Exception as e:
                continue
            
        # Reset the robot
        robot.reset()

        # The robot greets you
        robot.say("hi") # Available sounds: ['bragging', 'ayayay', 'confused8', 'ohno', 'charge', 'hi', 'confused2', 'confused3', 'elephant', 'tiresqueal', 'brrp', 'confused5']

        previous_sound_direction = 0
        while True:
            try:
                robot.sleep(.5)
                # Talk to the robot and the robot will turn to you
                # Get the direction where the sound comes from
                sound_direction = robot.sensor_state["sound_direction"]
                # Turn the Robot in that direction if direction > 100 deegres
                # The sound direction does not return to 0 so we only make the robot move it the sound direction gets updated
                if sound_direction > 100 and sound_direction != previous_sound_direction:
                    robot.turn(sound_direction)
                    previous_sound_direction = sound_direction

                # Robot detects being picked up
                # If you pick it up, the robot will start moving
                user_picked_up_robot = robot.sensor_state["picked_up"]
                if user_picked_up_robot:
                    robot.say("ayayay")
                    break
            
            except KeyboardInterrupt as e:
                robot.stop()
                pass

        while True:
            try:
                robot.sleep(.5)

                # Make the robot move
                robot.move(1000)

                # If robot is close to something stop and turn as well
                # 255 is the maximum and we don't want it to hit so let's try 200
                if robot.sensor_state["prox_left"] > 150 and robot.sensor_state["prox_right"] > 150:
                    robot.stop()
                    robot.say("tiresqueal")
                    robot.turn(180)
                
            
            except KeyboardInterrupt as e:
                robot.stop()
                pass


if __name__ == "__main__":
    #import logging
    #logging.getLogger().setLevel(logging.debug)
    bot_address = sys.argv[1] if len(sys.argv) > 1 else None
    run(bot_address)


