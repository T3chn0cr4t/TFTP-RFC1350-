#!/usr/bin/env python3
"""
TFTP Client Command.
"""

import sys
import argparse
import tftp

TIMEOUT = 2
PORT = 6969
BLKSIZE = 512

parser = argparse.ArgumentParser(prog='tftp-client')
parser.add_argument('-p', '--port', type=int, default=PORT)
parser.add_argument('-t', '--timeout', type=int, default=TIMEOUT)
parser.add_argument('-b', '--blksize', type=int, default=BLKSIZE)
parser.add_argument('cmd', type=str, choices=['get', 'put'])
parser.add_argument('host', type=str)
parser.add_argument('filename', type=str)
parser.add_argument('targetname', type=str, nargs='?', default='')
args = parser.parse_args()
if args.targetname == '':
    args.targetname = args.filename

# get request
if(args.cmd == 'get'):
    tftp.get((args.host, args.port), args.filename, args.targetname, args.blksize, args.timeout)

# put request
if(args.cmd == 'put'):
    tftp.put((args.host, args.port), args.filename, args.targetname, args.blksize, args.timeout)

# EOF
