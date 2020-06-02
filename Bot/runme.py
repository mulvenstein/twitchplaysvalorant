'''
author : tom mulvey
d : 6-2-20
this is gona be complete spaget and im sorry if u get banned,
    this is just a fun experiment.
'''

import socket
from emoji import demojize
sock = socket.socket()
import os
import sys
import json
import time
import uuid
import collections
import multiprocessing

PROCESSES = multiprocessing.cpu_count() - 1

import asyncio

'''
server = 'irc.chat.twitch.tv'
port = 6667
nickname = whateva you want
token = GET THIS TOKEN FROM https://twitchapps.com/tmi/
channel = CHANGE TO #CHANNEL_NAME to what u want to run this against
'''
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'twitch_plays_val_LULW'
token = 'yo'
channel = '#tmulvey'

loop = asyncio.get_event_loop()
queue = asyncio.Queue(loop=loop)

#----- funcs
def SockConn(): #deez nuts
    sock.connect((server, port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))
    return

def GetCommandsLive():
    while True:
        resp = sock.recv(2048).decode('utf-8')

        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))
        
        elif len(resp) > 0:
            print(demojize(resp))
    return

# send twitch message here pogu
async def produce():

    return

async def consume():

    return


def main():
    print("yo")
    SockConn()
    GetCommandsLive()
    return 

#----
if __name__ == "__main__":
    main()

main()