import os


class CloudEvasion:
    @staticmethod
    def detect_aws():
        if os.path.exists('/sys/hypervisor/uuid'):
            print("[CLOUD] AWS environment detected")

    @staticmethod
    def detect_gcp():
        print("[CLOUD] GCP metadata API probe simulated")

    @staticmethod
    def evade():
        print("[CLOUD] Obfuscating cloud SDK artifacts")
