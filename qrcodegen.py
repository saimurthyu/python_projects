import qrcode

def generate_qrcode(text):

    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(color="black",back_color="white")
    img.save("pavan1.png")

generate_qrcode('''Hlo sikku fafa
                Idigo puvvu 🌼 
Nvante lovvu <3''')    