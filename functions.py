import sqlite3 as sq3

#Вывод всех данных из таблицы School_Kind_Table
def print_school_kind_table():
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM School_Kind_Table")
        result = cursor.fetchall()
        return result

#Вывод всех данных из таблицы School_Type_Table
def print_school_type_table():
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM School_Type_Table")
        result = cursor.fetchall()
        return result

#Вывод всех данных из таблицы Area_Table
def print_area_table():
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Area_Table")
        result = cursor.fetchall()
        return result

#Вывод всех данных из таблицы Town_Type_Table
def print_town_type_table():
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Town_Type_Table")
        result = cursor.fetchall()
        return result

#Вывод всех данных из таблицы Subject_Table
def print_subject_table():
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Subject_Table")
        result = cursor.fetchall()
        return result
#print(print_subject_table())
#Вывод всех данных из таблицы School_Table
def print_school_table():
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM School_Table")
        result = cursor.fetchall()
        return result

#Вывод всех данных из таблицы School_Student_Table
def print_school_student_table():
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM School_Student_Table")
        result = cursor.fetchall()
        return result

#Вывод всех данных из таблицы Subject_Form_Table
def print_subject_sorm_table():
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Subject_Form_Table")
        result = cursor.fetchall()
        return result

#Вывод всех данных из таблицы Result_Table
def print_result_table():
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Result_Table")
        result = cursor.fetchall()
        return result

#Вывод всех данных из таблицы Task_Table
def print_task_table():
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Task_Table")
        result = cursor.fetchall()
        return result

#ответ на определенную задачу из результата экзамена опеределённого студента
def get_student_answer(student_id, task_id):
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT tt.task_id, tt.answer, rt.student_id, st.subject_name FROM Task_Table tt"
                       "LEFT JOIN Result_Table rt ON tt.result_id = rt.student_id AND tt.result_id = rt.subject_form_id "
                       "LEFT JOIN Subject_Form_Table sft ON rt.subject_form_id = sft.subject_form_id "
                       "LEFT JOIN Subject_Table st ON sft.subject_id = st.subject_id "
                       f"WHERE tt.task_id = {task_id} AND rt.student_id = '{student_id}';")
        result = cursor.fetchall()
        return result

#Средние результаты по предметам и годам
def get_average_subject_result(year):
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute(
            "SELECT st.subject_id, st.subject_name, AVG(rt.score_100) AS average_results FROM Subject_Form_Table sft "
            "LEFT JOIN Result_Table rt ON sft.subject_form_id = rt.subject_form_id "
            "INNER JOIN Subject_Table st ON sft.subject_id = st.subject_id "
            f"WHERE sft.year_of_exam = {year} "
            "GROUP BY sft.subject_form_id; ")
        result = cursor.fetchall()
        return result

#Средние баллы ЕГЭ по школам отсортированы по убыванию баллов 100 бальной шкалы (без базовой математики)
def get_average_school_result_100(year):
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute(
            "SELECT st.school_name , AVG(rt.score_100) AS average_results_100 FROM School_Table st "
            "LEFT JOIN School_Student_Table sst ON st.school_CODE = sst.school_code "
            "LEFT JOIN Result_Table rt ON sst.student_id  = rt.student_id "
            "LEFT JOIN Subject_Form_Table sft ON rt.subject_form_id = sft.subject_form_id "
            "LEFT JOIN Subject_Table st2 ON sft.subject_id = st2.subject_id "
            f"WHERE st2.subject_id != 22 AND sft.year_of_exam = {year} "
            "GROUP BY st.school_CODE "
            "ORDER BY average_results_100 DESC;")
        result = cursor.fetchall()
        return result

#Средние баллы ЕГЭ по школам отсортированы по убыванию баллов 5 бальной шкалы (без базовой математики)
def get_average_school_result_5(year):
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute(
            "SELECT st.school_CODE, st.school_name, AVG(rt.result_5) AS average_results_5 FROM School_Table st "
            "LEFT JOIN School_Student_Table sst ON st.school_CODE = sst.school_code "
            "LEFT JOIN Result_Table rt ON sst.student_id  = rt.student_id "
            "LEFT JOIN Subject_Form_Table sft ON rt.subject_form_id = sft.subject_form_id "
            "LEFT JOIN Subject_Table st2 ON sft.subject_id = st2.subject_id "
            f"WHERE st2.subject_id != 22 AND sft.year_of_exam = {year} "
            "GROUP BY st.school_CODE "
            "ORDER BY average_results_5 DESC;")
        result = cursor.fetchall()
        return result

