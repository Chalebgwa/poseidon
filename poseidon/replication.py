class Replicator:
    @staticmethod
    def network_share_copy(payload: bytes, shares: list):
        for share in shares:
            print(f"[REPLICATION] Copied payload to network share {share}")

    @staticmethod
    def removable_media_copy(payload: bytes, devices: list):
        for dev in devices:
            print(f"[REPLICATION] Copied payload to removable media {dev}")

    @staticmethod
    def ssh_bruteforce(hosts: list):
        for host in hosts:
            print(f"[REPLICATION] Simulated SSH brute-force against {host}")

    @staticmethod
    def container_deploy(image: str):
        print(f"[REPLICATION] Simulated deployment of malicious container image {image}")

    @staticmethod
    def cloud_function_injection(fn_name: str):
        print(f"[REPLICATION] Simulated injection into cloud function {fn_name}")

    @staticmethod
    def mqtt_propagation(brokers: list):
        for broker in brokers:
            print(f"[REPLICATION] Simulated MQTT propagation via broker {broker}")
