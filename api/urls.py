from django.urls import path
from . import views

urlpatterns = [


    path('todos/', views.TodoList.as_view()),
    path('todos', views.TodoListCreate.as_view(http_method_names=['post'])),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDetroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view(http_method_names=['put'])),
    path('signup/', views.signup),
    path('login/', views.login),

]