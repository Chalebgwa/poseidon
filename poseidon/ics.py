class ICSAttacks:
    @staticmethod
    def modbus_read(address: str, register: int):
        print(f"[ICS] Modbus READ from {address}, register {register}")

    @staticmethod
    def dnp3_attack(master: str, slave: str):
        print(f"[ICS] DNP3 Attack: {master} -> {slave}")
