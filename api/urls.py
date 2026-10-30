from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeViewset, basename='employees')

urlpatterns = [
    path('students/',views.StudentsView),
    path('student/<int:pk>/', views.StudentDetailView),
    # path('employees/', views.Employees.as_view()),
    #  path('employee/<int:pk>/', views.EmployeeDetail.as_view()),

    path('', include(router.urls)),

    path('blogs/',views.BlogView.as_view()),
    path('comment/',views.CommentView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailview.as_view()),
    path('comment/<int:pk>/', views.CommentDetailview.as_view()),
    ]


