import datetime
import pandas as pd


class HomeModel:
    _morning = datetime.time(6, 0, 0)
    _afternoon = datetime.time(12, 0, 0)
    _night = datetime.time(18, 0, 0)
    _systems_count = 0
    _users_count = 0

    def __init__(self, excel_file: pd.ExcelFile):
        self.message = ""
        self.excel_file = excel_file

    def update_message(self):
        now = datetime.datetime.now().time()

        if self._morning <= now < self._afternoon:
            self.message = "Bom dia"
        elif self._afternoon <= now < self._night:
            self.message = "Boa tarde"
        else:
            self.message = "Boa noite"

    def get_data_count(self, sheet_name: str = None):
        if sheet_name is not None:
            data = pd.read_excel(self.excel_file, sheet_name=sheet_name)
            return len(data.index)
