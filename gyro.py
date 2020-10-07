# importing socket module 
import socket
import binascii
import pyautogui

UDP_IP = ''
UDP_PORT = ''
  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT)) 

pyautogui.FAILSAFE = True
  
while True: 
    # buffer size is 1024 bytes 
    data, addr = sock.recvfrom(1024)  
    val = binascii.hexlify(data).decode('utf-8')
    val = [val[i:i+2] for i in range(0, len(val), 2)]
    measures = val[36:48]

    #print(int(measures[4] , 16), int(measures[5] , 16))

   
    try : 
      pitch = int(measures[5] , 16)  
      if (pitch > 110 and last < 100) or last > 110 and pitch < 100 :
           #print('scope')
           pyautogui.click(button='right')
    except : pass       
    last = pitch


   
    