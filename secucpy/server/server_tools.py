#!/usr/bin/python3

import socket 
from  numba import jit

class Create:

    def classic_server(host = socket.gethostname(), port:int = 8080, recv:int = 1024, guest:int= 1, data_send:bool = False, output:bool = False, output_msg:str = 'NONE'):


        # Connection Created
        server = socket.socket()
        server.bind((host, port))

        # start Connection listen
        server.listen(guest)
        conection ,adress = server.accept()

        if output != False:
            print(output_msg)

            while True:

                data = conection.recv(recv).decode()
                if not data: 
                    break

                print("connected user: " + str(data))
                
                
                if data_send != False:
                    data = input(' ----->')
                    conection.send(data.encode())

            conection.close()

    
    
    @jit
    def speed_server(host:str, port:int):
        server = socket.socket()
        server.bind((host, port))
        
        server.listen(1)

        connection, adress = server.accept()

        while True: 

            data = connection.recv(1024).decode()
            if not data: 
                break

            print("connected user: " + str(data))

        connection.close()   


    def Suitable_File_Transfer(file, host:str, port:int, recv:int = 1024):

        server = socket.socket()
        server.bind((host, port))

        connection, adress = server.accept()

        with open(file, "wb") as file: 

            while True: 

                byte = server.recv(recv)

                if not byte: 

                    print("***NO DATA***")

                file.write(byte)

                server.close()

