import socket
import random
from threading import Thread
class Sending(Thread):
    def run(self):
        while True:
            message=input()
            c = socket.socket()
            c.connect((recv_ip,recv_port))
            c.send(bytes(message,"utf-8"))
            print("***----Message sent----***")
            c.close()

class Receiveing(Thread):
    def run(self):
        while True:
            s = socket.socket()
            s.bind((ip,port))
            s.listen(20)
            a,addr=s.accept()
            print("\nReceived:", a.recv(1024).decode())
            
            a.close()
            s.close()





print("Welcome to chatting machine")
port=random.randint(10000,20000)
print("Your id is:", port)
ip=input("Enter your IP address ")
recv_port=0
print("To send message press 1")
print("To reveive message press 2")
wish=int(input("Enter your choice "))
if wish==1:
    recv_port=int(input("Enter the receiver id  "))
    recv_ip= str(input("Enter the receiver IPv4 addrerss "))
    c = socket.socket()
    c.connect((recv_ip, recv_port))
    c.send(bytes(str(port),"utf-8"))
    c.close()
if wish==2:
    s = socket.socket()
    s.bind((ip,port))
    s.listen(20)
    a,addr= s.accept()
    recv_port= int(a.recv(1024).decode())
    recv_ip=str(addr[0])
    print("Connected with:", recv_port,  recv_ip)
    a.close()
    s.close()

sender= Sending()
receiver= Receiveing()
sender.start()
receiver.start()