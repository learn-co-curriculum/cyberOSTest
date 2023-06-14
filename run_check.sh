#!/bin/bash
git clone https://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@github.com/learn-co-curriculum/cyberOSTest.git && cd cyberOSTest
# Detect the operating system
os="$(uname -s)"

if [[ "${os}" == "Darwin" ]]; then  # Mac OS
    # Install dependencies
    #pip install -r requirements_mac.txt
    # Run the Python script
    python3 check_mac.py
elif [[ "${os}" == "MINGW"* ]] || [[ "${os}" == "MSYS"* ]] || [[ "${os}" == "Windows"* ]]; then  # Windows
    # Install dependencies
    pip install -r requirements_windows.txt
    # Run the Python script
    python3 check_windows.py
else
    echo "Unsupported operating system: ${os}"
fi
