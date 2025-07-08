class DNSExfil:
    @staticmethod
    def tunnel(txt_chunks):
        for chunk in txt_chunks:
            print(f"[EXFIL/DNS] TXT query: {chunk}.exfil.example.com")


class StegoExfil:
    @staticmethod
    def embed_in_image(data: bytes):
        print(f"[EXFIL/STEGO] Embedded {len(data)} bytes into PNG")
