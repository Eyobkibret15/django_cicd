from rest_framework import routers
from .views import students

rout = routers.DefaultRouter()
rout.register("student", viewset=students, basename="student")
