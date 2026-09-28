from django.urls import path
from . import views
urlpatterns = [
  
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('project/',views.project,name='project'),
    path('skills/',views.skills,name='skills'),
    path('internships/',views.internships,name='internships'),
    path('footer/',views.footer,name='footer'),
    # path('Education/',views.Education,name='Education'),
    path('index/',views.index,name='index'),
    path('navbar/',views.navbar,name='navbar'),
]