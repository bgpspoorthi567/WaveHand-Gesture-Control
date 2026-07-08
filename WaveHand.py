import cv2
import serial
import time
import mediapipe as mp
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

arduino = serial.Serial("COM3", 9600, timeout=1)
time.sleep(2)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.6)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

light_on = False
hand_detected_time = None
gesture_mode = False   


def is_fist_closed(hand_landmarks):
    fingertips = [8, 12, 16, 20]
    finger_pips = [6, 10, 14, 18]

    for tip, pip in zip(fingertips, finger_pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            return False  
    return True  


def is_thumb_up_fist(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[4]
    thumb_ip = hand_landmarks.landmark[3]
    thumb_mcp = hand_landmarks.landmark[2]
    wrist = hand_landmarks.landmark[0]

    return (thumb_tip.y < thumb_ip.y < thumb_mcp.y
            and abs(thumb_tip.x - wrist.x) < 0.1
            and is_fist_closed(hand_landmarks))


def is_thumb_down_fist(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[4]
    thumb_ip = hand_landmarks.landmark[3]
    thumb_mcp = hand_landmarks.landmark[2]
    wrist = hand_landmarks.landmark[0]

    return (thumb_tip.y > thumb_ip.y > thumb_mcp.y
            and abs(thumb_tip.x - wrist.x) < 0.3
            and is_fist_closed(hand_landmarks))


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            if hand_detected_time is None:
                hand_detected_time = time.time()

            if not gesture_mode and (time.time() - hand_detected_time) >= 2:
                gesture_mode = True
                print("Hand locked -> Give gesture")
            if gesture_mode:
                if is_thumb_up_fist(handLms):
                    if not light_on:
                        print("Thumbs Up -> Light ON")
                        arduino.write(b'1')
                        light_on = True
                    cv2.putText(frame, "Thumbs Up (Fist) -> Light ON", (10, 110),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                elif is_thumb_down_fist(handLms):
                    if light_on:
                        print("Thumbs Down -> Light OFF")
                        arduino.write(b'0')
                        light_on = False
                    cv2.putText(frame, "Thumbs Down (Fist) -> Light OFF", (10, 110),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                else:
                    cv2.putText(frame, "Waiting for Thumbs Up/Down (Fist)", (10, 110),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            else:
                cv2.putText(frame, "Scanning hand... Please hold still", (10, 110),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 2)
    else:
        hand_detected_time = None
        gesture_mode = False

    cv2.imshow('Gesture Control', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
arduino.close()