import socket
import time
#import socket.timeout as TimeoutException

ClientMsg = "Yay!  Packet sent/received successfully!"
WhatToSend = str.encode(ClientMsg)
serverAddressPort = ("127.0.0.1", 12000)
bufferSize = 1024

# Create a UDP socket at client side

ClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
ClientSocket.settimeout(1)

# inits for min, max, avg RTTs, and packet loss
maxRTT = 0
minRTT = 1
compareRTT = 0
totalRTT = 0
avgRTT = 0
count = 0
pktLossCt = 0

# Send to server using created UDP socket
for seq in range(1, 11):
    beginTime = time.time()
    print("PING {}, start time {} seconds".format(seq, beginTime))
    ClientSocket.sendto(WhatToSend, serverAddressPort)
    # Heartbeat BEGIN
    currTime = str(beginTime)
    ClientSocket.sendto(str(seq).encode(), serverAddressPort)  # send seq num to server
    ClientSocket.sendto(currTime.encode(), serverAddressPort)  # send current timestamp in UDP packet to server
    # Heartbeat END
    try:
        ServerMsg = ClientSocket.recvfrom(bufferSize)
    except socket.timeout:
        print("\t> OOOOOOOOOOOOOOOOOHHHHHHHHHH NOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!  Request Timed out, Try again...")
        pktLossCt += 1  # number of lost packets
        continue
    endTime = time.time()
    if(ServerMsg[0] != ''):
        rcvmsg = ServerMsg[0].decode("utf-8")
        RTT = endTime - beginTime
        compareRTT = RTT
        msg = "\t> Message from Server: {}, and RTT = {} seconds".format(rcvmsg, RTT)
        print(msg)
        # Getting min/max RTTs + total RTTs for avg
        if (compareRTT > maxRTT):
            maxRTT = compareRTT
        elif (compareRTT < minRTT):
            minRTT = compareRTT
        totalRTT += RTT
        count += 1
avgRTT = totalRTT / count   # get avg RTT
pktLoss = int((pktLossCt / 10) * 100)    # get packet loss
report = "\n >>> REPORT: Min RTT = {} seconds,\n\t\t\t Max RTT = {} seconds,\n\t\t\t Avg RTT = {} seconds, \n\t\t\t Pkt Loss Rate = {}%".format(minRTT, maxRTT, avgRTT, pktLoss)  # give report
print(report)

