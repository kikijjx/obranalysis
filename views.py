import pandas as pd
import matplotlib.pyplot as plt
import diagram_funcs
import io
import urllib, base64
from django.shortcuts import render
from django.http import HttpResponse
import matplotlib
matplotlib.use('Agg')


def main(request):
    graph_data = diagram_funcs.graph_show([2018, 2019], [0, 1, 2, 3])
    return render(request, 'main.html', {'graph_data': graph_data})