#Средние баллы ЕГЭ по типам школ отсортированы по убыванию (без базовой математики)
def get_average_school_kind_result(year):
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT skt.school_kind_name, AVG(rt.score_100) AS average_score FROM School_Kind_Table skt "
                       "LEFT JOIN School_Table st ON skt.school_kind_id = st.school_kind_id "
                       "LEFT JOIN School_Student_Table sst ON st.school_CODE = sst.school_code "
                       "LEFT JOIN Result_Table rt ON sst.student_id = rt.student_id "
                       "LEFT JOIN Subject_Form_Table sft ON rt.subject_form_id = sft.subject_form_id "
                       "LEFT JOIN Subject_Table st2 ON sft.subject_id = st2.subject_id "
                       f"WHERE st2.subject_id != 22 AND sft.year_of_exam = {year} "
                       "GROUP BY skt.school_kind_id "
                       "ORDER BY average_score DESC ")
        result = cursor.fetchall()
        return result

#Средние баллы ЕГЭ по районам отсортированы по убыванию (без базовой математики)
def get_average_area_result(year):
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT at2.area_name, AVG(rt.score_100) AS average_score FROM Area_Table at2 "
                       "LEFT JOIN School_Table st ON at2.area_id  = st.area_id "
                       "LEFT JOIN School_Student_Table sst ON st.school_CODE = sst.school_code "
                       "LEFT JOIN Result_Table rt ON sst.student_id = rt.student_id "
                       "LEFT JOIN Subject_Form_Table sft ON rt.subject_form_id = sft.subject_form_id "
                       "LEFT JOIN Subject_Table st2 ON sft.subject_id = st2.subject_id "
                       f"WHERE st2.subject_id != 22 AND sft.year_of_exam = {year} "
                       "GROUP BY at2.area_id "
                       "ORDER BY average_score DESC ")
        result = cursor.fetchall()
        return result

#Средние баллы ЕГЭ по предметам и школам
def get_average_best_subject_school_result(year):
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute("WITH AvgScores AS ("
                       "    SELECT st.subject_id, st2.school_name, st.subject_name, AVG(rt.score_100) AS avg_score FROM Subject_Table st "
                       "    LEFT JOIN Subject_Form_Table sft ON st.subject_id = sft.subject_id "
                       "    LEFT JOIN Result_Table rt ON sft.subject_form_id = rt.subject_form_id "
                       "    LEFT JOIN School_Student_Table sst ON rt.student_id = sst.student_id "
                       "    LEFT JOIN School_Table st2 ON sst.school_code = st2.school_CODE "
                       f"    WHERE sft.year_of_exam = {year} "
                       "    GROUP BY st.subject_name, st2.school_CODE)"
                       "SELECT subject_id, school_name, subject_name, max_average_score "
                       "FROM ("
                       "    SELECT subject_id, school_name, subject_name, max(avg_score) AS max_average_score "
                       "    FROM AvgScores "
                       "    GROUP BY subject_name, subject_id "
                       ") AS max_scores "
                       "ORDER BY subject_id;")
        result = cursor.fetchall()
        return result

#Средние % выполнения
def get_average_subject_accuracy(year):
    with sq3.connect('test.db') as con:
        cursor = con.cursor()
        cursor.execute(
            "SELECT st.subject_id, st.subject_name, AVG(rt.accuracy) AS average_accuracy FROM Subject_Form_Table sft "
            "LEFT JOIN Result_Table rt ON sft.subject_form_id = rt.subject_form_id "
            "INNER JOIN Subject_Table st ON sft.subject_id = st.subject_id "
            f"WHERE sft.year_of_exam = {year} "
            "GROUP BY sft.subject_form_id; ")
        result = cursor.fetchall()
        return result

#print(get_average_subject_accuracy(2018))