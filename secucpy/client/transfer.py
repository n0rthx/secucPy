#!/usr/bin/python
# coding=utf8


import socket
import sys
import configparser
from numba import jit


class Create:

    def classic_client_transfer(host:str, port:int, message, recvValue:int = 1024, _return:bool = False):
 
    # it is use classic transfer method


        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sct: 
        
            sct.connect((host, port))
            sct.sendall(message)

            if _return == True:
            
                data = sct.recv(recvValue)
                return data




@jit
def client_speed_transfer(host:str, port:int, message):

    # speed_client_transfer method is non-secure but fasted transfer method file it is use numba

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sct: 
        
            sct.connect((host, port))
            sct.sendall(message)




def client_detailed_transfer(host:str, port:int, message, log:bool = True, _return:bool = True, socket_method = socket.SOCK_STREAM, rec_value:int=1024, _recv:bool = True):

    # Detailed transfer method


    if log != True and _return != False:

        if socket_method == socket.SOCK_STREAM or socket_method == socket.SOCK_RAW:

            with socket.socket(socket.AF_INET, socket_method) as sct :

                sct.connect((host, port))
            
            # if user used crypto algorithm.
            
            if _recv == True:
                return sct.recv(rec_value)

            else: 
                return None




def config_transfer(message, ConfigFile:str, serverInfoName:str = "SERVER_INFO", connectMethodsInfo:str = "CONNECT_METHOD", SocketKind = socket.SOCK_STREAM):
    
    config = configparser.ConfigParser()
    config.read(ConfigFile)

    # GET HOST AND PORT INFO 
    host = config[serverInfoName].get['HOST']
    port = config[serverInfoName].getint['PORT']

    # GET CONNECTION METHODS INFO 

    recv = config[connectMethodsInfo].getint['RECV']
    _rec = config[connectMethodsInfo].getboolean['REC_CHECK']
 

    try:
        with socket.socket(socket.AF_INET, SocketKind) as sct : 
            sct.connect((host, port))
            sct.sendall(message)

            if _rec == True: 
                
                _return = sct.recv(recv)
                return _return
            else:

                return None
            
            
    except:
            with socket.socket(socket.AF_INET6, SocketKind) as sct : 
                sct.connect((host, port))
                sct.sendall(message)

                if _rec == True: 
                
                    _return = sct.recv(recv)
                    return _return
                else:

                    return None
                

def SOCK_DGRAM_TRANSFER(host:str, port:int, message, recv:int, rec:bool = False): 

            # DGRAM Transfer Method
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sct:
                sct.connect((host, port))
                sct.sendall(message)

                if rec != False:
                    
                    data = sct.recv(recv)
                    return print(data)
                
                else:
                    return None
        
        except:

                with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as sct:
                    sct.connect((host, port))
                    sct.sendall(message)

                    if rec != False:
                    
                        data = sct.recv(recv)
                        return data

                    else:
                        return None
                    


class FileTransfer:
    
    
    def classic_FileTransfer(filePath, host:str, port:int, recv:int = 1024):
         

         # Classic file transfer method
         # Requires a compatible server
         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sct:
              
              sct.connect((host, port))

              sendFile = open(filePath, 'rb')
              sct.sendfile(sendFile)





         

        



                    
        


                    

        
                


                
            



                





    

    

