#! /usr/bin env python
# -*- conding: utf-8 -*-

import serial

class Controllers:
    def managerluz(self, argumento):
        try:
            ser = serial.Serial('/dev/ttyACM0', 9600)
            if argumento == 0:
                ser.write(b'0')
                return 'desligar'
            elif argumento == 1:
                ser.write(b'1')
                return 'ligar'
        except ValueError:
            return 'Ocorreu uma falha interna no sistema'
