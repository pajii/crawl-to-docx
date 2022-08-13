import os
import importlib.util as importutil
import sys

# I want to make this gui

# region requirements

MAIN_PATHS = {
    "data_dir": r'./data',
    "already_in_data": r'./data/already_in_data',
    "documents": r'./documents',
    "modules": r'./modules',
    "chrome": r'./data/chromedriver.exe'
}
DISPLAY_PROCESS = True
PROCESS_LINE_LENGTH = 50

MODULE_REQUIREMENTS = \
    ['os', 'pandas', 'numpy', 'bs4', 'PIL', 'copy', 'selenium', 'shutil', 'docx' ]


# endregion

# region functions

# region checking requirements


def check_directory_and_files(display_process: bool = False) -> None:
    global PROCESS_LINE_LENGTH, MAIN_PATHS
    if display_process:
        print("=" * PROCESS_LINE_LENGTH)
        print("  checking directory & files..")

    for key, path in MAIN_PATHS.items():
        if display_process:
            print(f"  check path {key} : {path}", end='')

        if os.path.exists(path):
            if display_process:
                print(" [True]")
        else:
            if display_process:
                print(" [False]")
            # make dir or exit
            if '.' in os.path.basename(path):
                print(f"!!! you must have {key} file '{path}'")
                _ = input()
                exit()
            else:
                print(f'!  creating data directory in {path}')
                os.mkdir(MAIN_PATHS['data_dir'])
    if display_process:
        print("  *done*")


def check_modules(display_process: bool = False) -> None:
    global PROCESS_LINE_LENGTH, MODULE_REQUIREMENTS
    if display_process:
        print("=" * PROCESS_LINE_LENGTH)
        print("  checking modules")
    not_exist_modules = [module_name for module_name in MODULE_REQUIREMENTS
                         if importutil.find_spec(module_name) is None]
    if display_process:
        for module_name in MODULE_REQUIREMENTS:
            print(f"  check module : {module_name} [{not module_name in not_exist_modules}]")
    if len(not_exist_modules) != 0:
        print(f"!  there is no module in python : {', '.join(not_exist_modules)}")
        _ = input()
        exit()
    print("  *done*")

# endregion


def import_modules(display_process: bool = False) -> None:
    if display_process:
        print("=" * PROCESS_LINE_LENGTH)
        print("  import modules")


# endregion

# region run section

# checking requirements
print('=' * PROCESS_LINE_LENGTH)

check_directory_and_files(DISPLAY_PROCESS)
check_modules(DISPLAY_PROCESS)

import_modules(DISPLAY_PROCESS)

print('=' * PROCESS_LINE_LENGTH)
# csv_data format : [site][category][date_make](comment).csv
print("  checking data..")

print("  최근에 저장한 파일 체크중..")

from modules import data_manager

print("최근에 저장한 파일이 없습니다.")

print(f"최근에 저장한 날짜 : ")

# endregion
