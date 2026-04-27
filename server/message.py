# message.py
#
# SETrain JSON message handler

from loguru import logger

class SETrainMsgHandler:
    
    def handle(self, msg, addr):

        if len(msg) == 0: return  # Do nothing in the event of
                                  # an empty message (i.e. poll
                                  # returned nothing)

        if msg['type']:
            match msg['type']:
                case 'heartbeat':
                    logger.debug(f"Received heartbeat from {addr}")

                case _:
                    logger.error(f"Received invalid type {msg['type']} from {addr}")
        else:
            logger.error("Missing message type.")
