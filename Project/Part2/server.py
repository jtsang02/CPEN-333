from socket import *
import random
from time import sleep

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    if (random.random() < 0.9):          # 90% of the time, values below 0.90 are chosen
        modifiedMessage = message.decode().replace("hello world", "ditto")  # replace greeting with ditto
        sleep(random.randrange(5, 50) / 1000)                       # simulate random delay b/t 5 and 50 ms before responding back
        serverSocket.sendto(modifiedMessage.encode(),clientAddress)