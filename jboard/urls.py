from django.urls import path
from .views import HomeView,DailyView,MacroView
from . import views

app_name='jboard'

urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    #path('datainput/',views.datainput,name='datainput'),
    path('daily/',views.DailyView.as_view(),name='daily'),
    path('macro/',views.MacroView.as_view(),name='macro'),
    path('portfolio/',views.portfolio,name='portfolio'),

    path('portfolio/create_pf_stocks/',views.create_pf_stocks.as_view(),name='create_pf_stocks'),
    path('portfolio/create_pf_bonds/',views.create_pf_bonds.as_view(),name='create_pf_bonds'),
        
]