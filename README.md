# QRcode Generator and Reader
&nbsp;

#### *Welcome to QRcode Generator and Reader’s documentation! Here, I shall give an overview of all the things you need to know to get started with this project.*
&nbsp;

![](images/hii.png)
&nbsp;

&nbsp;

*This mini project is divided in two parts ,i.e,Qrcode Generator and Qrcode Reader respectively.*
&nbsp;

## [![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/kritika-srivastava/Random-Password-Generator/blob/master/LICENSE)![Project Status](https://img.shields.io/badge/Project-Completed-orange)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
![Python Badge](https://img.shields.io/badge/Python-3.5%7C3.6%7C3.7-success)
![PyPi Dependency](https://img.shields.io/badge/PyPi-pyzbar-critical)

## Technical Stack
###### - Pyzbar (Python)
###### - Qrcode (Python)
###### - PIL (pillow-Python)
###### - Anaconda
###### - Webbrowser (Python)

&nbsp;


## Installing required Plugins
#### *The installation procedure is written keeping anaconda distribution as the base. However you can install the given plugins in any distribution.*
Open the anaconda prompt and activate your environment (if you prefer to work in any other virtual environment other than base) by typing the following command.
``` 
conda activate your_env_name  
```

*Run the given command in the anaconda prompt to install pyzbar.*
``` 
pip install pyzbar  
```
A list of package to be installed or to be updated shall appear on terminal and you will be prompted to select [y/n].Select y and press Enter.Now wait till the package is installed .
&nbsp;

*Run the given command in the anaconda prompt to install pyzbar.*
``` 
pip install PyQRCode  
```
*Run any one of the given commands in the anaconda prompt to install PIL(pillow).*
``` 
conda install -c anaconda pillow 
conda install pillow 
```
*Webbrowser is in-built in anaconda.*
&nbsp;

As of now, this project runs on Python 3.x . Make sure that all the given should be installed in any of your python distributions. To start the program first clone this [github repository](https://github.com/kritika-srivastava/QR-Code).
&nbsp;

## Steps to generate Qrcode
#### *First open your IDE and activate the virtual environment in which all the plugins are installed*
- To generate the Qr code open the QR Code Generator folder and then open the [Generator.py](https://github.com/kritika-srivastava/QR-Code/blob/master/QR%20Code%20Generator/Generator.py) file. Change the link to the link of your website or type your message and run the python file.
- Make sure you change the path of the directory in which you want to save the png image of qrcode. In case of saving the image in the current directory, just specify the name of image within the quotes.
&nbsp;

If everything worked so far, the png image should be made in the directory. Open the image and it should look something like this:
&nbsp;

<img src="images/profile_qr.png">
&nbsp;

## Steps to read Qrcode
#### *First open your IDE and activate the virtual environment in which all the plugins are installed*
- To read the Qr code open the QR Code Reader folder and then the [reader.py](https://github.com/kritika-srivastava/QR-Code/blob/master/QR%20Code%20Reader/reader.py) file.
- Now run the file.
  &nbsp;

If everything worked so far, the browser should open and display the website/message cooresponding to the qrcode.
&nbsp;


        
## References
#### -[PyPi: Qrcode ](https://pypi.org/project/qrcode/)
#### -[PyPi: Pyzbar](https://pypi.org/project/pyzbar/)


