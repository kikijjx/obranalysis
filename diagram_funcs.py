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
def average_subject_result_show(years, params, schools):
    data_frames = []
    for year in years:
        data_frames.append(pd.DataFrame(functions.get_average_subject_result(year, schools), columns=['Индекс', 'Предмет', 'Баллы']))

    fig = go.Figure()

    for i, df in enumerate(data_frames):
        df_filtered = df[df['Индекс'].isin(params)]
        df_filtered = df_filtered.reset_index(drop=True)

        fig.add_trace(go.Bar(x=df_filtered['Предмет'], y=df_filtered['Баллы'], text=df_filtered['Баллы'].apply(lambda x: str(round(x, 1))), textposition='auto', name=str(years[i])))

    fig.update_layout(barmode='group', xaxis_title='Предметы', yaxis_title='Баллы', showlegend=True)

    graph_data = fig.to_html(full_html=False)

    return graph_data


#Лучшие баллы в школах по предметам
def graph_show_best_schools(years, params, schools):
    data_frames = []
    for year in years:
        data_frames.append(pd.DataFrame(functions.get_average_best_subject_school_result(year, schools), columns=['Индекс', 'Школа', 'Предмет', 'Баллы']))

    fig = go.Figure()

    for i, df in enumerate(data_frames):
        df_filtered = df[df['Индекс'].isin(params)]
        df_filtered = df_filtered.reset_index(drop=True)

        text = df_filtered['Школа'] + '<br>' + df_filtered['Баллы'].apply(lambda x: str(round(x, 1)))
        fig.add_trace(go.Bar(x=df_filtered['Предмет'], y=df_filtered['Баллы'], text=text, textposition='auto', name=str(years[i])))

    fig.update_layout(barmode='group', xaxis_title='Предметы', yaxis_title='Баллы', showlegend=True)

    graph_data = fig.to_html(full_html=False)

    return graph_data


def average_subject_accuracy_show(years, params, schools):
    data_frames = []
    for year in years:
        data_frames.append(pd.DataFrame(functions.get_average_subject_accuracy(year, schools), columns=['Индекс', 'Предмет', 'Процент']))

    fig = go.Figure()

    for i, df in enumerate(data_frames):
        df_filtered = df[df['Индекс'].isin(params)]
        df_filtered = df_filtered.reset_index(drop=True)

        text = df_filtered['Процент'].apply(lambda x: str(round(x, 1)) + '%')
        fig.add_trace(go.Bar(x=df_filtered['Предмет'], y=df_filtered['Процент'], text=text, textposition='auto', name=str(years[i])))

    fig.update_layout(barmode='group', xaxis_title='Предметы', yaxis_title='Процент выполнения', showlegend=True)

    graph_data = fig.to_html(full_html=False)

    return graph_data




def average_subject_task_type_accuracy_show(task_types, years, params):
    fig = go.Figure()
    for type in task_types:
        data_frames = []
        for year in years:
            data_frames.append(pd.DataFrame(functions.get_task_type_accuracy(type, year),
                                            columns=['Индекс', 'Предмет', 'Год', 'Тип', 'Процент']))
        year_count = 0
        for i, df in enumerate(data_frames):
            df_filtered = df[df['Индекс'].isin(params)]
            df_filtered = df_filtered.reset_index(drop=True)
            year = [2018, 2019, 2020, 2021, 2022]
            fig.add_trace(go.Bar(x=[df_filtered['Предмет'],df_filtered['Год']], y=df_filtered['Процент'],
                             text=df_filtered['Процент'].apply(lambda x: str(round(x, 1))), textposition='auto', name=f'{year[year_count]}:{type}'))
            year_count+=1
        fig.update_layout(barmode='stack', xaxis_title='Предметы', yaxis_title='Проценты', showlegend=True)
    graph_data = fig.to_html(full_html=False)
    return graph_data


def show_participant_count(years, params, schools):
    data_frames = []
    for year in years:
        data = functions.get_participant_count_by_subject_year(year, schools)
        data_frames.append(pd.DataFrame(data, columns=['Индекс', 'Предмет', 'Количество']))
    fig = go.Figure()
    for i, df in enumerate(data_frames):
        df_filtered = df[df['Индекс'].isin(params)]
        df_filtered = df_filtered.reset_index(drop=True)
        text = df_filtered['Количество'].apply(lambda x: str(x))
        fig.add_trace(go.Bar(x=df_filtered['Предмет'], y=df_filtered['Количество'], text=text, textposition='auto', name=str(years[i])))
    fig.update_layout(barmode='group', xaxis_title='Предметы', yaxis_title='Количество участников', showlegend=True)
    graph_data = fig.to_html(full_html=False)
    return graph_data

def average_district_result_show(subject_id, years, areas):
    data_frames = []
    for year in years:
        data_frames.append(pd.DataFrame(functions.get_average_district_result(subject_id, [year], areas), columns=['Район', 'Баллы']))
    fig = go.Figure()
    for i, df in enumerate(data_frames):
        fig.add_trace(go.Bar(x=df['Район'], y=df['Баллы'], text=df['Баллы'].apply(lambda x: str(round(x, 1))), textposition='auto', name=str(years[i])))
    fig.update_layout(barmode='group', xaxis_title='Районы', yaxis_title='Баллы', showlegend=True)
    graph_data = fig.to_html(full_html=False)
    return graph_data
