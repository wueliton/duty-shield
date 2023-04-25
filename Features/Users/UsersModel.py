import pandas as pd


class UsersModel:
    def __init__(self, excel_file: pd.ExcelFile):
        self.excel_file = excel_file

    def get_data(self):
        data = pd.read_excel(self.excel_file, sheet_name="users")
        return [["CPF", "Código", "Perfil"], data.values.tolist()]