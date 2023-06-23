import time
import io
import base64
# from picamera import PiCamera
from PIL import Image

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


# def takePicture():
#     # Create an instance of PiCamera
#     camera = PiCamera()

#     # Capture the image
#     camera.start_preview()
#     time.sleep(5)  # wait for the camera to adjust to light conditions
#     image = io.BytesIO()
#     camera.capture(image, format='jpeg')
#     image.seek(0)
#     camera.stop_preview()
#     camera.close()

#     # Convert the image to bytes and encode it in base64
#     img_bytes = Image.open(image)
#     buffer = io.BytesIO()
#     img_bytes.save(buffer, format='JPEG')
#     img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

#     # Pass the base64-encoded image to the HTML template
#     return img_str
