import qrcode
from pathlib import Path

def generate_qr_code(url: str, output_path: Path) -> Path:
    """
    Generate a QR code image for the given URL and save it to output_path.
    Returns the path to the saved image.
    """
    img = qrcode.make(url)
    img.save(output_path)
    return output_path
