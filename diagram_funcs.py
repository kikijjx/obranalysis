import pandas as pd
import matplotlib.pyplot as plt
import functions
import io
import base64
import plotly.graph_objs as go
import plotly.express as px

def get_color(i):
    colors = ['yellow', 'green', 'blue', 'red', 'orange']
    return colors[i % len(colors)]

#Средние баллы по предметам
def average_subject_result_show(years, params):
    data_frames = []
    for year in years:
        data_frames.append(pd.DataFrame(functions.get_average_subject_result(year), columns=['Индекс', 'Предмет', 'Баллы']))

    fig = go.Figure()

    for i, df in enumerate(data_frames):
        df_filtered = df[df['Индекс'].isin(params)]
        df_filtered = df_filtered.reset_index(drop=True)

        fig.add_trace(go.Bar(x=df_filtered['Предмет'], y=df_filtered['Баллы'], name=str(years[i])))

    fig.update_layout(barmode='group', xaxis_title='Предметы', yaxis_title='Баллы')

    graph_data = fig.to_html(full_html=False)

    return graph_data


#Лучшие баллы в школах по предметам
def graph_show_best_schools(years, params, schools):
    data_frames = []
    bar_width = 0.18
    school = []
    for year in years:
        data_frames.append(pd.DataFrame(functions.get_average_best_subject_school_result(year, schools), columns=['Индекс', 'Школа', 'Предмет', 'Баллы']))
        school = pd.DataFrame(functions.get_average_best_subject_school_result(year, schools))
    plt.figure()
    for i, df in enumerate(data_frames):
        df_filtered = df[df['Индекс'].isin(params)]
        df_filtered = df_filtered.reset_index(drop=True)

        plt.bar([j + i * bar_width for j in df_filtered['Индекс']], df_filtered['Баллы'], bar_width, color=get_color(i), label=str(years[i]))
        for j, value in enumerate(df_filtered['Баллы']):
            plt.text(df_filtered['Индекс'][j] + i * bar_width, value, str(round(value, 1)), ha='center', va='bottom')
        for j, school in enumerate(df_filtered['Школа']):
            plt.text(df_filtered['Индекс'][j] + i * bar_width, j, school, ha='center', va='bottom', rotation=90)
    plt.ylabel('Баллы')
    #plt.title('Школы с лучшим средним баллом по предмету')
    plt.xticks([j + len(data_frames) * bar_width / 2 for j in df_filtered['Индекс']], df_filtered['Предмет'], rotation=45)
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    graph_data = base64.b64encode(buf.getvalue()).decode()
    plt.close()
    return graph_data

def average_subject_accuracy_show(years, params):
    data_frames = []
    bar_width = 0.17
    for year in years:
        data_frames.append(pd.DataFrame(functions.get_average_subject_accuracy(year), columns=['Индекс', 'Предмет', 'Процент']))

    plt.figure()

    for i, df in enumerate(data_frames):
        df_filtered = df[df['Индекс'].isin(params)]
        df_filtered = df_filtered.reset_index(drop=True)

        plt.bar([j + i * bar_width for j in df_filtered['Процент']], df_filtered['Процент'], bar_width, color=get_color(i), label=str(years[i]))
        for j, value in enumerate(df_filtered['Процент']):
            plt.text(df_filtered['Индекс'][j] + i * bar_width, value, str(round(value, 1)), ha='center', va='bottom')

    plt.xlabel('Предметы')
    plt.ylabel('Процент выполнения')
    #plt.title('Средний балл по предмету')
    plt.xticks([j + len(data_frames) * bar_width / 2 for j in df_filtered['Индекс']], df_filtered['Процент'], rotation=45)
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    graph_data = base64.b64encode(buf.getvalue()).decode()
    plt.close()
    return graph_data


def average_subject_task_type_accuracy_show(task_types, years, params):
    data_frames = []
    bar_width = 0.17
    task = []
    for type in task_types:
        for year in years:
            data_frames.append(pd.DataFrame(functions.get_task_type_accuracy(task_type, year), columns=['Индекс','Предмет','Год','Тип','Процент']))

    plt.figure()

    for i, df in enumerate(data_frames):
        df_filtered = df[df['Индекс'].isin(params)]
        df_filtered = df_filtered.reset_index(drop=True)

        plt.bar([j + i * bar_width for j in df_filtered['Индекс']], df_filtered['Процент'], bar_width, color=get_color(i), label=str(years[i]))
        for j, value in enumerate(df_filtered['Процент']):
            plt.text(df_filtered['Процент'][j] + i * bar_width, value, str(round(value, 1)), ha='center', va='bottom')

    plt.xlabel('Предметы')
    plt.ylabel('Процент выполнения')
    plt.xticks([j + len(data_frames) * bar_width / 2 for j in df_filtered['Индекс']], df_filtered['Процент'], rotation=45)
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    graph_data = base64.b64encode(buf.getvalue()).decode()
    plt.close()
    return graph_data