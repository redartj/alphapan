from django import forms

ExRCharts = [
    ('원달러','USDKRW'),
    ('원엔','JPYKRW'),
    ('원유로','EURKRW'),
    ('원위안','CNYKRW'),
]
class ExRDateForm(forms.Form):
    chart = forms.CharField(widget=forms.Select(choices=ExRCharts))
    start = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
