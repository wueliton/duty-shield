import pandas as pd


class SystemsModel:
    def __init__(self, excel_file: pd.ExcelFile):
        self.excel_file = excel_file

    def get_data(self):
        excel_file = pd.ExcelFile(self.excel_file)
        data = pd.read_excel(excel_file, sheet_name="systems")
        data_dict = data.to_dict('records')
        return data_dict

    def get_excel_file(self):
        return self.excel_file
