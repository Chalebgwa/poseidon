class StealthLoader:
    @staticmethod
    def process_hollow(target: str, payload: bytes):
        print(f"[STEALTH] Process hollowing into {target}, payload size {len(payload)} bytes")

    @staticmethod
    def load_via_wmi(script: str):
        print(f"[STEALTH] WMI Script Execution: {script[:30]}...")

    @staticmethod
    def load_via_powershell(cmd: str):
        print(f"[STEALTH] PowerShell Exec: {cmd[:40]}...")
