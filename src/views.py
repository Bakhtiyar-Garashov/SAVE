import csv

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):  # this is our main page that will be available when you hit the sire
    return render(request, 'index.html')


def get_data(request):
    data = {}  # this dict is container that stores all the data uploaded as csv
    if request.method == "GET":  # if request is just GET, then redirect to the same page
        return render(request, "index.html")

    try:
        # getting all form input values from request POST object
        input_fc = request.POST['inputFC']
        input_year = request.POST['inputYear']
        input_ms = request.POST['inputMS']
        input_capex = request.POST['inputCAPEX']
        input_annual = True if request.POST.get('inputAnnual') else False  # if checkbox is not checked make the value false otherwise true
        input_ideal = True if request.POST.get('inputIdeal') else False
        input_incremental = True if request.POST.get('inputIncremental') else False
        csv_file = request.FILES["csv_file"]  # getting uploaded csv file from user
        file_data = csv_file.read().decode("utf-8")  # read file and prevent any encoding issue
        data['input_fc'] = input_fc
        data['input_year'] = input_year
        data['input_ms'] = input_ms
        data['input_capex'] = input_capex
        data['input_annual'] = input_annual
        data['input_ideal'] = input_ideal
        data['input_incremental'] = input_incremental
        data["data"] = file_data

        # as I don't have main processing code over csv and csv files will have different templates,
        # it is impossible to implement editing (or processing) uploaded csv(s) right now. You just need to read csv
        # based on uploaded format, process it with main code and return it as downloadable new csv with the
        # (replace your final output from processing code over input with my dictionary which is named data)
        # help of code below. In case of any problem, I am ready to help :)

        # here we are defining response headers to make csv response downloadable
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="scenario_output.csv"'

        # writer object takes a iterable (list, collection) and writes it to new row of csv
        writer = csv.writer(response)
        writer.writerow(data.keys())  # writing column names (first row of csv from dictionary keys)
        writer.writerow(data.values())  # writing rest of the data (dict values as row

        return response

    except Exception as e:
        # in case of any error (e.g. issues with reading csv), simply show error message to the user
        return HttpResponse(
            "Something went wrong. See the error message for more info. \nError message:{}".format(e))
