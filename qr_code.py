import qrcode as qr

image = qr.make("https://github.com/VinayakPJadhav")
image.save("MyGitHub_QR.png")