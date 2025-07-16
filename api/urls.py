from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register("employees", views.EmployeeViewset, basename="employees")

urlpatterns = [
    path("students/", views.studentsView),
    path("students/<int:pk>/", views.studentsDetailView),
    # path("employees/", views.Employees.as_view()),
    # path("employees/<int:pk>/", views.EmployeeDetail.as_view()),
    path("", include(router.urls)),
    path("blogs/", views.BlogsView.as_view()),
    path("comments/", views.CommentsView.as_view()),
    path("blogs/<int:pk>/", views.BlogDetailView.as_view()),
    path("comments/<int:pk>/", views.CommentDetailView.as_view()),
    # Token Authentication
    # path("login/", obtain_auth_token, name="login"),
    path("register/", views.registration_view, name="register"),
    # path("logout/", views.logout_view, name="logout"),
    # JWT Authentication
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
