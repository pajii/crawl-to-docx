import pandas as pd
import os


# csv_data format: [site] [category] [date_make] (comment) .csv
# there should be no whitespace in  parentheses
# csv format : [date] [user(str)] [number(str)] [site path]

class DataManager:
    supported_sites = ['site', 'dc-inside']

    def __init__(self, _dir_path_name: str):
        self.file_list = []

        for file_path_name in os.listdir(_dir_path_name):
            self.file_list.append()

    class CsvData:
        def __init__(self, _path: str):
            pass

    class JsonData:
        def __init__(self, _path: str):
            pass

'''    # check file has correct name
    def isCorrectDataFileName(self, _filename: str, print_message=False) -> bool:
        name_list = _filename.split()
        if len(name_list) < 3:
            return False
        elif not all(*[char in g_str for g_str in name_list[:3]] for char in '[]'):
            return False
        # site
        if name_list[0][1:-1] in DataManager.supported_sites:
            pass

    def print_supported_site(self) -> None:
        print(" " * 5 + "supported site" + " " * 5)
        for site_name in DataManager.supported_sites:
            print(" " + site_name)'''