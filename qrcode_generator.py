import qrcode
from PIL import Image
# image = qr.make('https://kitabkinbech.pythonanywhere.com/')

# image.save('kitabkinbech.png')


qr = qrcode.QRCode(version=1,error_correction= qrcode.ERROR_CORRECT_H, box_size=10,border=4)
qr.add_data('https://kitabkinbech.pythonanywhere.com')
qr.make(fit=True)
img = qr.make_image(fill_color = 'red',back_color = 'white')
img.save('kitabkinbech.jpg')