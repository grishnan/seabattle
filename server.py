from socket import *

def run_server():
    ''' Run server '''
    myHost = 'localhost'
    myPort = 12345

    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.bind((myHost, myPort))
    sockobj.listen(2)

    while True:
        connection, address = sockobj.accept()
        print("Есть коннект! IP = ", address[0])
        connection.close()

