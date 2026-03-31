import subprocess
import sys

def main():
    print("Starting build...")
    # Lệnh build cho Arduino Uno
    build_cmd = "arduino-cli compile --fqbn arduino:avr:uno firmware/blink.ino"
    
    result = subprocess.run(build_cmd, shell=True)
    
    if result.returncode == 0:
        print("Build Successful!")
    else:
        print("Build Failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
