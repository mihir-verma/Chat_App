"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import os
import sys
import ctypes

msglist = []

def receive():
    while True:
        msg = client_socket.recv(BUFSIZ).decode("utf8")
        ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), False)
        msglist.append(msg)
        os.system('cls')
        for msg in msglist:
            print(msg)

def send(): #event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = input()
    client_socket.send(bytes(msg, "utf8"))
    #msglist.append(msg)
    os.system('cls')
    for msg in msglist:
        print(msg)
    if msg == "{quit}":
        client_socket.close()
        sys.exit()

HOST = input('Who do you want to contact?\n(Only right answer in hex codes will be accepted): ')
PORT = input('Enter secret key for encryption: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

x = Thread(target=receive)
x.start()

while True:
    send()
