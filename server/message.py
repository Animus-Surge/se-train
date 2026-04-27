# message.py
#
# SETrain JSON message handler

from loguru import logger

class SETrainMsgHandler:
    
    def handle(self, msg, addr):

        if msg['type']:
            match msg['type']:
                case 'heartbeat':
                    logger.debug(f"Received heartbeat from {addr}")

                case _:
                    logger.error(f"Received invalid type {msg['type']} from {addr}")
        else:
            logger.error("Missing message type.")
