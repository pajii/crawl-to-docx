# region main import
import os
import sys

# endregion

# I want to make this gui
print("hello world\n")

MAIN_PATHS = {
    "data_dir": r'./data',
    "already_in_data": r'./data/already_in_data',
    "documents": r'./documents',
    "modules": r'./modules',
    "chrome": r'./data/chromedriver.exe'
}

line_length = 50

process_line_length = 50


# region functions

# region checking requirements
def check_directory_and_files(display_process: bool = False) -> None:
    global line_length, MAIN_PATHS
    if display_process:
        print("=" * process_line_length)
        print("  checking directory & files..")

    for key, path in MAIN_PATHS.items():
        if display_process:
            print(f"  check path {key} : {path}", end='')

        if (os.path.exists(path)):
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


# endregion

# endregion


# region

# checking requirements
print('=' * line_length)
check_directory_and_files(True)

print('=' * line_length)
# csv_data format : [site][category][date_make](comment).csv
print("  checking data..")
print("  checking modules..")

print("  최근에 저장한 파일 체크중..")
from modules import data_manager

print("최근에 저장한 파일이 없습니다.")

print(f"최근에 저장한 날짜 : ")
