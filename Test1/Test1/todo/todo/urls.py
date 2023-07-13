from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Lists/view/', views.ListsView.as_view()),
    path('api/Lists/post/', views.ListsPost.as_view()),
    path('api/Lists/<int:pk>', views.ListsDetail.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]