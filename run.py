import os
import sys
import platform
import subprocess

arc = None

print(f' •\x1b[38;5;196m ->\x1b[37m CHECKING FOR UPDATES ')
os.system('git pull --quiet')

def main():
    global arc
    architecture = platform.architecture()
    
    if architecture[0] == '32bit':
        arc = "32BIT"
        sys.exit(f' •\x1b[38;5;196m ->\x1b[37m 32BIT NOT SUPPORTED')
    
    elif architecture[0] == '64bit':
        arc = "64BIT"
        print(f' •\x1b[38;5;196m ->\x1b[37m 64BIT DETECTED')
        print(f' •\x1b[38;5;196m ->\x1b[37m STARTING Grgzz ')
        
        try:
            import data.HARRY64
        except ImportError:
            sys.exit("ERROR: data.HARRY64 module not found!")
    
    else:
        arc = "INVALID"
        sys.exit("•\x1b[38;5;196m ->\x1b[37m UNKNOWN DEVICE TYPE")

if __name__ == "__main__":
    main()