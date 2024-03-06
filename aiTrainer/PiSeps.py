from aiTrainer import poseModule as pm
import cv2
import time
import math


class PiSeps :
    def __init__(self):
        self.count =0
        self.pose = pm.poseDetector()
        self.wrong_position = False
        self.counter = 0
        self.count_flip = False
        self.got_down = True
        self.first_enter = True
        self.timeForCurl = -1
        self.pTime = time.time()

    def rightPosture(self,img):
        hand = ""
        img = self.pose.find_pose(img, False)
        self.lm_list = self.pose.find_position(img, False)
        if (len(self.lm_list) > 12):
            x11, y11, z11 = self.lm_list[11][1], self.lm_list[11][2], self.lm_list[11][3]
            x12, y12, z12 = self.lm_list[12][1], self.lm_list[12][2], self.lm_list[12][3]
            length = math.hypot(x12-x11, y12-y11)
            #print("z11 : ", z11, " z12 : ", z12)
            if z11 == 1 or z12 == -1:
                hand = "Derecho"

            elif z12 == 1 or z11 == -1 :
                hand = "Izquierdo"

            if length<120 :
                return True, hand
            else :
                return False, hand
        return False, hand

    def get_left_or_right(self, img) :
        pass
        #if (len(self.lm_list) > 12) :
        #    print(selflm)


    def wrongElbowPosition(self, img, hand):
        x1, x2, y1 = 0, 0, 0
        hand_cof = 1
        if (len(self.lm_list) > 16):
            x12 =  self.lm_list[12][1]
            x14, y14 = self.lm_list[14][1], self.lm_list[14][2]
            x11 = self.lm_list[11][1]
            x13, y13 = self.lm_list[13][1], self.lm_list[13][2]
            if hand == "Derecho":
                x1, x2, y1 = x14, x12 , y14
                hand_cof = 1

            elif hand == "Izquierdo":
                x1, x2, y1 = x13, x11 , y13
                hand_cof = -1

            #print(hand_cof)
           #print(int(x1-x2))
            if int(x1 - x2) < (-10*hand_cof):
                self.wrong_position = (hand == "Derecho")
            else:
                self.wrong_position = (hand == "Izquierdo")

            if self.wrong_position:
                cv2.putText(img, "X", (x1-50 if hand == "Derecho" else  x1 , y1+30), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 6)

        return self.wrong_position;

    def count_curl_and_time(self, img, hand_cof, hand):
        angle = 0
        if hand == "Derecho" :
            angle = self.pose.find_angle(img, 12, 14, 16, draw=False)
        elif hand == "Izquierdo" :
            angle = self.pose.find_angle(img, 11, 13, 15, draw=False)
            angle = (360-angle) % 360
        #print(angle)

        if angle < (160) and angle > (140) and not self.wrong_position:
            if self.first_enter:
                self.pTime = time.time()
                self.first_enter = False
            self.got_down = True

        if angle < (80) and self.got_down and angle != -1 and not self.wrong_position:
            # print(time.time())
            # print(pTime)
            self.timeForCurl = round(time.time() - self.pTime, 2)
            self.count_flip = True
            self.got_down = False

        if self.count_flip:
            self.counter += 1
            #print(self.counter)
            #print(self.timeForCurl)
            self.first_enter = True
            self.count_flip = False

        if self.counter == 10:
            print(f'self.counter is {self.counter}')
            self.counter = 0
            return 10, time.time() - self.pTime

        #self.check_weight(img, time.time()-self.pTime)

        return self.counter, time.time()-self.pTime
