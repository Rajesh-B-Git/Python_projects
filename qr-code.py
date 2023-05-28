# install pip install PyQRCode package
# install pip install pypng package


import pyqrcode

url = input("ENter URL to generate QR code : \n")
QR = pyqrcode.create(url)
QR.png("webqr.png", scale=8)
