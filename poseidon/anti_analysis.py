import os
import time
import random
import ctypes
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
