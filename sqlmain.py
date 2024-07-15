import sys
import time
from art import *
import scan

# MESSAGE
WARNING_MESSAGE = f"[warning]\t"
ERROR_MESSAGE = f"[error]\t"
INFO_MESSAGE = f"[info]\t"


def get_input(prompt):
    try:
        user_input = input(prompt)
        args = user_input.split()
        if args[0] != 'sqli':
            return None
        return args
    except Exception as e:
        print(f"[Error]: {e}")
        return None


def check_list(lst):
    setTemp = set(lst)
    if len(setTemp) == len(lst):
        for ele in setTemp:
            if ele.isdigit() is False:
                return False
            if int(ele) < 1 or int(ele) > 4:
                return False
        return True
    return False


def banner_func():
    with open('data/banner.txt', 'r') as file:
        content = file.read()
    print(content)


def help_func():
    with open('data/help.txt', 'r') as file:
        content = file.read()
    print(content)


def scan_func():
    url = None
    # Verify URL
    while True:
        url = input("\turl:\t")
        resScan = scan.scan_url(url)
        print("\t" + resScan[0])
        if resScan[1] == "1":
            break

    # Choose MODE
    while True:
        try:
            n_mode = int(input("\tMode\t > "))
            if n_mode == 1:
                # Thuc hien Normal mode
                print("\t" + INFO_MESSAGE + "Mode: NORMAL")
                scan.scan_vulnerability(url, 'Normal')
                break
            elif n_mode == 2:
                # Thuc hien Time Base mode
                print("\t" + INFO_MESSAGE + "Mode: Time Base")
                scan.scan_vulnerability(url, 'Time Base')
                break
            elif n_mode == 3:
                # Thuc hien Custom mode
                print("\t" + INFO_MESSAGE + "Mode: Custom")
                scan.scan_vulnerability(url, 'Custom')
        except ValueError:
            print("\t" + WARNING_MESSAGE + "Invalid mode. Please choose again.")
            continue

    return


if __name__ == "__main__":
    banner_func()
    while True:
        userinput = get_input(" >> ")
        if userinput is None:
            print(ERROR_MESSAGE + "\tundefined syntax")
            continue
        else:
            if userinput[1] == '-help':
                help_func()
            elif userinput[1] == '-scan':
                scan_func()
            elif userinput[1] == '-detect':
                print(INFO_MESSAGE + "\tnot available now")
            elif userinput[1] == '-exit':
                break
            else:
                print(ERROR_MESSAGE + "\tundefined option")
