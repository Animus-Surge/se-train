# network.py - UDP socket communication module
#
# Handles communication to and from the server and the mod.
#
# Author: Surge

import json
import socket
import time

from loguru import logger

PORT = 11000
MOD_PORT = 11001

class SETrainNetworkHandler:

    def __init__(self, host="127.0.0.1", port=PORT, mod_port=MOD_PORT):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((host, port))

        self.sock.setblocking(False)

        self.in_msg_buffer = []

        self.mod_port = mod_port
        self.clients = {}
        self.timeout = 10.0

    def update(self):
        # RX block
        try:
            while True:
                data, addr = self.sock.recvfrom(4096)
                try:
                    msg = json.loads(data.decode())
                    self.in_msg_buffer.append((msg, addr))
                except json.JSONDecodeError:
                    logger.warning(f"Received malformed JSON from {addr}")
                
        except (BlockingIOError, socket.error):
            pass # Ignore

        # TX block


    def poll(self):
        if self.in_msg_buffer:
            return self.in_msg_buffer.pop(0)
        return {}, None


    def send(self, ip, msg):
        json_string = json.dumps(msg)
        try:
            self.sock.sendto(json_string.encode(), (ip, self.mod_port))
        except Exception as e:
            logger.error(f"Failed to send to {ip}. Message: {json_string}\n{e.with_traceback()}")

