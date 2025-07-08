import base64
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def decrypt_string(data_b64, key=None):
    """Reverse AES-CBC encrypted, Base64-encoded string."""
    try:
        raw = base64.b64decode(data_b64)
        iv, ct = raw[:16], raw[16:]
        key = key or b"\x00" * 32
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(128).unpadder()
        decrypted = decryptor.update(ct) + decryptor.finalize()
        return unpadder.update(decrypted) + unpadder.finalize()
    except Exception:
        return b""
