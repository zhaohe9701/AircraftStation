import threading
import time
from threading import Thread
from uart import uart


class MessageServer:
    def __init__(self):
        self.receiveThread = Thread(target=self.receiveLoop)
        self.keep = True
        self.openUartReceive = True
        self.sendToTerminal = False
        self.terminal = None
        self.processorList = []

    def registerProcessor(self, processor):
        self.processorList.append(processor)

    def start(self):
        self.receiveThread.start()

    def stop(self):
        self.keep = False
        self.receiveThread.join()

    def receiveLoop(self):
        while self.keep:
            if self.openUartReceive and uart.port is not None and uart.port.isOpen:
                receiveBuf = uart.port.read(1000)
                for processor in self.processorList:
                    processor.inputData(receiveBuf)
                time.sleep(0.01)
            else:
                time.sleep(0.1)

    def send(self, data):
        if self.openUartReceive and uart.port is not None and uart.port.isOpen:
            uart.transmit(data)
