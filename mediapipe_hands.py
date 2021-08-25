import numpy as np

def hand_capture(queue):
    #multiprocessing queue for communication between processes    
    import cv2
    import mediapipe as mp

    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.2,
        max_num_hands=1) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # Flip the image horizontally for a later selfie-view display, and convert
            # the BGR image to RGB.
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            results = hands.process(image)
            image = np.zeros(image.shape)
            # Draw the hand annotations on the image.
            image.flags.writeable = True
            # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                coordinates = np.array([[landmark.x, landmark.y, landmark.z] for landmark in results.multi_hand_landmarks[0].landmark], dtype=np.float16)
                queue.put(coordinates)
                # for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, results.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)
            cv2.imshow('MediaPipe Hands', image)
            if cv2.waitKey(20) & 0xFF == ord('d'):
                break

    cap.release()
