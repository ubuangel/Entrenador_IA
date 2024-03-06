import cv2
from choice import Choice as cho
import time


def generate_image(img1, img2, ys,xs) :
    h2,w2 = img2.shape[:2]

    for i in range(h2) :
        for j in range(w2) :
            img1[ys + i, xs + j] = img2[i, j] if img2[i, j].all() != 0 else img1[ys + i, xs + j]

    return img1

def choice() :
    wCam, hCam = 720, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    choice = cho.Choice()

    first_enter_1 = True
    pTime = 0
    while True:
        success, img = cap.read()
        img_1 = cv2.imread("Images/start.png")
        
        img_n = cv2.imread("Images/confondoazul.png")
        img_2 = cv2.imread("Images/thumb_up.png")

        #img= generate_image(img, img_n, 0, 0)
        #img= generate_image(img, img_1, 5, 240)
       # img = generate_image(img, img_2, 167, 476)
        
        #relleno
        img_relleno=cv2.rectangle(img, (200,0), (460,220), (255,0,0), -1)
        
        img= generate_image(img_relleno, img_1, 5, 240)
        
        cv2.rectangle(img, (0,0), (200,480), (255,0,0), -1)
        img_rellenoderecho=cv2.rectangle(img, (460,0), (639,480), (255,0,0), -1)
        
        
        img = generate_image(img_rellenoderecho, img_2, 167, 476)
        
        cv2.putText(img_relleno, f'Si estas listo haz ', (200, 210), cv2.FONT_HERSHEY_DUPLEX, 1,
                    (255, 255, 0), 2)
        cv2.rectangle(img, (200, 220), (460, 480), (42, 42, 162), 3)
        
        cv2.rectangle(img, (460,460), (480,720), (255,0,0), -1)
        
        
        
        cTime = time.time()
        is_thumb_up, xb1, xb2, yb1 = choice.get_choice(img)

        if is_thumb_up and xb1<470 and  xb2>180 and yb1>180:# and yb2<470 :
            #print("in first if")
            if first_enter_1 :
                pTime = cTime
                first_enter_1 = False
            if (cTime-pTime) >= 2 :
                #print("start exercise")
                return "start exercise"
        else :
            first_enter_1 = True

        cv2.imshow("AI Trainer", img)
        cv2.setWindowProperty('AI Trainer', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        ch = cv2.waitKey(1)

if __name__ == "__main__" :
    choice()


