import os
import sys

# I want to make this gui
print("hello world\n")

MAIN_PATHS = {
    "data_dir": r'./data',
    "already_in_data": r'./data/already_in_data',
    "documents": r'./documents',
    "modules": r'./modules',
    "chrome": r'./data/chromedriver.exe'
}
REQUIRED_MODULE = {
    "data_manager" : ["pandas", "numpy", "error_test"]
}

line_length = 50

#functions
def check_exist_modules(module_name: str, print_message: bool):
    global REQUIRED_MODULE
    for i_module_name in REQUIRED_MODULE[module_name]:
        if i_module_name not in sys.modules:
            print("dsg")

# check directory
print("=" * line_length)
print("  checking directory & files..")
if not os.path.exists(MAIN_PATHS['data_dir']):
    print("!  you don't have a data directory")
    print(f"!  creating data directory in '{MAIN_PATHS['data_dir']}'..")
    os.mkdir(MAIN_PATHS['data_dir'])

if not os.path.exists(MAIN_PATHS['already_in_data']):
    print("!  you don't have a already_in_data directory")
    print(f"!  creating already_in_data directory in '{MAIN_PATHS['already_in_data']}'..")
    os.mkdir(MAIN_PATHS['already_in_data'])

if not os.path.exists(MAIN_PATHS['documents']):
    print("!  you don't have a documents directory")
    print(f"!  creating documents directory in '{MAIN_PATHS['documents']}'..")
    os.mkdir(MAIN_PATHS['documents'])

if not os.path.exists(MAIN_PATHS['modules']):
    print("!  you don't have a modules directory")
    print("!!! if you don't have modules, you can't use this programs")
    _ = input()
    exit()
print(" *done*")

# checking requirements
print('=' * line_length)
print("  checking requirements..")
if not os.path.exists(MAIN_PATHS["chrome"]):
    print(f"!!! you should download chromedriver.exe in '{os.path.dirname(MAIN_PATHS['chrome'])}'")
    _ = input()
    exit()
print(" *done*")


print('=' * line_length)
# csv_data format : [site][category][date_make](comment).csv
print("  checking data..")
print("  checking modules..")

print("  최근에 저장한 파일 체크중..")
from modules import data_manager




print("최근에 저장한 파일이 없습니다.")

print(f"최근에 저장한 날짜 : ")
