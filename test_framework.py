#!/usr/bin/env python3

"""
Basic test script for the Poseidon APT simulation framework.
"""

import os
import sys
import subprocess

def test_import():
    """Test that all modules can be imported successfully."""
    print("Testing module imports...")
    
    try:
        from poseidon.anti_analysis import GhostKernel
        from poseidon.metamorphism import ChimeraEngine
        from poseidon.persistence import Persistence
        from poseidon.stealth_loader import StealthLoader
        from poseidon.shadow_move import ShadowMove
        from poseidon.exfiltration import DNSExfil, StegoExfil
        from poseidon.c2 import DGAEngine, PhantomProtocol, TorC2, CallbackProtocol
        from poseidon.ics import ICSAttacks
        from poseidon.mobile import MobileInfect
        from poseidon.devices import USBAttack, AudioCovert
        from poseidon.cloud import CloudEvasion
        from poseidon.rootkits import KernelRootkit, UEFIRootkit
        from poseidon.packer import Packer
        from poseidon.ai import AIAdversary
        from poseidon.selfdestruct import SelfDestruct, AutoSig
        from poseidon.infection import InfectionVectors
        from poseidon.replication import Replicator
        print("✓ All modules imported successfully")
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False

def test_safety_check():
    """Test that the safety check prevents unauthorized execution."""
    print("Testing safety mechanisms...")
    
    result = subprocess.run([sys.executable, "main.py"], 
                          capture_output=True, text=True, cwd=".")
    
    if result.returncode == 0 and "ERROR: Unauthorized environment" in result.stdout:
        print("✓ Safety check working - unauthorized access blocked")
        return True
    else:
        print("✗ Safety check failed")
        return False

def test_authorized_execution():
    """Test that the framework runs with proper authorization."""
    print("Testing authorized execution...")
    
    env = os.environ.copy()
    env["APT_RESEARCH_MODE"] = "approved"
    
    result = subprocess.run([sys.executable, "main.py"], 
                          capture_output=True, text=True, 
                          cwd=".", env=env, timeout=15)
    
    if result.returncode == 0 and "Poseidon APT simulation terminated safely" in result.stdout:
        print("✓ Authorized execution completed successfully")
        return True
    else:
        print("✗ Authorized execution failed")
        print("STDOUT:", result.stdout[-500:])  # Last 500 chars
        print("STDERR:", result.stderr[-500:])
        return False

def main():
    """Run all tests."""
    print("Running Poseidon APT Framework Tests")
    print("=" * 40)
    
    tests = [
        test_import,
        test_safety_check,
        test_authorized_execution
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()
        except Exception as e:
            print(f"✗ Test {test.__name__} crashed: {e}")
            print()
    
    print("=" * 40)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! Framework is fully functional.")
        return 0
    else:
        print("❌ Some tests failed.")
        return 1

if __name__ == "__main__":
    sys.exit(main())