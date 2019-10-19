import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

# Listen for incoming datagrams
while True:
    # Receive reply from client
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    # Format and print reply and IP
    clientMsg = "Message from Client: {}".format(message)
    clientIP = "Client IP Address: {}".format(address)
    print(clientMsg)
    print(clientIP)

    # Send message to client
    msgFromServer = '{"status":"emergency"}'
    bytesToSend = str.encode(msgFromServer)
    UDPServerSocket.sendto(bytesToSend, address)

