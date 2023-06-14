#!/bin/bash

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
    python check_windows.py
else
    echo "Unsupported operating system: ${os}"
fi
