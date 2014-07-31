#------------------------------------------------------------------------------
# Name:     toplevel.py
# Purpose:  Top level controller for launching and controlling 
#           child processes
#
# Author:   jsafrit
# Created:  07/31/2014
#------------------------------------------------------------------------------
import serial
import shlex,subprocess
import time
import sys

def createVirtualComms(comm1='COM8', comm2='COM9'):
    '''create virtual com ports for testing link'''
    cmdline = 'socat PTY,link={} PTY,link={}'.format(comm1,comm2)
    args = shlex.split(cmdline)
    pComms = subprocess.Popen(args)
    #wait minimum time to ensure ports are up before returning
    time.sleep(1)
    if not pComms:
        print('Attempt to open comms failed. Exiting...')
        sys.exit(3)
    return pComms

def main():
    print('Calling {}...'.format('createVirtualComms'))
    toplevel = createVirtualComms()
    if toplevel:
        print('Sucessful!')   
        toplevel.terminate()
        
        
    

if __name__ == '__main__':
    main()