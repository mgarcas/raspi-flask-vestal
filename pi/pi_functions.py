"""
File: pi_functions.py
Author: mgarcas
Date: June 8, 2023

Description: This file contains Python functions for Raspberry Pi Flask App raspi_flask_vestal.

Usage: Execute this script to display a greeting message.

License: This file is distributed under the MIT license.
"""


def getTemp():
    try:
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            temp = f.read()
            f.close()
            return int(temp)/1000
    except Exception as e:
        return 'You are not probably in your Pi, error {}'.format(e)


def C_to_F(C):
    return (C * 9/5) + 32
