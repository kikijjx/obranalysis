import pandas as pd
import matplotlib.pyplot as plt
import functions
import io
import base64

#Средние баллы по предметам
def graph_show(years, params):
    data_frames = []
    bar_width = 0.17

    for year in years:
        data_frames.append(pd.DataFrame(functions.get_average_subject_result(year), columns=['Индекс', 'Предмет', 'Баллы']))

    plt.figure()

    for i, df in enumerate(data_frames):
        df_filtered = df[df['Индекс'].isin(params)]
        plt.bar([j + i * bar_width for j in df_filtered['Индекс']], df_filtered['Баллы'], bar_width, color=get_color(i), label=str(years[i]))
        for j, value in enumerate(df_filtered['Баллы']):
            plt.text(df_filtered['Индекс'][j] + i * bar_width, value, str(round(value, 1)), ha='center', va='bottom')

    plt.xlabel('Предметы')
    plt.ylabel('Баллы')
    plt.title('Средний балл по предмету')
    plt.xticks([j + len(data_frames) * bar_width / 2 for j in df_filtered['Индекс']], df_filtered['Предмет'], rotation=45)
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    graph_data = base64.b64encode(buf.getvalue()).decode()
    plt.close()
    return graph_data


def get_color(i):
    colors = ['yellow', 'green', 'blue', 'red', 'orange']
    return colors[i % len(colors)]