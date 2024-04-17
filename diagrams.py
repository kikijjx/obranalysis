import pandas as pd
import matplotlib.pyplot as plt
import functions
import plotly.graph_objs as go
import plotly.express as px

# Средние баллы по предметам

def average_subject_result_show(years):
    data_frames = []
    for year in years:
        data_frames.append(pd.DataFrame(functions.get_average_subject_result_press_release(year), columns=['Индекс', 'Предмет', 'Баллы']))

    fig = go.Figure()

    for i, df in enumerate(data_frames):
        fig.add_trace(go.Bar(x=df['Предмет'], y=df['Баллы'], text=df['Баллы'].apply(lambda x: str(round(x, 1))), textposition='auto', name=str(years[i])))

    fig.update_layout(barmode='group', xaxis_title='Предметы', yaxis_title='Баллы', showlegend=True)

    return fig

def average_subject_task_type_accuracy_show(task_types, years):
    fig = go.Figure()
    for type in task_types:
        data_frames = []
        for year in years:
            data_frames.append(pd.DataFrame(functions.get_task_type_accuracy(type, year),
                                            columns=['Индекс', 'Предмет', 'Год', 'Тип', 'Процент']))
        year_count = 0
        for i, df in enumerate(data_frames):
            # df_filtered = df['Индекс']
            # df_filtered = df_filtered.reset_index(drop=True)

            year = [2018, 2019, 2020, 2021, 2022]
            fig.add_trace(go.Bar(x=[df['Предмет'],df['Год']], y=df['Процент'],
                             text=df['Процент'].apply(lambda x: str(round(x, 1))), textposition='auto', name=f'{year[year_count]}:{type}'))
            year_count+=1
        fig.update_layout(barmode='stack', xaxis_title='Предметы', yaxis_title='Проценты', showlegend=True)

    return fig

def show_participant_count(years):
    data_frames = []
    for year in years:
        data = functions.get_participant_count_by_subject_year_press_release(year)
        data_frames.append(pd.DataFrame(data, columns=['Индекс', 'Предмет', 'Количество']))
    fig = go.Figure()
    for i, df in enumerate(data_frames):
        text = df['Количество'].apply(lambda x: str(x))
        fig.add_trace(go.Bar(x=df['Предмет'], y=df['Количество'], text=text, textposition='auto', name=str(years[i])))
    fig.update_layout(barmode='group', xaxis_title='Предметы', yaxis_title='Количество участников', showlegend=True)
    return fig