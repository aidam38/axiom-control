import serial
from playsound import playsound

# Test sound effect
playsound("/sound/wall-e-boot.mp3")

PASSWORDS = ["ASTEROID", "DETERGENT", "ERROR", "RIVER", "REPLICA", "AMALGAM"]
OVERRIDE = "AD TERRAM"

NUM_PUZZLES = len(PASSWORDS)

ser = serial.Serial("COM9", 115200, timeout=0.1)

state = {password: False for password in PASSWORDS}
override_unlocked = False

def progress():
    return int(sum(state.values()) / NUM_PUZZLES * 100)

while True:
    submission = ser.readline().strip().decode("utf-8")
    if not submission:
        continue

    print(f"Submission: {submission}")
    if override_unlocked and submission == OVERRIDE:
        print("Override accepted!")
        break
    elif submission in PASSWORDS:
        state[submission] = True
        print(f"Unlocked {submission}!")
        if sum(state.values()) == NUM_PUZZLES:
            override_unlocked = True
            print("Override unlocked!")
    
    print(f"Progress: {progress()}%")

    ser.write(progress())

    
    