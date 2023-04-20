#!/usr/bin/python
# coding=utf8



import socket
import sys
from numba import jit


def classic_client_transfer(host:str, port:int, message, recvValue:int = 1024, _return:bool = False):
 
    # it is use classic transfer method


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket: 
        
        socket.connect((host, port))
        socket.sendall(message)

        if _return == True:
            
            data = socket.recv(recvValue)
            return data




@jit
def client_speed_transfer(host:str, port:int, message):

    # speed_client_transfer method is non-secure but fasted transfer method file it is use numba

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket: 
        
            socket.connect((host, port))
            socket.sendall(message)




def client_detailed_transfer(host:str, port:int, message, log:bool = True, _return:bool = True, socket_method = socket.SOCK_STREAM, crypt:str = 'NONE', recv:int=1024):

    # Detailed transfer method

    crypt.upper

    if log != True and _return != False:

        if socket_method == socket.SOCK_STREAM or socket_method == socket.SOCK_RAW:

            with socket.socket(socket.AF_INET, socket_method) as socket :

                socket.connect((host, port))
            
            # if user used crypto algorithm.


                if crypt == 'NONE':
                    socket.sendall(message)

                elif crypt == 'FERNET':
                    pass



                





    

    

