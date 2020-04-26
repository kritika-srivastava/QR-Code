#Kritika Srivastava
#April 26, 2020
#The given code decodes the given Qrcode and opens the website cooresponding to it.

from pyzbar.pyzbar import decode
#pyzbar is the alternative to opencv for this mini project

from PIL import Image 
# pillow is a package in python

import webbrowser 
#to let python open the linked webpage

d=decode(Image.open(r'C:\Users\Kritika\Desktop\VSC\python\QR-Code\images\profile_qr.png'))
# Saving the decoded in url
url=(d[0].data.decode())
webbrowser.open(url)
#Hurray the url opens a website ;-) 
# My GitHub profile though

#While displaying a simple message encoded in qrcode comment the line 17 and type:
#print(url)