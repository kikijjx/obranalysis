import pandas as pd
import sqlalchemy as sqla
import pathlib

pd.options.mode.copy_on_write = True


def main():
    folder = input('Введите полный путь к папке с результатами ЕГЭ: ')
    # C:\Users\roryt\PycharmProjects\obranalysis\results
    conn = get_db_connection(folder)
    flist = list(pathlib.Path(folder).glob('*.xlsx'))
    for f in flist:
        year = f.stem[0:4]
        curlistkeys = pd.ExcelFile(f).sheet_names
        base = pd.read_excel(f, sheet_name=curlistkeys[0])
        schools = pd.read_excel(f, sheet_name=curlistkeys[1])
        set_school_kind(schools, conn)
        print('Заполнил School_Kind_Table для %s' % f)
        set_school_type(schools, conn)
        print('Заполнил School_Type_Table для %s' % f)
        set_town_type(schools, conn)
        print('Заполнил Town_Type_Table для %s' % f)
        set_area(schools, conn)
        print('Заполнил Area_Table для %s' % f)
        set_school(schools, conn)
        print('Заполнил School_Table для %s' % f)
        set_subject(base, conn)
        print('Заполнил Subject_Table для %s' % f)
        set_student(base, conn)
        print('Заполнил School_Student_Table для %s' % f)
        set_subject_form(base, conn, year)
        print('Заполнил Subject_Form_Table для %s' % f)
        set_result(base, conn, year)
        print('Заполнил Result_Table для %s' % f)


def get_db_connection(folder):
    return sqla.create_engine('sqlite:///test.db')  # TODO: замените это на реальную дб


def set_school_kind(schools, conn):
    df = schools[['SchoolKindCode', 'SchoolKindName']].set_axis(['school_kind_id', 'school_kind_name'],
                                                                axis=1).drop_duplicates()

    for i in range(len(df)):
        try:
            df.iloc[i:i + 1].to_sql('School_Kind_Table', conn, if_exists='append', index=False,
                                    method=None)  # очень медленно, если много записей
        except sqla.exc.IntegrityError as e:
            pass


def set_school_type(schools, conn):
    df = schools[['SchoolTypeCode', 'SchoolTypeName']].set_axis(['school_type_id', 'school_type_name'],
                                                                axis=1).drop_duplicates()

    for i in range(len(df)):
        try:
            df.iloc[i:i + 1].to_sql('School_Type_Table', conn, if_exists='append', index=False, method=None)
        except sqla.exc.IntegrityError as e:
            pass


def set_town_type(schools, conn):
    df = schools[['TownTypeCode', 'TownTypeName']].set_axis(['town_type_id', 'town_type_name'],
                                                            axis=1).drop_duplicates()

    for i in range(len(df)):
        try:
            df.iloc[i:i + 1].to_sql('Town_Type_Table', conn, if_exists='append', index=False, method=None)
        except sqla.exc.IntegrityError as e:
            pass


def set_area(schools, conn):
    df = schools[['AreaCode', 'AreaName', 'TownshipName', 'GovernmentCode', 'GovernmentName']].set_axis(
        ['area_id', 'area_name', 'township_name', 'government_id', 'government_name'], axis=1).drop_duplicates(
        subset='area_id')

    for i in range(len(df)):
        try:
            df.iloc[i:i + 1].to_sql('Area_Table', conn, if_exists='append', index=False, method=None)
        except sqla.exc.IntegrityError as e:
            pass


def set_school(schools, conn):
    df = schools[
        ['SchoolID', 'SchoolCode', 'LawAddress', 'ShortName', 'SchoolKindCode', 'SchoolTypeCode', 'AreaCode',
         'GovernmentCode']].set_axis(
        ['school_id', 'school_code', 'law_address', 'school_name', 'school_kind_id', 'school_type_id', 'area_id',
         'town_type_id'], axis=1)

    for i in range(len(df)):
        try:
            df.iloc[i:i + 1].to_sql('School_Table', conn, if_exists='append', index=False, method=None)
        except sqla.exc.IntegrityError as e:
            pass


def set_subject(base, conn):
    df = base[['Предмет', 'Название предмета']].set_axis(['subject_id', 'subject_name'], axis=1).drop_duplicates()

    for i in range(len(df)):
        try:
            df.iloc[i:i + 1].to_sql('Subject_Table', conn, if_exists='append', index=False, method=None)
        except sqla.exc.IntegrityError as e:
            pass


def set_student(base, conn):
    df = base[['ID', 'Код школы']].set_axis(['student_id', 'school_code'], axis=1).drop_duplicates()

    for i in range(len(df)):
        try:
            df.iloc[i:i + 1].to_sql('School_Student_Table', conn, if_exists='append', index=False, method=None)
        except sqla.exc.IntegrityError as e:
            pass


def set_subject_form(base, conn, year):  # Я УБЬЮ СЕБЯ
    df = base[
        ['Предмет', 'Оценка кратких ответов', 'Оценка развернутых ответов', 'Оценка устных ответов']].drop_duplicates(
        subset=['Предмет'])

    df['A_tasks_count'] = df['Оценка кратких ответов'].str.len()
    df['B_tasks_count'] = df['Оценка развернутых ответов'].str.len().div(4).astype('Int64')
    df['C_tasks_count'] = df['Оценка устных ответов'].str.len().div(4).astype('Int64')
    df['year_of_exam'] = year
    df['subject_id'] = df['Предмет']
    df['subject_form_id'] = year + df.Предмет.map("{:02d}".format)

    res = df[['subject_form_id', 'subject_id', 'year_of_exam', 'A_tasks_count', 'B_tasks_count', 'C_tasks_count']]

    for i in range(len(df)):
        try:
            res.iloc[i:i + 1].to_sql('Subject_Form_Table', conn, if_exists='append', index=False, method=None)
        except sqla.exc.IntegrityError as e:
            pass


def set_result(base, conn, year):
    df = base[['ID', 'Предмет', 'Первичный балл', 'Процент выполнения', '100 балльная шкала']]
    df['student_id'] = df['ID']
    df['subject_form_id'] = year + df.Предмет.map("{:02d}".format)
    df['result_id'] = df['subject_form_id'] + '-' + df['ID']
    df['accuracy'] = df['Процент выполнения']
    df['primary_score'] = df['Первичный балл']
    df['score_100'] = df['100 балльная шкала']
    df['result_5'] = pd.Series()
    df['result_5'] = df['score_100']

    df.loc[(df.score_100 >= 85), 'result_5'] = 5
    df.loc[(df.score_100 < 85) & (df.score_100 >= 61), 'result_5'] = 4
    df.loc[(df.score_100 < 61) & (df.score_100 >= 41), 'result_5'] = 3
    df.loc[(df.score_100 < 41), 'result_5'] = 2
    df.loc[(df.Предмет == 22), 'result_5'] = df['score_100']

    res = df[['result_id', 'student_id', 'subject_form_id', 'primary_score', 'accuracy', 'score_100',
              'result_5']]

    res.to_sql('Result_Table', conn, if_exists='append', index=False, method=None)


main()
