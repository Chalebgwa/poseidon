class InfectionVectors:
    @staticmethod
    def drive_by_download(url: str):
        print(f"[INFECTION] Simulated drive-by download from {url}")

    @staticmethod
    def email_phishing(recipient: str, attachment: str):
        print(f"[INFECTION] Simulated phishing email to {recipient} with {attachment}")

    @staticmethod
    def watering_hole(site: str):
        print(f"[INFECTION] Simulated watering-hole compromise of {site}")

    @staticmethod
    def usb_autorun(device: str):
        print(f"[INFECTION] Simulated USB autorun on {device}")

    @staticmethod
    def supply_chain(pkg_name: str):
        print(f"[INFECTION] Simulated supply-chain compromise via {pkg_name}")

    @staticmethod
    def container_escape(container_id: str):
        print(f"[INFECTION] Simulated container escape from {container_id}")

    @staticmethod
    def mobile_sms_link(number: str, link: str):
        print(f"[INFECTION] Simulated SMS lure to {number} with link {link}")
