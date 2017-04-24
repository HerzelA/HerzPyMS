########################
## Author : HerzelA   ##
## Date   : 24/4/2017 ##
########################
#import sys
from Communication.PacketHandler.ClientLoginHandler import *
# The main server process, uses PacketHandler to connect to the client at first
def main():
	print "Hello to HerzMS python server!"
	loginPacketHandler()


if __name__ == "__main__":
    main()

