import socket
from argparse import ArgumentParser
import os
import sys


def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, int(port)))
    s.shutdown(socket.SHUT_WR)
    response = ""
    while True:
        data = s.recv(4096)
        if not data:
            break
        #print("Received:", repr(data))
        response = repr(data)
    print("Connection closed.")
    s.close()
    split_bytes(response)

def split_bytes(x):
    #split = [x[i] for i in range(0, len(x))]
    print_int((x[2:-4].split(" \\n")))
    #print(xfor x in str)

def print_int(x):
    flag = ""
    #print(x)
    for i in x:
        flag += chr(int(i)) 
    print(flag)

parser = ArgumentParser()
parser.add_argument("-host", "--hostname", help="add the hostname of the server")
parser.add_argument("-p", "--port", help="add the port for the connection")
args = parser.parse_args()

hostname = sys.argv[2]
port = sys.argv[4]

print("You are connecting to: {} on port {}.".format(hostname, port))

netcat(hostname, port)
#print(response)
