from django import forms

ExRCharts = [
    ('USDKRW','원-달러'),
    ('JPYKRW','원-엔'),
    ('EURKRW','원-유로'),
    ('CNYKRW','원-위안'),
]
ExRCharts = [
    ('KOSPI','코스피'),
    ('KOSDAQ','코스닥'),
]

class ExRDateForm(forms.Form):
    chart = forms.CharField(widget=forms.Select(choices=ExRCharts))
    start = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))


class MktDateForm(forms.Form):
    chart = forms.CharField(widget=forms.Select(choices=ExRCharts))
    start = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
