from socket import *
import time

serverName = "localhost" #replace with actual name
serverPort = 12000 #use an available port


clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)              # simualte packet loss

for i in range(1, 6):
    start_time = time.time()           
    message = f"PING {i} - hello world"
    clientSocket.sendto(message.encode(),(serverName, serverPort))  # store time when request sent
    
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        end_time = time.time()
        print(modifiedMessage.decode(),"    ", f"RTT is {end_time - start_time}")      # print RTT result and received message   
    except timeout:
        print("request timed out")
          
clientSocket.close()

# https://stackoverflow.com/questions/18311338/python-udp-client-time-out-machinsm