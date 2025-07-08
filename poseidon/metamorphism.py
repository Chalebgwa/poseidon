import os
import random
import re
import base64
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from .utils import decrypt_string


class ChimeraEngine:
    def __init__(self):
        self.key = os.urandom(32)
        self.iteration = 0

    def metamorphic_transform(self, code: str) -> str:
        self.iteration += 1
        transforms = [
            self._insert_junk_code,
            self._control_flow_obfuscation,
            self._encrypt_string_literals,
            self._variable_renaming
        ]
        for _ in range(random.randint(2, 4)):
            code = random.choice(transforms)(code)
        print(f"[CHIMERA] Metamorphic iteration {self.iteration}")
        return code

    def _insert_junk_code(self, code: str) -> str:
        junk = [
            "for _ in range(7): pass",
            "x = 0xDEADBEEF; x ^= 0xCAFEBABE",
            "None if random.random() > 0.5 else None"
        ]
        i = random.randint(0, len(code))
        return code[:i] + "\n" + random.choice(junk) + "\n" + code[i:]

    def _control_flow_obfuscation(self, code: str) -> str:
        return re.sub(
            r"if (.+?):",
            r"flag = \1; while flag: flag = False;",
            code
        )

    def _encrypt_string_literals(self, code: str) -> str:
        literals = re.findall(r'"([^"]+)"', code)
        for s in set(literals):
            iv = os.urandom(16)
            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
            padder = padding.PKCS7(128).padder()
            padded = padder.update(s.encode()) + padder.finalize()
            ct = cipher.encryptor().update(padded) + cipher.encryptor().finalize()
            b64 = base64.b64encode(iv + ct).decode()
            code = code.replace(f'"{s}"', f'decrypt_string("{b64}", key=engine.key)')
        return code

    def _variable_renaming(self, code: str) -> str:
        vars_found = set(re.findall(r"\b([a-z_][a-z0-9_]{2,})\b", code))
        for var in vars_found:
            new_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8))
            code = re.sub(rf"\b{var}\b", new_name, code)
        return code
