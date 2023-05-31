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
                
    # def update_row(self, target_sheet_name: str, expr, updated_line: dict):
    #     excel_file = pd.ExcelFile(self.file_name)
    #     sheets_dict = pd.read_excel(excel_file, sheet_name=None)
    #     df = sheets_dict[target_sheet_name]
    #     if isinstance(expr, int):
    #         line = df[df['cpf'] == expr].index[0]
    #     else:
    #         line = df.query(expr).index[0]
            
    #     for col, value in updated_line.items():
    #         df.at[line, col] = value
            
    #     with pd.ExcelWriter(excel_file) as writer:
    #         for sheet_name, sheet_df in sheets_dict.items():
    #             sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)
