import socket
import json

serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print('Client up and listening')

# Send test message to server
msgFromClient = '{"status":"alive"}'
bytesToSend = str.encode(msgFromClient)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

while True:
    # Receive from server using created UDP socket
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    # Format and print message and IP address
    msgStr = "Message from Server: {}".format(msgFromServer[0])
    address = "Server IP Address: {}".format(msgFromServer[1])
    print(msgStr)
    print(address)

    msg = msgFromServer[0].decode()
    statusDict = json.loads(msg)
    print('JSON Dict:')
    print(statusDict)
