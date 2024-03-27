import pandas as pd
import matplotlib.pyplot as plt
import diagram_funcs
import io
import urllib, base64
from django.shortcuts import render
from django.http import HttpResponse
import matplotlib
import functions
matplotlib.use('Agg')


def main(request):
    graph_data = diagram_funcs.graph_show([2018, 2019], [0, 1, 2, 3])
    return render(request, 'main.html', {'graph_data': graph_data})

def load_template(request):
    template_name = request.GET.get('template')
    subjects_list = functions.print_subject_table()
    if template_name == 'template1':
        return render(request, 'template1.html', {'subjects_list': subjects_list})
    elif template_name == 'template2':
        return render(request, 'template2.html')
    else:
        return render(request, 'sorry.html')