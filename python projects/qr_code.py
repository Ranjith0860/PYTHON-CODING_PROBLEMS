import qrcode

# Take input from user
data = input("Enter the QR code link to generate: ").strip()
file_name = input("Enter the file name to save (without extension or with extension): ").strip()

# Check if user gave an extension; if not, add .png
if not (file_name.endswith(".png") or file_name.endswith(".jpg")):
    file_name += ".png"

# Create QRCode object
qr = qrcode.QRCode(box_size=12, border=7)

qr.add_data(data)
qr.make(fit=True)

# Create image
image = qr.make_image(fill_color='black', back_color='white')

# Save the image
image.save(file_name)
print(f"QR Code saved as {file_name}")
