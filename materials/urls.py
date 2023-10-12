from materials.apps import MaterialsConfig
from django.urls import path

from materials.views.materials import *
from materials.views.sections import *
from materials.views.tests import *

app_name = MaterialsConfig.name


urlpatterns = [
    path('section/create/', SectionCreateAPIView.as_view(), name='section_create'),
    path('section/list/', SectionListAPIView.as_view(), name='section_list'),
    path('section/retrieve/<int:pk>/', SectionRetrieveAPIView.as_view(), name='section_view'),
    path('section/update/<int:pk>/', SectionUpdateAPIView.as_view(), name='section_update'),
    path('section/delete/<int:pk>/', SectionDeleteAPIView.as_view(), name='section_delete'),

    path('materials/create/', MaterialsCreateAPIView.as_view(), name='materials_create'),
    # path('materials/<int:pk>/list/', MaterialsListAPIView.as_view(), name='materials_list'),
    path('materials/retrieve/<int:pk>/', MaterialsRetrieveAPIView.as_view(), name='materials_view'),
    path('materials/update/<int:pk>/', MaterialsUpdateAPIView.as_view(), name='materials_update'),
    path('materials/delete/<int:pk>/', MaterialsDeleteAPIView.as_view(), name='materials_delete'),

    path('tests/create/', TestsCreateAPIView.as_view(), name='tests_create'),
    path('materials/retrieve/<int:pk>/tests', TestsListAPIView.as_view(), name='tests_list'),
    path('tests/retrieve/<int:pk>/', TestsRetrieveAPIView.as_view(), name='tests_view'),
    path('tests/update/<int:pk>/', TestsCreateAPIView.as_view(), name='tests_update'),
    path('tests/delete/<int:pk>/', TestsCreateAPIView.as_view(), name='tests_delete'),
    ]