import qrcode
import re
import validators

def is_valid_filename(filename):
    return re.match(r'^[a-zA-Z0-9_-]+(\.png)?$', filename) is not None

def is_valid_url(url):
    return validators.url(url)  # Using the validators library to check if the URL is valid

def generate_QR_code_from_URL(URL, filename, version=None, box_size=10, border=5):
    if not filename.lower().endswith(".png"):
        filename += "_QR.png"
    
    QR = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    QR.add_data(URL)
    QR.make(fit=True)
    
    img = QR.make_image(fill='black', back_color='white')
    img.show()  # Display the QR code
    img.save(filename)  # Save the QR code as an image file
    print(f"QR code saved as '{filename}'")

if __name__ == "__main__":
    url = input("Enter the URL to generate a QR code: ")
    while not is_valid_url(url):
        print("Invalid URL. Please enter a valid URL (e.g., https://example.com).")
        url = input("Enter the URL to generate a QR code: ")
    
    while True:
        filename = input("Enter the filename to save the QR code (without extension or with .png): ")
        if is_valid_filename(filename):
            break
        print("Invalid filename. Use only letters, numbers, hyphens, and underscores.")
    
    generate_QR_code_from_URL(url, filename)
