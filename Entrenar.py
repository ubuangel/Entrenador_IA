import cv2
import time
import ModuloPose as pm
import Brazo as ps
import numpy as np

import threading
import pyglet

#test

def generate_image(img1, img2, ys,xs) :
    h2,w2 = img2.shape[:2]

    for i in range(h2) :
        for j in range(w2) :
            img1[ys + i, xs + j] = img2[i, j] if img2[i, j].all() != 0 else img1[ys + i, xs + j]

    return img1

def check_weight(img, current_duration_for_curl, counter, wrong_position):

    x, y = 600, 320
    if wrong_position :
        cv2.putText(img, f'  Asegurate que', (x + 50, y - 110), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
        cv2.putText(img, f'  tu codo este', (x + 50, y - 80),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
        cv2.putText(img, f'  en linea con', (x + 50, y - 50),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
        cv2.putText(img, f'  tu hombro!', (x + 50, y - 20),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
    elif current_duration_for_curl > 3 and counter > 6:
        cv2.putText(img, f'Ese es mi', (x + 80, y - 100), cv2.FONT_HERSHEY_DUPLEX, 1, (76, 153, 0), 2)
        cv2.putText(img, f'Chico', (x + 80, y - 60), cv2.FONT_HERSHEY_DUPLEX, 1, (76, 153, 0), 2)
        cv2.putText(img, f'Solo falta: {10 - counter}', (x + 80, y - 35),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (76, 153, 0), 2)
    elif current_duration_for_curl > 3 and counter <= 6:

        cv2.putText(img, f'Solo tenemos:', (x + 70, y - 110),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)
        
        cv2.putText(img, f'{counter}', (x + 130, y - 80),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)
        
        cv2.putText(img, f' Hazlo Bien,', (x + 70, y - 50),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
        cv2.putText(img, f' Vamos!!!', (x + 70, y - 20),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)



    
def tell_hand_order(img,hand):
    #if (len(self.lm_list) > 16):
    x, y = 600, 310
    cv2.putText(img, f'Cambio !!', (x + 100, y - 80),
                cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)
    cv2.putText(img, f' lateral ', (x + 80, y - 50),
                cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)
    cv2.putText(img, f' {hand}', (x + 80, y - 25),
                cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)


def aiTrainer() :
    cap = cv2.VideoCapture(0)
    wcam, hcam = 1000, 1000
    cap.set(3,wcam)
    cap.set(4,hcam)

    pTime = 0
    pose = pm.poseDetector(min_detection_confidence=0.8)
    piStat = ps.PiSeps()
    group = 1
    hand_order = "Derecho"

    timer = 11
    counter = 0
    hand_cof = 1
    verified_hand = ""

    first_enter = True
    first_time_enter=True
    first_sound_enter=True
    while True :
        success, img = cap.read()
       
        right_pos, hand = piStat.rightPosture(img)
        cTime = time.time()
        if first_time_enter:
            pTime=cTime
            first_time_enter=False

        if hand == "Derecho":
            verified_hand = "Derecho"
        elif hand == "Izquierdo":
            verified_hand = "Izquierdo"

        if verified_hand == "Izquierdo":
            hand_cof= -1
        elif verified_hand == "Derecho":
            hand_cof= 1

        cv2.rectangle(img, (0,0), (210,480), (255,255,255), -1)
        coach_img = cv2.imread("Images/coachredi.jpg")
        

        if not timer and hand_order==verified_hand:
            wrong_pos = piStat.wrongElbowPosition(img, verified_hand)
            counter, current_duration_for_curl = piStat.count_curl_and_time(img, hand_cof, verified_hand)
           
            check_weight(img, current_duration_for_curl, counter, wrong_pos)
        
        elif 9<timer<=11:
            cv2.putText(img, f' A mi orden', (700, 200),
                        cv2.FONT_HERSHEY_DUPLEX, 1, (76, 153, 0), 2)
            
        elif hand_order!=verified_hand :
            tell_hand_order(img, hand_order)
        elif 1<timer<=3:
            cv2.putText(img, f' Estas Listo!!', (700, 200),
                        cv2.FONT_HERSHEY_DUPLEX, 1, (76, 153, 0), 2)
        if 0<timer<=1:
            cv2.putText(img, f' Ya!!', (700, 200),cv2.FONT_HERSHEY_DUPLEX, 1, (76, 153, 0), 2)
            if first_sound_enter==True:
       
       

                first_sound_enter=False


        if cTime - pTime >= 1 and timer > 0:
            timer-=1
            pTime = cTime


        cv2.putText(img, f'Cuenta: ', (10, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (42, 42, 162), 2)
        cv2.putText(img, f'{counter}', (130, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
        cv2.putText(img, f'Serie: ', (10, 90), cv2.FONT_HERSHEY_DUPLEX, 1, (42, 42, 162), 2)
        cv2.putText(img, f'{group}/4', (110, 90), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
        cv2.putText(img, f'Descanso: ', (10, 130), cv2.FONT_HERSHEY_DUPLEX, 1, (42, 42, 162), 2)
        cv2.putText(img, f'{timer}', (170, 130), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)

        if counter == 10:
            print(f'in if and counter is {counter}')
            if first_enter:
                group += 1
               
                hand_order = "Izquierdo" if hand_order == "Derecho" else "Derecho"
                counter = 0
                timer = 15
                first_enter = False
                first_sound_enter=True

        if counter != 10:
            first_enter = True

        if group == 5 :
            cTime=time.time()
            pTime=cTime
            while cTime-pTime<=1:
                success, img = cap.read()
                coach_img = cv2.imread("Images/coachredi.jpg")
                img = np.concatenate((img, coach_img), axis=1)
                cv2.putText(img, f'Buen !! ', (700, 190),
                            cv2.FONT_HERSHEY_DUPLEX, 1, (76, 153, 0), 2)
                
                cv2.putText(img, f' Trabajo!! ', (700, 240),
                        cv2.FONT_HERSHEY_DUPLEX, 1, (76, 153, 0), 2)
                
                cv2.imshow("AI Trainer", img)
                cv2.waitKey(1)
                cTime=time.time()
            
            sound = pyglet.resource.media('sounds/long_whistle.mp3', streaming=False)
            sound.play()
          
            return True

        cv2.imshow("AI Trainer", img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('AI Trainer',cv2.WND_PROP_VISIBLE) < 1: 
            break
   
       
        cv2.waitKey(1)
       
        

if __name__ == "__main__" :
    aiTrainer()

