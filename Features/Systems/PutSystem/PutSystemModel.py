import pandas as pd


class PutSystemModel:
    sheet_name = "systems"

    def __init__(self, excel_file: pd.ExcelFile):
        self.excel_file = excel_file

    def get_system_by_cod(self, cod: str):
        excel_file = pd.ExcelFile(self.excel_file)
        df = pd.read_excel(excel_file, sheet_name=self.sheet_name)
        return df.loc[(df["cod"] == cod)].to_dict("records")

    def save(self, cod: str, name: str):
        excel_file = pd.ExcelFile(self.excel_file)
        sheets_dict = pd.read_excel(excel_file, sheet_name=None)
        df = sheets_dict[self.sheet_name]
        new_data = pd.DataFrame({'cod': [cod], 'name': [name]})
        df = pd.concat([df, new_data])
        with pd.ExcelWriter(self.excel_file) as writer:
            for sheet_name, sheet_df in sheets_dict.items():
                if sheet_name == self.sheet_name:
                    sheet_df = df
                sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)

    def update(self, old_cod: str, cod: str, name: str):
        excel_file = pd.ExcelFile(self.excel_file)
        sheets_dict = pd.read_excel(excel_file, sheet_name=None)
        df = sheets_dict[self.sheet_name]
        line = df[df['cod'] == old_cod].index[0].item()
        df.at[line, 'cod'] = cod
        df.at[line, 'name'] = name
        with pd.ExcelWriter(self.excel_file) as writer:
            for sheet_name, sheet_df in sheets_dict.items():
                sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)
