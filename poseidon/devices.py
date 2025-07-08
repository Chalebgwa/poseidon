class USBAttack:
    @staticmethod
    def rubber_ducky(script: str):
        print(f"[USB] Rubber Ducky payload: {script[:30]}...")

    @staticmethod
    def badusb(payload: bytes):
        print(f"[USB] BadUSB emulation, payload size {len(payload)} bytes")


class AudioCovert:
    @staticmethod
    def ultrasonic_beacon(data: bytes):
        print(f"[AUDIO] Ultrasonic beacon transmission, {len(data)} bytes")
