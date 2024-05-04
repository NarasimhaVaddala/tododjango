from django.urls import path, include
from modelapp import views

urlpatterns = [
    path('', views.index , name="index"),
    path('post', views.index , name="post"),
    path('update<int:id>', views.update , name="update"),
    path('delete<int:id>', views.delete , name="delete")
    # path('update<int:id>/', views.update , name="update")
]
