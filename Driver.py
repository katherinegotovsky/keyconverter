#!/usr/bin/python2.6
import socket
import time

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5

def handle_request(client_connection):
    request = client_connection.recv(1024)
    output = (request.decode())
    output1 = list(output)
    num = 20
    num1 = []
    while output1[num] != 'H':
        num1.append(output1[num])
        num = num + 1
    num1 = ''.join(num1)
    print num1
    import time
    import os
    import SHADMODULE1
    
    f = open('SHADSTUFF.txt','r+')
    Lines=f.readlines()
    Line = str(Lines[1])
    lines1 = list(Lines)
    list1 = []
    f1 = open('SHADSTUFFNUMBERS.txt','r+')
    number = f1.readlines()
    for i in range(len(lines1[1])):
        list1.append(lines1[1][i])
    numbercheck = list1[28]
    holder = SHADMODULE1.numbers(numbercheck)
    num1 = int(num1)
    keyboard1 = num1 / 20
    holder1 = holder + keyboard1
    holder1 = str(holder1)
    list1[28] = holder1
    list1=''.join(list1)
    os.system(list1)
    f.close()    
    http_response = b"""\
HTTP/1.1 200 OK

Hello, People!
"""
    client_connection.sendall(http_response)
    time.sleep(1)  

def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))

    while True:
        client_connection, client_address = listen_socket.accept()
        handle_request(client_connection)
        client_connection.close()

if __name__ == '__main__':
    serve_forever()
