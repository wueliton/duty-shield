from typing import Union, Callable
import pandas as pd
from pandas import DataFrame


class SoDService:
    file_name = "db/sod_database.xlsx"
    excel_file = pd.ExcelFile("db/sod_database.xlsx")

    def _get_data(self, sheet_name: Union[str, int, None]):
        return pd.read_excel(self.excel_file, sheet_name=sheet_name)

    def get_sheet_data(self, sheet_name: Union[str, int]):
        excel_file = pd.ExcelFile(self.file_name)
        data = pd.read_excel(excel_file, sheet_name=sheet_name)
        return data.to_dict('records')
        
    def get_column_data(self, sheet_name, column1, column2, column3, column4):
        excel_file = pd.ExcelFile(self.file_name)
        data = pd.read_excel(excel_file, sheet_name=sheet_name)
        if column1 in data.columns and column2 in data.columns and column3 in data.columns and column4 in data.columns:
            column_data = data[[column1, column2, column3, column4]].values.tolist()
            return column_data
        else:
            return None
        
    def get_value_data(self, sheet_name, column1, column2, value1, value2):
        excel_file = pd.ExcelFile(self.file_name)
        data = pd.read_excel(excel_file, sheet_name=sheet_name)
        if column1 in data.columns and column2 in data.columns:
            column_data = data[[column1, column2]].values.tolist()
            for item in column_data:
                item.insert(0, value1)
                item.insert(1, value2)
            return column_data
        else:
            return None

    def get_sheet_count(self, sheet_name: Union[str, int]):
        excel_file = pd.ExcelFile(self.file_name)
        data = pd.read_excel(excel_file, sheet_name=sheet_name)
        return data.dropna().shape[0]

    def query(self, sheet_name: str, expr: str):
        excel_file = pd.ExcelFile(self.file_name)
        excel = pd.read_excel(excel_file, sheet_name=None)
        df = excel[sheet_name]
        query = df.query(expr)
        return query.to_dict('records')

    def find(self, sheet_name: Union[str, int], expr: str):
        excel_file = pd.ExcelFile(self.file_name)
        excel = pd.read_excel(excel_file, sheet_name=None)
        df = excel[sheet_name]
        result = df.query(expr)
        return result.to_dict('records')
    
    def find_keys(self, sheet_name: Union[str, int], expr: str, key1: str, key2: str, value1: str, value2: str):
        excel_file = pd.ExcelFile(self.file_name)
        excel = pd.read_excel(excel_file, sheet_name=None)
        df = excel[sheet_name]
        result = df.query(expr)
        records = result.to_dict('records')
        data_list = [[record[key1], record[key2]] for record in records]
        for item in data_list:
                item.insert(0, value1)
                item.insert(1, value2)
        return data_list

        

    def add_row(self, target_sheet_name: str, new_line: DataFrame):
        if new_line is None:
            return

        excel_file = pd.ExcelFile(self.file_name)
        sheets_dict = pd.read_excel(excel_file, sheet_name=None)
        df = sheets_dict[target_sheet_name]
        df = pd.concat([df, new_line])
        with pd.ExcelWriter(self.excel_file) as writer:
            for sheet_name, sheet_df in sheets_dict.items():
                if sheet_name == target_sheet_name:
                    sheet_df = df
                sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)

    def update_row(self, target_sheet_name: str, expr: str, updated_line: dict):
        excel_file = pd.ExcelFile(self.file_name)
        sheets_dict = pd.read_excel(excel_file, sheet_name=None)
        df = sheets_dict[target_sheet_name]
        line = df.query(expr).index[0]
        for col, value in updated_line.items():
            df.at[line, col] = value
        with pd.ExcelWriter(excel_file) as writer:
            for sheet_name, sheet_df in sheets_dict.items():
                sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)
