import qrcode
from PIL import Image
print("Enter QR Code dimensions & design characteristics: ")
b_size=int(input("Box size= "))
border_thickness=int(input("Border size= "))
f_color=input("QR fill color: ")
background_color=input("Background color: ")
url=input("Enter url=  ")

qr=qrcode.QRCode(version=1, 
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=b_size,border=border_thickness)

qr.add_data(url)
qr.make(fit=True)
img=qr.make_image(fill_color=f_color.lower(),back_color=background_color.lower())
img.save("qrcode.png")