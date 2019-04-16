from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080)) #나와 연결할때 8080포트를 써라


print('연결됐습니다')

while 1:
    message = input(">>>")
    clientSock.send(message.encode('utf-8'))

    data = clientSock.recv(1024)
    print('상대방 : ', data.decode('utf-8'))
