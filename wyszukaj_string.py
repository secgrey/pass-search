import sys
import os
import socket

directory = sys.argv[2]
fstring = sys.argv[1]

def check():
    for root, subdirs, files in os.walk(directory):
        for ffile in files:
            fpath = os.path.join(root, ffile)
            with open(fpath, "r") as f:
                datafile = f.readlines()
            for line in datafile:
                if fstring in line:
                    print(socket.getfqdn() + ' | ' + f.name)

check()




