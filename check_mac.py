import os
import subprocess
import platform

# ANSI color codes
NC = '\033[0m'
RED = '\033[0;31m'
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
CYAN = '\033[0;36m'

def evaluate_test(command, comparator, required_value):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
        result = result.stdout.decode('utf-8').strip()
        # Compare the output with the required value
        if comparator(result, required_value):
            return "pass", True
        else:
            return "fail", False
    except subprocess.CalledProcessError:
        return "fail", False

def print_table_results(name, command, comparator=lambda x, y: True, required_value=None):
    result, success = evaluate_test(command, comparator, required_value)
    color = GREEN if success else RED
    print(f"{name:<30} => [ {color}{result if result else 'fail'}{NC} ]")

def print_delimiter():
    print(f"{BLUE}{'*'*40}{NC}")

def print_header(header):
    print(f"\n{CYAN}{'*'*12} {header} {'*'*12}{NC}\n")

# Validation
print_header("VALIDATING SETUP")
print_delimiter()

# 1. Windows or Linux
os_comparator = lambda x, y: x == 'Linux' or x.startswith('MINGW')
print_table_results("Windows or Linux", "uname -s", comparator=os_comparator)
print_delimiter()

# 2. At least 500GB storage
print_table_results("At least 500GB storage", "df -k / | tail -n 1 | awk '{print $4}'", comparator=lambda x, y: int(x) >= y, required_value=500*1024*1024)  # Comparing in KB
print_delimiter()

# 3. At least 16GB RAM
print_table_results("At least 16GB RAM", "sysctl -n hw.memsize", comparator=lambda x, y: int(x) >= y, required_value=16*1024*1024*1024)  # Comparing in Bytes
print_delimiter()

# 4. 2GHz+ Processor
def cpu_speed_comparator(result, required_value):
    speed = result.split('@')[1].strip()
    speed = float(speed[:-3])  # Removing 'GHz' and converting to float
    return speed >= required_value

print_table_results("2GHz+ Processor", "sysctl -n machdep.cpu.brand_string", comparator=cpu_speed_comparator, required_value=2.0)  # Comparing in GHz
print_delimiter()

