import socket
import sys


########################################################################
#                          COMMON ROUTINES                             #
########################################################################


RRQ = b'\x00\x01'
WRQ = b'\x00\x02'

#RRQ

def sendRRQ(sock, addr, filename,mode): 
    data = RRQ+ bytearray (filename.encode())+bytes(1)+bytearray (mode.encode())+bytes(1)
    sock.sendto(data,addr)

#WRQ

def sendWRQ(sock, addr, filename,mode):
    data = WRQ+ bytearray (filename.encode())+bytes(1)+bytearray (mode.encode())+bytes(1)
    sock.sendto(data,addr)
   

########################################################################
#                             SERVER SIDE                              #
########################################################################


def runServer(addr, timeout, thread):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('',6969))
    sock.settimeout(timeout)
    while True:
        data, addr = sock.recvfrom(1500)
        print('Starting TFTP server, listening on %s'.format(addr[0], addr[1], data))
        sock.sendto(data, addr)
        sock.close()
    


########################################################################
#                             CLIENT SIDE                              #
########################################################################


def put(addr, filename, targetname, blksize, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    sendWRQ(sock, addr, filename,'octet')
    sock.close()
    


########################################################################


def get(addr, filename, targetname, blksize, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    sendRRQ(sock, addr, filename,'octet')
    sock.close()

# EOF