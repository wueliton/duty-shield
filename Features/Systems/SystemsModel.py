import pandas as pd


class SystemsModel:
    def __init__(self, excel_file: pd.ExcelFile):
        self.excel_file = excel_file

    def get_data(self):
        data = pd.read_excel(self.excel_file, sheet_name="systems")
        return [data.columns.tolist(), data.values.tolist()]
