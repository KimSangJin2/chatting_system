from socket import *

port = 8080

serverSock = socket(AF_INET, SOCK_STREAM) #소켓생성(AF, 소켓타입)
serverSock.bind(('', port)) #8080포트를 모든 인터페이스(IP)에 연결
serverSock.listen(1) #접속은 최대 1명을 허락하겠다.

print('%d번 포트로 접속대기중....'%port)

connectionSock, addr = serverSock.accept() #접속을 수락하고 그 후 통신을 함. connectionSock = 새로운 소켓, addr = 상대방AF

print(str(addr), '에서 접속이 확인되었습니다.')

while 1:
    data = connectionSock.recv(1024)
    print('상대방 : ', data.decode('utf-8'))

    message = input('>>>')
    connectionSock.send(message.encode('utf-8'))





