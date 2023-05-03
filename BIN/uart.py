import time

import serial
import serial.tools.list_ports
import threading
from threading import Thread
from copy import deepcopy


class Uart:
    def __init__(self):
        self.portList = []
        self.port = None
        self.receiveThread = None
        self.receiveBuf = "".encode('utf-8')
        self.lock = threading.Lock()

    def findPort(self):
        self.portList = list(serial.tools.list_ports.comports())
        if len(self.portList) > 0:
            print(list(self.portList[0]))
            return list(self.portList[0])
        else:
            return []

    def openPort(self, port, baudRate, byteSize, parity, stopBits):

        if byteSize == "5":
            byteSize = serial.FIVEBITS
        elif byteSize == "6":
            byteSize = serial.SIXBITS
        elif byteSize == "7":
            byteSize = serial.SEVENBITS
        else:
            byteSize = serial.EIGHTBITS

        if parity == "奇校验":
            parity = serial.PARITY_ODD
        elif parity == "偶校验":
            parity = serial.PARITY_EVEN
        else:
            parity = serial.PARITY_NONE

        if stopBits == "1":
            stopBits = serial.STOPBITS_ONE
        elif stopBits == "1.5":
            stopBits = serial.STOPBITS_ONE_POINT_FIVE
        else:
            stopBits = serial.STOPBITS_TWO

        self.port = serial.Serial(port=port, baudrate=int(baudRate), bytesize=byteSize, parity=parity, stopbits=stopBits)
        if self.port.isOpen():
            self.receiveThread = Thread(target=self.receiveLoop)
            return True, "串口打开成功."
        else:
            return False, "串口打开失败."

    def closePort(self):
        if self.port is not None:
            self.port.close()
        self.port = None

    def transmit(self, data):
        if self.port is None:
            return False
        self.port.write(data.encode('utf-8'))

    def receiveLoop(self):

        while self.port is not None and self.port.isOpen:
            self.lock.acquire()
            self.receiveBuf += self.port.readline()
            self.lock.release()

    def receive(self):
        if not self.lock.acquire(False):
            return "".encode('utf-8')
        else:
            return deepcopy(self.receiveBuf)


uart = Uart()
