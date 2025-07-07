
from django.urls import path # type: ignore
from . import views  # ✅ Make sure this is not indented!

#localhost:8000/chai
#localhost:8000
urlpatterns = [
    path('', views.all_chai, name='all_chai'),

]
