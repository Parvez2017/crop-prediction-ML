from django import forms

class CropRecommendationForm(forms.Form):
    temperature = forms.FloatField()
    humidity = forms.FloatField()
    ph = forms.FloatField()
    rainfall = forms.FloatField()