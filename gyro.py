# importing socket module 
import socket
import binascii
import pyautogui
import joblib

UDP_IP = 
UDP_PORT = 
model = joblib.load('rf_classifier')
scaler = joblib.load('scaler_rf')
  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT)) 

pyautogui.FAILSAFE = True

commands = [  '',
              'pyautogui.keyUp("w")',
              'pyautogui.click(button="right")',
              'pyautogui.keyDown("w")',
              
           ]


with open('orientations.csv' , 'a' , newline = '') as f :
   
    temp = 1

    while True: 

        

        # buffer size is 1024 bytes 
        data, addr = sock.recvfrom(1024)  
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
             exec(commands[m])
             


 
        temp = m
        #print(m)                                     

   
    
