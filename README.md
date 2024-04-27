# Gesture-Controlled Mecanum Wheel Robot

This project demonstrates how to control a Mecanum wheel robot using hand gestures detected by a camera. The robot's movements (forward, backward, left, right) are determined by the gestures recognized by the hand-tracking algorithm.

## Hardware Requirements

- Raspberry Pi
- Mecanum wheel robot chassis
- Four DC motors
- Two L298N motor drivers (or equivalent)
- Camera module compatible with Raspberry Pi
- Jumper wires
- Power supply

## Software Requirements

- Python 3
- OpenCV
- Mediapipe
- RPi.GPIO (for Raspberry Pi GPIO control)

## Setup Instructions

1. Connect the hardware components according to the wiring diagram provided.
2. Install the required Python libraries by running the following command:

3. Clone or download this repository to your Raspberry Pi.
4. Navigate to the directory containing the code files.
5. Run the main Python script using the following command:


## Usage

1. Launch the script as instructed above.
2. Place your hand in front of the camera.
3. Perform gestures such as moving your hand forward, backward, left, or right.
4. The Mecanum wheel robot should respond accordingly to your gestures, moving in the desired direction.

## Notes

- Ensure the camera has a clear view of your hand gestures.
- Fine-tune the gesture recognition algorithm as needed for better accuracy.
- Adjust the GPIO pin configurations in the code if your hardware setup differs.

## Credits

- This project utilizes the MediaPipe library for hand tracking and gesture recognition.
- Special thanks to the OpenCV and Raspberry Pi communities for their valuable contributions to the Python ecosystem.

