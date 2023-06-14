import os
import subprocess
import sys
import platform

# Clone the repository
subprocess.run(['git', 'clone', 'https://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@github.com/learn-co-curriculum/cyberOSTest.git'], check=True)
os.chdir('cyberOSTest')

# Detect the operating system
os_type = platform.system()

if os_type == 'Darwin':  # Mac OS
    # Install dependencies
    #subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements_mac.txt'], check=True)
    # Run the Python script
    subprocess.run([sys.executable, 'check_mac.py'], check=True)
elif os_type in ['Windows']:  # Windows
    # Install dependencies
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements_windows.txt'], check=True)
    # Run the Python script
    subprocess.run([sys.executable, 'check_windows.py'], check=True)
else:
    print("Unsupported operating system: ", os_type)
