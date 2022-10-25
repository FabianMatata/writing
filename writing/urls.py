from django.contrib import admin
from django.urls import include, path
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),

    # C (CREATE)
    path('', views.data_form, name='data_create'),
    # R (READ)
    path('data/', views.data_read, name='data_read'),
    # U (UPDATE)
    path('<int:id>', views.data_form, name='data_update'),
    # D (DELETE)
    path('data_delete/<str:candidate_id>', views.data_delete, name='data_delete'),
]
