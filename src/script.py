# Import packages
import qrcode

# QR function
def generate_qr(data: str,
                filename: str = "qrcode.png",
                version: int = 1,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size: int = 10,
                border: int = 4) -> None:
    """
    Generate a QR code image.

    Args:
        data: The text or URL to encode.
        filename: Output file name (PNG).
        version: An integer from 1 to 40 that controls the size of the QR code.
                 Higher numbers = bigger code, more data capacity.
        error_correction: The error correction level.
                          ONE OF: ERROR_CORRECT_L, ERROR_CORRECT_M,
                                  ERROR_CORRECT_Q, ERROR_CORRECT_H
        box_size: Pixel size of each “box” in the QR code.
        border: Width (in boxes) of the white border around the QR code.
    """
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved to {filename}")

generate_qr("https://github.com/danielan987", "github_profile.png")
