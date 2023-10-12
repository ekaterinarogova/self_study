from materials.apps import MaterialsConfig
from django.urls import path

from materials.views.materials import *
from materials.views.sections import *
from materials.views.tests import *

app_name = MaterialsConfig.name


urlpatterns = [
    path('section/create/', SectionCreateAPIView.as_view(), name='section_create'),
    path('section/list/', SectionListAPIView.as_view(), name='section_list'),
    path('section/<int:pk>/', SectionRetrieveAPIView.as_view(), name='section_view'),
    path('section/update/<int:pk>/', SectionUpdateAPIView.as_view(), name='section_update'),
    path('section/delete/<int:pk>/', SectionDeleteAPIView.as_view(), name='section_delete'),

    path('section/<int:pk>/materials/', MaterialsListAPIView.as_view(), name='materials_list'),
    path('materials/create/', MaterialsCreateAPIView.as_view(), name='materials_create'),
    path('materials/<int:pk>/', MaterialsRetrieveAPIView.as_view(), name='materials_view'),
    path('materials/update/<int:pk>/', MaterialsUpdateAPIView.as_view(), name='materials_update'),
    path('materials/delete/<int:pk>/', MaterialsDeleteAPIView.as_view(), name='materials_delete'),

    path('materials/retrieve/<int:pk>/tests_list', TestsListAPIView.as_view(), name='tests_list'),
    path('tests/create/', TestsCreateAPIView.as_view(), name='tests_create'),
    path('tests/<int:pk>/', TestsRetrieveAPIView.as_view(), name='tests_view'),
    path('tests/update/<int:pk>/', TestsCreateAPIView.as_view(), name='tests_update'),
    path('tests/delete/<int:pk>/', TestsCreateAPIView.as_view(), name='tests_delete'),
    path('tests/<int:pk>/answer', TestAnswerView.as_view(), name='tests_answer'),
    ]