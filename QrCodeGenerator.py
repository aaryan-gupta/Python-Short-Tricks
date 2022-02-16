import pyqrcode # pip install pyqrcode
import png # pip install pypng
from pyqrcode import QRCode
s = "google.com"
url = pyqrcode.create(s)
url.svg("myqr.svg", scale=8)
url.png("myqr.png", scale=8)