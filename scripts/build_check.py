import os
import subprocess
import sys

def run_command(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error: Command failed with return code {result.returncode}")
        sys.exit(1)

def main():
    print("--- Starting Embedded CI Pipeline ---")
    
    # 1. Giả sử ta dùng Arduino-CLI để build
    # Lệnh build cho board Arduino Uno
    build_cmd = "arduino-cli compile --fqbn arduino:avr:uno firmware/blink.ino"
    run_command(build_cmd)
    
    print("--- Build Successful! ---")

if __name__ == "__main__":
    main()
