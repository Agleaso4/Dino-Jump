import cvzone
from cvzone.HandTrackingModule import HandDetector
import cv2
import pyautogui as auto
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
while True:
    # Get image frame
    success, img = cap.read()
    hands = False
    if success:
        hands, img = detector.findHands(img, draw=True)
    if hands:   
        if len(hands) > 1:
            if hands[0]["lmList"][0][0] < hands[1]["lmList"][0][0]:
                left_hand = hands[0]  # Left hand
                right_hand = hands[1]  # Right hand
            else:
                left_hand = hands[1]  # Left hand
                right_hand = hands[0]  # Right hand

            # Left Hand
            HandLandMarkList1 = left_hand["lmList"]  # List of 21 Landmark points
            length_i_t,info_i_t,frame_i_t = detector.findDistance(HandLandMarkList1[4][0:2],HandLandMarkList1[8][0:2],img)
            length_i_t = round(length_i_t)
            # Right Hand
            HandLandMarkList2 = right_hand["lmList"]
            length2_i_t,info2_i_t,frame2_i_t = detector.findDistance(HandLandMarkList2[4][0:2],HandLandMarkList2[8][0:2],img)
            length2_i_t = round(length2_i_t)

            length_i_i,info_i_i,frame_i_i = detector.findDistance(HandLandMarkList1[4][0:2],HandLandMarkList2[4][0:2],img)
            length_i_i = round(length_i_i)

            length_p_t,info_p_t,frame_p_t = detector.findDistance(HandLandMarkList2[4][0:2],HandLandMarkList2[20][0:2],img)
            length_p_t = round(length_p_t)

            length2_p_t,info2_p_t,frame2_p_t = detector.findDistance(HandLandMarkList1[4][0:2],HandLandMarkList1[20][0:2],img)
            length2_p_t = round(length2_p_t)

            if length_i_i < 25:
                auto.press('space')
            elif length_p_t < 25:
                auto.press('left')
            elif length2_p_t < 25:
                auto.press('right')
            elif length_i_t > 25 and length2_i_t < 25:
                auto.press('down')
            elif length_i_t < 25 and length2_i_t > 25:
                auto.press('up')
            

        else:
            # Left Hand
            HandLandMarkList1 = hands[0]["lmList"]  # List of 21 Landmark points
            length,info,frame = detector.findDistance(HandLandMarkList1[4][0:2],HandLandMarkList1[8][0:2],img)
            length = round(length)

            if length<25:
                auto.press('up')

            
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q') or cv2.getWindowProperty("Image", 0) == -1:
        cv2.destroyWindow("Image") 
        break
