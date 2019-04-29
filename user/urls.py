from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^user/$', UserView.as_view()),
    url(r'^login/$', LoginView.as_view()),
    url(r'^hospital/$', HospitalView.as_view()),
    url(r'^carer/$', CarerView.as_view()),
    url(r'^suggestion/$', SuggestionView.as_view()),
    url(r'^commit/$', EvaluationView.as_view()),
]
