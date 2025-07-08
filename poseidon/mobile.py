class MobileInfect:
    @staticmethod
    def android_hook(app_name: str):
        print(f"[MOBILE] Hooked Android app {app_name}")

    @staticmethod
    def ios_jailbreak(device_id: str):
        print(f"[MOBILE] Simulated iOS jailbreak on {device_id}")
