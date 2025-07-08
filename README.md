```
    ____  ____  _____ ______________  ____  _   __
   / __ \/ __ \/ ___// ____/  _/ __ \/ __ \/ | / /
  / /_/ / / / /\__ \/ __/  / // / / / / / /  |/ /
 / ____/ /_/ /___/ / /____/ // /_/ / /_/ / /|  /
/_/    \____//____/_____/___/_____/\____/_/ |_/
```

# Poseidon APT Simulation Framework

```
      /\\
     /  \\
    / /\\ \\
   / /  \\ \\
  /_/    \\_\\
    |  |
    |  |
    |  |
    |  |
```

Poseidon is a collection of simulated malware capabilities used exclusively for research and educational purposes. The project mimics an advanced persistent threat's toolkit without performing any real destructive actions. **It should never be deployed in a production environment.**

The main entry point is `main.py`, which coordinates calls to individual modules within the `poseidon` package. The environment variable `APT_RESEARCH_MODE` must be set to `"approved"` in order to run, acting as a simple safety check.

## Modules

| Module | Description |
|--------|-------------|
| `anti_analysis.py` 🛡️ | Detects sandbox or debugger artifacts and prints decoy messages when analysis is suspected. |
| `ai.py` 🤖 | Adaptive threat that selects techniques based on a provided environment profile. |
| `c2.py` 🌎 | Command and control examples: DGA, peer-to-peer forwarding, Tor, callbacks. |
| `cloud.py` ☁️ | Detects common cloud environments and obfuscates indicators. |
| `devices.py` 📱 | Simulates USB-based attacks and covert audio channel usage. |
| `exfiltration.py` 📦 | Data exfiltration via DNS tunneling and basic steganography. |
| `ics.py` ⚙️ | Illustrates attacks on industrial protocols such as Modbus and DNP3. |
| `infection.py` 🌧️ | Drive‑by downloads, phishing, and supply‑chain compromise. |
| `mobile.py` 📲 | Demonstrates mobile device attacks on Android and iOS. |
| `persistence.py` 🔍 | RunKeys, scheduled tasks, and DLL hijacking. |
| `replication.py` 🔧 | Spreading via network shares and removable media. |
| `rootkits.py` 🛠️ | Kernel and UEFI level persistence techniques. |
| `selfdestruct.py` 🗑️ | Simulated cleanup and example Sigma rules. |
| `shadow_move.py` 📣 | Credential harvesting and lateral movement. |
| `stealth_loader.py` 🔮 | Covert code loading like process hollowing. |
| `metamorphism.py` 🧃 | Rudimentary metamorphic engine for evasion. |
| `packer.py` 🗃️ | Stubs for packing and unpacking payloads. |
| `utils.py` 🔎 | Helper functions like symmetric decryption. |

## Purpose

The purpose of Poseidon is to help defenders understand attacker tradecraft and build detection strategies. Each module logs its actions instead of performing real malicious activity. By studying how these components interact, security professionals can test detection rules and train analysts in a controlled environment.
