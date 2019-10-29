import socket
import time
#import socket.timeout as TimeoutException

ClientMsg = "FUCK YOU UDP Server"
WhatToSend = str.encode(ClientMsg)
serverAddressPort = ("127.0.0.1", 12000)
bufferSize = 1024

# Create a UDP socket at client side

ClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
ClientSocket.settimeout(1)

# inits for min, max, and avg RTTs
maxRTT = 0
minRTT = 1
compareRTT = 0
totalRTT = 0
avgRTT = 0
count = 0

# Send to server using created UDP socket
for i in range(1,11):
    beginTime = time.time()
    seq = i
    print("PING {} {}".format(i, beginTime))
    ClientSocket.sendto(WhatToSend, serverAddressPort)
    try:
        ServerMsg = ClientSocket.recvfrom(bufferSize)
    except socket.timeout:
        print("   > OOOOOOOOOOOOOOOOOHHHHHHHHHH NOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!! Request Timed out, Try again...")
        continue
    endTime= time.time()
    if(ServerMsg[0] !=''):
        rcvmsg= ServerMsg[0].decode("utf-8")
        RTT= endTime- beginTime
        compareRTT = RTT
        msg = "   > Message from Server {} and RTT = {} seconds".format(rcvmsg, RTT)
        print(msg)
        # Getting min/max RTTs + total RTTs for avg
        if (compareRTT > maxRTT):
            maxRTT = compareRTT
        elif (compareRTT < minRTT):
            minRTT = compareRTT
        totalRTT += RTT
        count += 1
avgRTT = totalRTT / count   # get avg RTT
msg2 = "\n >>> REPORT: Min RTT = {} seconds, Max RTT = {} seconds, Avg RTT = {} seconds".format(minRTT, maxRTT, avgRTT)
print(msg2)

