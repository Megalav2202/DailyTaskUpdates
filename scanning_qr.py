from pyzbar.pyzbar import decode
from PIL import Image

def scan_qr_code(image_path):
    # Load image
    img = Image.open(image_path)

    # Decode QR code
    decoded_objects = decode(img)

    # Extract URL
    for obj in decoded_objects:
        if obj.type == 'QRCODE':
            return obj.data.decode('utf-8')

    return None

# Example usage:
if __name__ == "__main__":
    qr_code_path = "C:/Users/megalav/Downloads/qr-code (1).png"  # Replace with your QR code image path
    scanned_url = scan_qr_code(qr_code_path)
    if scanned_url:
        print("Scanned URL:", scanned_url)
    else:
        print("No QR code found or couldn't extract URL.")
