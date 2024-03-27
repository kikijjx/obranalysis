import pandas as pd
import matplotlib.pyplot as plt
import functions
import io
import base64

#Средние баллы по предметам

df_2018 = pd.DataFrame(functions.get_average_subject_result(2018),columns=['Индекс','Предмет','Баллы'])
df_2019 = pd.DataFrame(functions.get_average_subject_result(2019),columns=['Индекс','Предмет','Баллы'])
df_2020 = pd.DataFrame(functions.get_average_subject_result(2020),columns=['Индекс','Предмет','Баллы'])
df_2021 = pd.DataFrame(functions.get_average_subject_result(2021),columns=['Индекс','Предмет','Баллы'])
df_2022 = pd.DataFrame(functions.get_average_subject_result(2022),columns=['Индекс','Предмет','Баллы'])

bar_width = 0.17

plt.bar(df_2018["Индекс"], df_2018["Баллы"], bar_width, color='yellow', label='2018')
plt.bar([i + bar_width for i in df_2019["Индекс"]], df_2019["Баллы"], bar_width, color='green', label='2019')
plt.bar([i + 2*bar_width for i in df_2020["Индекс"]], df_2020["Баллы"], bar_width, color='blue', label='2020')
plt.bar([i + 3*bar_width for i in df_2021["Индекс"]], df_2021["Баллы"], bar_width, color='red', label='2021')
plt.bar([i + 4*bar_width for i in df_2022["Индекс"]], df_2022["Баллы"], bar_width, color='orange', label='2022')

plt.xlabel('Предметы')
plt.ylabel('Баллы')
plt.title('Средний балл по предмету')
plt.xticks(df_2018["Индекс"], df_2018["Предмет"], rotation=45)
plt.xticks([i + bar_width for i in df_2019["Индекс"]], df_2019["Предмет"], rotation=45)
plt.xticks([i + 2*bar_width for i in df_2020["Индекс"]], df_2020["Предмет"], rotation=45)
plt.xticks([i + 3*bar_width for i in df_2021["Индекс"]], df_2021["Предмет"], rotation=45)
plt.xticks([i + 4*bar_width for i in df_2022["Индекс"]], df_2022["Предмет"], rotation=45)

for i, value in enumerate(df_2018["Баллы"]):
    plt.text(df_2018["Индекс"][i], value, str(round(value, 1)), ha='center', va='bottom')

for i, value in enumerate(df_2019["Баллы"]):
    plt.text(df_2019["Индекс"][i] + bar_width, value, str(round(value, 1)), ha='center', va='bottom')

for i, value in enumerate(df_2020["Баллы"]):
    plt.text(df_2020["Индекс"][i] + 2*bar_width, value, str(round(value, 1)), ha='center', va='bottom')

for i, value in enumerate(df_2021["Баллы"]):
    plt.text(df_2021["Индекс"][i] + 3*bar_width, value, str(round(value, 1)), ha='center', va='bottom')

for i, value in enumerate(df_2022["Баллы"]):
    plt.text(df_2022["Индекс"][i] + 4*bar_width, value, str(round(value, 1)), ha='center', va='bottom')

plt.legend()
plt.figure()

#Лучшие баллы в школах по баллам

df_2018 = pd.DataFrame(functions.get_average_best_subject_school_result(2018),columns=['Индекс','Школа','Предмет','Баллы'])
df_2019 = pd.DataFrame(functions.get_average_best_subject_school_result(2019),columns=['Индекс','Школа','Предмет','Баллы'])
df_2020 = pd.DataFrame(functions.get_average_best_subject_school_result(2020),columns=['Индекс','Школа','Предмет','Баллы'])
df_2021 = pd.DataFrame(functions.get_average_best_subject_school_result(2021),columns=['Индекс','Школа','Предмет','Баллы'])
df_2022 = pd.DataFrame(functions.get_average_best_subject_school_result(2022),columns=['Индекс','Школа','Предмет','Баллы'])

bar_width = 0.18

plt.bar(df_2018["Индекс"], df_2018["Баллы"], bar_width, color='yellow', label='2018')
plt.bar([i + bar_width for i in df_2019["Индекс"]], df_2019["Баллы"], bar_width, color='green', label='2019')
plt.bar([i + 2*bar_width for i in df_2020["Индекс"]], df_2020["Баллы"], bar_width, color='blue', label='2020')
plt.bar([i + 3*bar_width for i in df_2021["Индекс"]], df_2021["Баллы"], bar_width, color='red', label='2021')
plt.bar([i + 4*bar_width for i in df_2022["Индекс"]], df_2022["Баллы"], bar_width, color='orange', label='2022')

