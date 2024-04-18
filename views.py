import pandas as pd
import diagram_funcs
import press_release_gen
from django.shortcuts import render
from django.http import HttpResponse
import matplotlib
from django.http import JsonResponse
import functions
from string import Template

matplotlib.use('Agg')

def main(request):
    return render(request, 'main.html')


def load_template(request):
    template_name = request.GET.get('template')
    subjects_list = sorted(functions.print_subject_table(), key=lambda x: x[1])
    years_list = sorted(functions.get_actual_years(), key=lambda x: x)
    area_schools_dict = {}
    schools_list = sorted(functions.get_school_table(), key=lambda x: x[1])
    area_list = sorted(functions.print_area_table(), key=lambda x: x[1])
    for area in functions.print_area_table():
        area_schools_dict[area[0]] = [school[1] for school in functions.get_school_table() if school[6] == area[0]]
    if template_name == 'template1':
        return render(request, 'template1.html',
                      {'subjects_list': subjects_list, 'years_list': years_list, 'schoolcode_list': schools_list,
                       'area_list': area_list, 'area_schools_dict': area_schools_dict})
    elif template_name == 'template2':
        return render(request, 'template2.html',
                      {'subjects_list': subjects_list, 'years_list': years_list, 'schoolcode_list': schools_list,
                       'area_list': area_list, 'area_schools_dict': area_schools_dict})
    elif template_name == 'template3':
        return render(request, 'template3.html',
                      {'subjects_list': subjects_list, 'years_list': years_list, 'schoolcode_list': schools_list,
                       'area_list': area_list, 'area_schools_dict': area_schools_dict})
    elif template_name == 'template4':
        task_types_list = pd.DataFrame(functions.get_task_types())  # нужна другая процедура
        return render(request, 'template4.html',
                      {'subjects_list': subjects_list, 'years_list': years_list, 'task_types_list': task_types_list,
                        'schoolcode_list': schools_list, 'area_list': area_list, 'area_schools_dict': area_schools_dict})
    elif template_name == 'template5':
        return render(request, 'template5.html',
                      {'subjects_list': subjects_list, 'years_list': years_list, 'schoolcode_list': schools_list,
                       'area_list': area_list, 'area_schools_dict': area_schools_dict})
    elif template_name == 'template6':
        return render(request, 'template6.html',
                      {'subjects_list': subjects_list, 'years_list': years_list, 'schoolcode_list': schools_list,
                       'area_list': area_list, 'area_schools_dict': area_schools_dict})
    else:
        return render(request, 'sorry.html')

def generate_press_release(request):
    with open(press_release_gen.generator(2020), 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename={press_release_gen.generator(2020)}'
        return response
# def generate_press_release(request):
#     data1 = 2
#     data2 = 75
#     data3 = 5
#     with open('pressreleasetemplate.txt', 'r', encoding='utf-8') as file:
#         template = Template(file.read())
#     press_release = template.substitute(
#         data1=data1,
#         data2=data2,
#         data3=data3,
#     )
#     with open('pressrelease.txt', 'w', encoding='utf-8') as file:
#         file.write(press_release)
#     return HttpResponse(press_release, content_type='text/plain')

def update_graph1(request):
    selected_years = list(map(int, request.GET.getlist('years[]')))
    selected_subjects = list(map(int, request.GET.getlist('subjects[]')))
    selected_schools = request.GET.getlist('schools[]')
    selected_areas = request.GET.getlist('areas[]')
    graph_data = diagram_funcs.average_subject_result_show(selected_years, selected_subjects, selected_schools).to_html(full_html=False)
    return HttpResponse(graph_data)

def update_graph2(request):
    selected_years = list(map(int, request.GET.getlist('years[]')))
    selected_subjects = list(map(int, request.GET.getlist('subjects[]')))
    selected_schools = request.GET.getlist('schools[]')
    selected_areas = request.GET.getlist('areas[]')
    graph_data = diagram_funcs.graph_show_best_schools(selected_years, selected_subjects, selected_schools)
    return HttpResponse(graph_data)


def update_graph3(request):
    selected_years = list(map(int, request.GET.getlist('years[]')))
    selected_subjects = list(map(int, request.GET.getlist('subjects[]')))
    selected_schools = request.GET.getlist('schools[]')
    selected_areas = request.GET.getlist('areas[]')
    graph_data = diagram_funcs.average_subject_accuracy_show(selected_years, selected_subjects, selected_schools)
    return HttpResponse(graph_data)


def update_graph4(request):
    selected_years = list(map(int, request.GET.getlist('years[]')))
    selected_subjects = list(map(int, request.GET.getlist('subjects[]')))
    selected_task_types = list(map(request.GET.getlist('task_types[]')))
    graph_data = diagram_funcs.average_subject_task_type_accuracy_show(selected_task_types, selected_years,
                                                                       selected_subjects)
    return JsonResponse({'graph_data': graph_data})

def update_graph5(request):
    selected_years = list(map(int, request.GET.getlist('years[]')))
    selected_subjects = list(map(int, request.GET.getlist('subjects[]')))
    selected_schools = request.GET.getlist('schools[]')
    selected_areas = request.GET.getlist('areas[]')
    graph_data = diagram_funcs.show_participant_count(selected_years, selected_subjects, selected_schools).to_html(full_html=False)
    return HttpResponse(graph_data)

def update_graph6(request):
    selected_subject = int(request.GET.get('subject'))
    selected_years = list(map(int, request.GET.getlist('years[]')))
    selected_areas = request.GET.getlist('areas[]')
    graph_data = diagram_funcs.average_district_result_show(selected_subject, selected_years, selected_areas)
    return HttpResponse(graph_data)