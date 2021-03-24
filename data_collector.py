import socket
import binascii
import pyautogui
import csv

UDP_IP = 
UDP_PORT = 
  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT)) 

pyautogui.FAILSAFE = True


with open('orientations.csv' , 'a' , newline = '') as f :

    while True: 
        # buffer size is 1024 bytes 
        data, addr = sock.recvfrom(1024)  
        val = binascii.hexlify(data).decode('utf-8')
        val = [val[i:i+2] for i in range(0, len(val), 2)]
        measures = val[36:48]
        #print(measures)
        

        writer = csv.writer(f)
        w = [int(x , 16) for x in  measures]
        row_ = []

        for v in [w[0:2] , w[4:6] , w[8:10]] : 

          for k in v : row_.append(k)

        row_.append(3)

        
        writer.writerow(row_)  
