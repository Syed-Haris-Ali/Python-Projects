
# Genrate QR CODE
# IMPORT QRCODE FROM PYQRCODE

import pyqrcode
import png
from pyqrcode import QRCode

s = "www.google.com"
# GENRATE QR CODE

url = pyqrcode.create(s)
url.svg("myqr.svg", scale=8)
url.png('myqr.png', scale=6)
