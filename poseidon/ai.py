import random


class AIAdversary:
    @staticmethod
    def choose_ttp(env_profile: dict):
        ttp = random.choice(["process_hollow", "kerberoast", "dns_exfil", "pth"])
        print(f"[AI] Selected TTP: {ttp} for environment {env_profile}")
