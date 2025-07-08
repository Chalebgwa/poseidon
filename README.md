# Poseidon APT Simulation Framework

Poseidon is a collection of simulated malware capabilities used exclusively for research and educational purposes. The project mimics an advanced persistent threat's toolkit without performing any real destructive actions. **It should never be deployed in a production environment.**

The main entry point is `main.py`, which coordinates calls to individual modules within the `poseidon` package. The environment variable `APT_RESEARCH_MODE` must be set to `"approved"` in order to run, acting as a simple safety check.

## Modules

- **anti_analysis.py** – Detects sandbox or debugger artifacts and prints decoy messages when analysis is suspected.
- **ai.py** – Demonstrates an adaptive threat that selects techniques based on a provided environment profile.
- **c2.py** – Implements command and control concepts including domain generation algorithms (DGA), peer-to-peer forwarding, Tor-based communication, and callback scheduling.
- **cloud.py** – Contains routines that detect common cloud environments and obfuscate potential indicators.
- **devices.py** – Simulates USB-based attacks and covert audio channel usage.
- **exfiltration.py** – Shows data exfiltration via DNS tunneling and basic steganography.
- **ics.py** – Illustrates attacks against industrial control protocols such as Modbus and DNP3.
- **infection.py** – Provides numerous infection vectors like drive‑by downloads, phishing, and supply‑chain compromise.
- **mobile.py** – Demonstrates mobile device attacks such as hooking Android apps or simulating an iOS jailbreak.
- **persistence.py** – Presents traditional persistence mechanisms like RunKeys, scheduled tasks, and DLL hijacking.
- **replication.py** – Simulates spreading the payload via network shares, removable media, and other channels.
- **rootkits.py** – Shows kernel and UEFI level persistence techniques.
- **selfdestruct.py** – Handles simulated cleanup by wiping memory or disk and producing example Sigma rules.
- **shadow_move.py** – Mimics credential harvesting and lateral movement within a network.
- **stealth_loader.py** – Demonstrates techniques for covertly loading code such as process hollowing and PowerShell execution.
- **metamorphism.py** – Provides a rudimentary metamorphic engine that modifies code to evade detection.
- **packer.py** – Stubs for packing and unpacking payloads.
- **utils.py** – Helper functions such as symmetric decryption used by other modules.

## Purpose

The purpose of Poseidon is to help defenders understand attacker tradecraft and build detection strategies. Each module logs its actions instead of performing real malicious activity. By studying how these components interact, security professionals can test detection rules and train analysts in a controlled environment.

