#!/usr/bin/python
# coding=utf8



# Python packages 
import cython
import socket
import sys



def classic_client_transfer(host:str, port:int, message, recvValue:int = 1024, _return:str = False):
 
    # it is use classic transfer method


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket: 
        
        socket.connect((host, port))
        socket.sendall(message)

        if _return == true:
            
            data = socket.recv(recvValue)
            return data



def client_speed_transfer(host:str, port:int, message, recvValue:int = 1024):

    # speed_client_transfer method is non-secure but fasted transfer method file it is use C
    pass








    

    

