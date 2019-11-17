import sys
import os
import socket

directory = ''
fstring = ''

def printUsage():
	print('-------------------------------------------------------------------\n')
	print('Usage:')
	print('python pass-search.py string_to_search_for directory_to_be_searched\n')
	print('-------------------------------------------------------------------\n')


def validateArguments():
	if len(sys.argv) != 3:
		printUsage()
		return False
	elif os.path.isdir(sys.argv[2]) == False:
		print('Path you gave is not a directory')
		printUsage()
		return False
	else:
		global directory
		directory = sys.argv[2]
		global fstring
		fstring = sys.argv[1]
		return True


def check():
    for root, subdirs, files in os.walk(directory):
        for ffile in files:
            fpath = os.path.join(root, ffile)
            with open(fpath, "r") as f:
                datafile = f.readlines()
            for line in datafile:
                if fstring in line:
                    print(socket.getfqdn() + ' | ' + f.name)

if validateArguments() is True:
	print('\nSearching for ' + fstring + ' in ' + directory + '\n')
	check()
	print('\nEnd of searching')