plt.ylabel('Баллы')
plt.title('Школы с лучшим средним баллом по предмету')
plt.xticks(df_2018["Индекс"], df_2018["Предмет"], rotation=45)
plt.xticks([i + bar_width for i in df_2019["Индекс"]], df_2019["Предмет"], rotation=45)
plt.xticks([i + 2*bar_width for i in df_2020["Индекс"]], df_2020["Предмет"], rotation=45)
plt.xticks([i + 3*bar_width for i in df_2021["Индекс"]], df_2021["Предмет"], rotation=45)
plt.xticks([i + 4*bar_width for i in df_2022["Индекс"]], df_2022["Предмет"], rotation=45)


for i, value in enumerate(df_2018["Баллы"]):
    plt.text(df_2018["Индекс"][i], value, str(round(value, 1)), ha='center', va='bottom')

for i, value in enumerate(df_2019["Баллы"]):
    plt.text(df_2019["Индекс"][i] + bar_width, value, str(round(value, 1)), ha='center', va='bottom')

for i, value in enumerate(df_2020["Баллы"]):
    plt.text(df_2020["Индекс"][i] + 2*bar_width, value, str(round(value, 1)), ha='center', va='bottom')

for i, value in enumerate(df_2021["Баллы"]):
    plt.text(df_2021["Индекс"][i] + 3*bar_width, value, str(round(value, 1)), ha='center', va='bottom')

for i, value in enumerate(df_2022["Баллы"]):
    plt.text(df_2022["Индекс"][i] + 4*bar_width, value, str(round(value, 1)), ha='center', va='bottom')


for i, school in enumerate(df_2018["Школа"]):
    plt.text(df_2018["Индекс"][i], i, school, ha='center', va='bottom', rotation=90)

for i, school in enumerate(df_2019["Школа"]):
    plt.text(df_2019["Индекс"][i] + bar_width, i, school, ha='center', va='bottom', rotation=90)

for i, school in enumerate(df_2020["Школа"]):
    plt.text(df_2020["Индекс"][i] + 2*bar_width, i, school, ha='center', va='bottom', rotation=90)

for i, school in enumerate(df_2021["Школа"]):
    plt.text(df_2021["Индекс"][i] + 3*bar_width, i, school, ha='center', va='bottom', rotation=90)

for i, school in enumerate(df_2022["Школа"]):
    plt.text(df_2022["Индекс"][i] + 4*bar_width, i, school, ha='center', va='bottom', rotation=90)


def show_subject_performance(subject_name):
    df_2018 = pd.DataFrame(functions.get_average_subject_accuracy(2018),
                           columns=['Индекс', 'Предмет', 'Процент выполнения'])
    df_2019 = pd.DataFrame(functions.get_average_subject_accuracy(2019),
                           columns=['Индекс', 'Предмет', 'Процент выполнения'])
    df_2020 = pd.DataFrame(functions.get_average_subject_accuracy(2020),
                           columns=['Индекс', 'Предмет', 'Процент выполнения'])
    df_2021 = pd.DataFrame(functions.get_average_subject_accuracy(2021),
                           columns=['Индекс', 'Предмет', 'Процент выполнения'])
    df_2022 = pd.DataFrame(functions.get_average_subject_accuracy(2022),
                           columns=['Индекс', 'Предмет', 'Процент выполнения'])

    percentages = [df_2018[df_2018['Предмет'].str.contains(subject_name)]['Процент выполнения'].values[0],
                   df_2019[df_2019['Предмет'].str.contains(subject_name)]['Процент выполнения'].values[0],
                   df_2020[df_2020['Предмет'].str.contains(subject_name)]['Процент выполнения'].values[0],
                   df_2021[df_2021['Предмет'].str.contains(subject_name)]['Процент выполнения'].values[0],
                   df_2022[df_2022['Предмет'].str.contains(subject_name)]['Процент выполнения'].values[0]]

    years = ['2018', '2019', '2020', '2021', '2022']
    fig, axs = plt.subplots(1, 5, figsize=(20, 5))
    for i in range(5):
        axs[i].pie([percentages[i], 100 - percentages[i]],
                   labels=[f'Выполнено:', 'Не выполнено'], autopct='%1.1f%%', startangle=0)
        axs[i].axis('equal')
        axs[i].set_title(f'{subject_name}: {years[i]}')

    plt.show()


# Запрос пользователю ввести название предмета
subject_name = input("Введите название предмета: ")

# Отображение 5 круговых диаграмм с процентом выполнения по предмету на каждый из годов
show_subject_performance(subject_name)



