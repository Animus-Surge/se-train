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

    running = True
    
    def __init__(self):
        self.msg_handler = SETrainMsgHandler()
        self.network_handler = SETrainNetworkHandler()

    def start(self):
        # Loop
        logger.info("Hello World!")

        while self.running:
            message = self.network_handler.poll()

            self.msg_handler.handle(message[0], message[1])
        
        logger.info("Goodbye!")


if __name__ == "__main__":
    SETrainServer().start()
