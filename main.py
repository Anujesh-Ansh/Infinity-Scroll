"""
}-> How to go with it

1-> we need to capture video
2-> we need to specify with color we want to focus on
3-> after selecting the color, we need to remove noises from the output video
4-> make a proper rectangle around the specified color
5-> now make a focal point, i.e, fixed point, from where the scrolling would start

NOTE-> ( U can make a function to return values for x,y,h,w and call it to select the starting fixed point,
        later on simply keep calling the function in the 'while True' section) --> using this, you can make the fixed point dynamic,

 matlab, jaise ki abhi maine ek point select kar diya hai '370', toh yeh chalega, par agar mere ko isko durr se chalana hai toh yeh phir ulta seedha kaam karega
 toh isiliye function banao taaki program jab start ho toh humlog apna fixed point automatically set karle, aur phir agar uske upar move karenge toh yeh scroll up hoga, warna agar neeche gaye toh yeh scroll down hoga

 6-> Now see if axis y is less than fixed point then scroll up, else scroll down


 }-> Uses of different packages and variables

 -> open cv - to perform programming on videos
 -> pyautogui - to perform any keyboard or mouse task
 -> contours - used to draw lines around the specified area
 -> rectangle - makes a proper rectangle around the specified area
 -> drawContours - makes the lines around the contour
 -> lower & upper - to specify the range of a particular color

 THank YOu !!!

 Anujesh Ansh Signing Off !!!

"""



import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)  # to capture video

yellow_lower = np.array([22, 93, 0])  # these 2 are the color range specifically for yellow, search 'cv2 yellow color range' or of any color to add it in the program
yellow_upper = np.array([45, 255, 255])  # these two commands only specify, as to which color to select
prev_y = 370  # change arounding to the  requirement

while True:
    ret, frame = cap.read()  # saves the video data in ret and frame
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converts the frame to gray in color
    hsv =cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Coverts the frame to hsv saturation
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)  # Sets the range for hsv saturation range

    # draws green line across the selected or similar color
    contour, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame, contour, -1, (0, 255, 0), 2)

    # to remove noises from the video
    for c in contour:
        area = cv2.contourArea(c)
        if area > 300:
            x, y, w, h = cv2.boundingRect(c)  # gives 4 values, which are related to position
            cv2.rectangle(frame, (x , y), (x + w, y + h), (0, 255, 0), 2)
            #cv2.drawContours(frame, c, -1, (0, 255, 0), 2)
            print('y = ',y,'    p =  ',prev_y)
            if y>=prev_y-70 and y<=prev_y+50:
                print('holding')

            elif y < prev_y:

                print('moving down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                #prev_y = y
            elif y > prev_y:
                print('moving up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
    # display option
    cv2.imshow('frame', frame)  # it displays the video, with the name frame, which can be changed to anything
    # cv2.imshow('mask', mask)  # displays the video, with applied feature on frame window
    if cv2.waitKey(10) == ord('q'):  # if the video is selected and 'q' is pressed, them the video would stop
        break

cap.release()
cv2.destroyAllWindows()