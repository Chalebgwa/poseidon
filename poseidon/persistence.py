class Persistence:
    @staticmethod
    def add_registry_runkey(name: str, cmd: str):
        print(f"[PERSIST] Registry RunKey: {name} -> {cmd}")

    @staticmethod
    def schedule_task(name: str, cmd: str, interval: str):
        print(f"[PERSIST] Scheduled Task: {name}, every {interval}")

    @staticmethod
    def dll_hijack(service: str, dll_path: str):
        print(f"[PERSIST] DLL Hijack: {service} loads {dll_path}")
