import pandas as pd
import sqlalchemy as sqla
import pathlib

def main():
    folder = input('Введите полный путь к папке с результатами ЕГЭ: ')
    # C:\Users\roryt\PycharmProjects\obranalysis\results
    # get_excel_files(folder)
    conn = get_db_connection(folder)

def get_excel_files(folder):
    flist = list(pathlib.Path(folder).glob('*.xlsx'))
    for f in flist:
        curlistkeys = pd.ExcelFile(f).sheet_names
        base = pd.read_excel(f, sheet_name=curlistkeys[0])
        schools = pd.read_excel(f, sheet_name=curlistkeys[1])

def get_db_connection(folder):
    return sqla.create_engine('sqlite:///test.db') # TODO: замените это на реальную дб

def set_school_kind(schools, conn):
    df = schools[['SchoolKindCode', 'SchoolKindName']]
    df.to_sql('School_Kind_Table', conn, if_exists='replace')



main()