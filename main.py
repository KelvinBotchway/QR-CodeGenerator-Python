import qrcode
from PIL import Image

data = "www.linkedin.com/in/kelvin-botchway-691148201"

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

#Create an image from the QR code
image = qr.make_image(fill="black", back_color="white")

#SAve the image
image.save("qr_code.png")
Image.open("qr_code.png")
