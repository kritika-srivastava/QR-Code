#Kritika Srivastava
#April 26, 2020
#The given code encodes a given url or information in a qrcode.

import qrcode
import PIL
from PIL import Image

qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5

)
# You can add a text or a file depending upon your requirement.
# Eg-              data='Hello I am kritika'

data='https://github.com/kritika-srivastava'
# I added the link of my github profile....Cheers ;-)

qr.add_data(data)
qr.make(fit=True)

img=qr.make_image(fill_color="black",back_color="white") 
#Choosing the foreground and background colour of the qrcode generated 

img.save(r'C:\Users\Kritika\Desktop\VSC\python\QR-Code\images\profile_qr.png')
#Hint :Place the path of the directory in which you wamt to save the image along with its name.

#Uncomment the following to save the image in the same directory as this python file and comment line 27.
#Don't forget to change the image name to a desired name. ;-)
#img.save('profile_qr.png')







