class KernelRootkit:
    @staticmethod
    def dk_object_hide(pid: int):
        print(f"[RK] Simulated DKOM hide of PID {pid}")

    @staticmethod
    def hook_syscall(number: int):
        print(f"[RK] Hooked syscall number {number}")


class UEFIRootkit:
    @staticmethod
    def install():
        print("[UEFI] Simulated UEFI bootkit installation")

    @staticmethod
    def persist():
        print("[UEFI] Shadow bootloader written to NVRAM")
