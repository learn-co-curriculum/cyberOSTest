from colorama import init, Fore, Style
import platform
import os
import psutil

init(autoreset=True)

# Use colorama colors
class colors:
    OKGREEN = Fore.GREEN
    FAIL = Fore.RED
    OKBLUE = Fore.BLUE
    HEADER = Fore.CYAN

def evaluate_test(test_name, test_func):
    """Print test name and pass/fail depending on whether test_func returns True."""
    result = test_func()
    status = colors.OKGREEN + "pass" if result else colors.FAIL + "fail"
    print(f"{test_name:30} => [ {status} ]{Style.RESET_ALL}")

def check_os():
    """Check if the OS is either Windows or Linux."""
    return platform.system() in ['Windows', 'Linux']

def check_storage():
    """Check if the machine has at least 500GB of storage."""
    return psutil.disk_usage('/')[0] / (2**30) >= 500

def check_ram():
    """Check if the machine has at least 16GB of RAM."""
    return psutil.virtual_memory().total / (2**30) >= 16

def check_cpu():
    """Check if the CPU has a frequency of at least 2GHz."""
    return psutil.cpu_freq().max >= 2000

if __name__ == "__main__":
    print("\n" + colors.HEADER + "************ VALIDATING SETUP ************" + Style.RESET_ALL + "\n")
    print(colors.OKBLUE + "******************************************" + Style.RESET_ALL)

    evaluate_test("Windows or Linux", check_os)
    print(colors.OKBLUE + "******************************************" + Style.RESET_ALL)

    evaluate_test("At least 500GB storage", check_storage)
    print(colors.OKBLUE + "******************************************" + Style.RESET_ALL)

    evaluate_test("At least 16GB RAM", check_ram)
    print(colors.OKBLUE + "******************************************" + Style.RESET_ALL)

    evaluate_test("2GHz+ Processor", check_cpu)
    print(colors.OKBLUE + "******************************************" + Style.RESET_ALL)
