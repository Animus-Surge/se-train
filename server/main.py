# SE Train
# A Train Mod for Space Engineers
# 
# main.py - Main server entry point
# Author: Surge
# Date: Apr 20, 2026

from message import SETrainMsgHandler
from network import SETrainNetworkHandler

from loguru import logger

class SETrainServer:

    msg_handler = None
    network_handler = None
    
    def __init__(self):
        pass

    def start(self):
        pass


if __name__ == "__main__":
    SETrainServer().start()
