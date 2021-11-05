from django.urls import path

from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'app001_projectManagement'
urlpatterns = [

    #path('', views.v010_TopPage, name='topPage'),
    #path('Signup/', views.v015_Signup, name='Signup'),
    #path('login/', views.v020_Signin, name='login'),
    #path('logout/', views.v025_Signout, name='logout'),
    path('projectList/', views.v030_ProjectList, name='projectList'),
    path('projectCreate/', views.v040_ProjectCreate, name='projectCreate'),
    path('project/<str:urlID>/top/', views.v050_ProjectTop, name='projectTop'),
    path('project/<str:urlID>/taskTable/', views.v060_TaskTable, name='taskTable'),
    path('project/<str:urlID>/taskCreate/', views.v070_TaskCreate, name='taskCreate'),
    path('project/<str:urlID>/taskDetail/<int:seq>/', views.v080_TaskDetail, name='taskDetail'),
    path('project/<str:urlID>/taskDetail/<int:seq>/update/', views.v090_TaskUpdate, name='taskUpdate'),
    path('project/<str:urlID>/taskDetail/<int:seq>/delete/', views.v100_TaskDelete, name='taskDelete'),
    path('success/', views.v910_SuccessView, name='success'),
    path('systemError/', views.v990_SystemError, name='systemError'),
    #-------------------------------------------------------------
    path('test01/', views.test01, name='test01'),


] + static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
