import pandas as pd
import os

# csv_data format: [site] [category] [date_make] (comment) .csv
# csv format : [date] [user(str)] [number(str)] [site path]

class DataManager:
    def __init__(self, _dir_path_name: str):
        self.file_list = []
        for file_path_name in os.listdir(_dir_path_name):
            self.file_list.append(())
    class CsvData:
        def __init__(self, _path: str):
            pass

    def isCorrectData(self, _path: str) -> bool:
        pass