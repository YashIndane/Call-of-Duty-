# importing socket module 

import socket
import binascii
import pyautogui
import joblib

UDP_IP = '192.168.29.176'
UDP_PORT = 5600
model = joblib.load('svm_classifier')
scaler = joblib.load('scaler_svm')
  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT)) 

pyautogui.FAILSAFE = True

commands = [  '',
              'pyautogui.keyUp("w")',
              'pyautogui.click(button="right")',
              'pyautogui.keyDown("w")',
              'pyautogui.drag(-170, 0, 0.5,button="left")', 
              'pyautogui.drag(170, 0, 0.5,button="left")' 
           ]

temp = 1

while True: 

        buffer_size = 1024  
        data, addr = sock.recvfrom(buffer_size)  
        val = binascii.hexlify(data).decode('utf-8')
        val = [val[i:i+2] for i in range(0, len(val), 2)]
        measures = val[36:48]
        #print(measures)

        w = [int(x , 16) for x in  measures]
        row_ = []

        for v in [w[0:2] , w[4:6] , w[8:10]] : 

          for k in v : row_.append(k)

        p = scaler.transform([row_])
        m = model.predict(p)[0]  

        #print(m)
        
        if abs(m - temp) !=0 :
             
             #pyautogui.click(button='right')
             try :
                if m == 2 and temp == 3:
                    pyautogui.keyUp("w")

                if m == 3 and temp == 2 : 
                    pyautogui.click(button="right")

                if m == 1 and temp == 2 :
                    pyautogui.click(button="right")

                #exec(commands[m])

             except: c__ = 0
             if m in (4,5) and temp == 3:
                #pyautogui.keyUp("w")
                #pyautogui.keyDown("z")
                exec(commands[m])
                #pyautogui.keyUp("z")

             else:
                exec(commands[m])   

             if m in (4 , 5):
                    pyautogui.moveTo(950 , 570)
           
             
        temp = m
        #print(m)                                     
