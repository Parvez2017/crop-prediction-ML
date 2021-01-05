import numpy as np 
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CropRecommendationForm
from .prediction import get_prediction


def index(request):
    form = CropRecommendationForm()
    data = {}
    if request.method == 'POST':
        form = CropRecommendationForm(request.POST)
        if form.is_valid():
            temperature = float(form.cleaned_data['temperature'])
            humidity = float(form.cleaned_data['humidity'])
            ph = float(form.cleaned_data['ph'])
            rainfall = float(form.cleaned_data['rainfall'])
            
            prd_list = np.array([[temperature, humidity, ph, rainfall]])
            print(prd_list)
            prediction = get_prediction(prd_list)
            print(prediction)
            data['prediction'] = prediction 

    return render(request, 'index.html', {'form': form, 'data': data})