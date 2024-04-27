import cv2
import mediapipe as mp
import RPi.GPIO as GPIO
import time

# Initialize MediaPipe Hands.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# GPIO setup
# Motor 1 (Front left)
motor1A = 20  # Direction pin
motor1B = 21  # Direction pin
GPIO.setup([motor1A, motor1B], GPIO.OUT)

# Motor 2 (Front right)
motor2A = 22  # Direction pin
motor2B = 23  # Direction pin
GPIO.setup([motor2A, motor2B], GPIO.OUT)

# Motor 3 (Rear left)
motor3A = 24  # Direction pin
motor3B = 25  # Direction pin
GPIO.setup([motor3A, motor3B], GPIO.OUT)

# Motor 4 (Rear right)
motor4A = 26  # Direction pin
motor4B = 27  # Direction pin
GPIO.setup([motor4A, motor4B], GPIO.OUT)

# Define motor control functions for Mecanum wheels
def move_forward():
    GPIO.output(motor1A, True)
    GPIO.output(motor1B, False)
    GPIO.output(motor2A, True)
    GPIO.output(motor2B, False)
    GPIO.output(motor3A, True)
    GPIO.output(motor3B, False)
    GPIO.output(motor4A, True)
    GPIO.output(motor4B, False)

def move_backward():
    GPIO.output(motor1A, False)
    GPIO.output(motor1B, True)
    GPIO.output(motor2A, False)
    GPIO.output(motor2B, True)
    GPIO.output(motor3A, False)
    GPIO.output(motor3B, True)
    GPIO.output(motor4A, False)
    GPIO.output(motor4B, True)

def turn_right():
    GPIO.output(motor1A, True)
    GPIO.output(motor1B, False)
    GPIO.output(motor2A, False)
    GPIO.output(motor2B, True)
    GPIO.output(motor3A, True)
    GPIO.output(motor3B, False)
    GPIO.output(motor4A, False)
    GPIO.output(motor4B, True)

def turn_left():
    GPIO.output(motor1A, False)
    GPIO.output(motor1B, True)
    GPIO.output(motor2A, True)
    GPIO.output(motor2B, False)
    GPIO.output(motor3A, False)
    GPIO.output(motor3B, True)
    GPIO.output(motor4A, True)
    GPIO.output(motor4B, False)

def stop_motors():
    GPIO.output([motor1A, motor1B, motor2A, motor2B, motor3A, motor3B, motor4A, motor4B], False)

# Define gesture recognition function
def classify_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    palm_base = landmarks[0]

    if thumb_tip.x > palm_base.x and index_tip.x > palm_base.x:
        return 'Turn Right'
    elif thumb_tip.x < palm_base.x and index_tip.x < palm_base.x:
        return 'Turn Left'
    elif index_tip.y < palm_base.y:
        return 'Move Forward'
    elif index_tip.y > palm_base.y:
        return 'Move Backward'
    return 'Unknown'

# Setup video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    image = cv2.flip(frame, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = classify_gesture(hand_landmarks.landmark)
            cv2.putText(image, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            
            # Control motors based on gesture
            if gesture == 'Move Forward':
                move_forward()
            elif gesture == 'Move Backward':
                move_backward()
            elif gesture == 'Turn Right':
                turn_right()
            elif gesture == 'Turn Left':
                turn_left()
            else:
                stop_motors()

    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
GPIO.cleanup()
