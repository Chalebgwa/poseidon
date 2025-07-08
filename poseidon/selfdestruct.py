class SelfDestruct:
    @staticmethod
    def wipe_memory():
        print("[WIPE] Erasing memory artifacts")

    @staticmethod
    def wipe_disk():
        print("[WIPE] Simulating full disk wipe")


class AutoSig:
    @staticmethod
    def generate_sigma(events: list):
        print(f"[SIGGEN] Generated Sigma rule for events: {events}")
