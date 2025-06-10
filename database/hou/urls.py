from django.urls import path
from .views import receive_user_location, get_player_info, register_user, check_user, update_player_location, submit_task_answer, get_task_locations, get_nearby_task, get_tasks, activate_nearby_task,start_task,activate_task_by_answer

urlpatterns = [
    path('api/user_location/', receive_user_location, name='user_location'),
    path('api/player_info/', get_player_info, name='player_info'),
    path('api/register/', register_user, name='register_user'),
    path('api/check_user/', check_user, name='check_user'),
    path('api/update_location/', update_player_location, name='update_location'),
    path('api/submit_task_answer/', submit_task_answer, name='submit_task_answer'),
    path('api/task_locations/', get_task_locations, name='task_locations'),
    path('api/get_nearby_task/', get_nearby_task, name='get_nearby_task'),
    path('api/tasks/', get_tasks, name='get_tasks'),
    path('api/activate_nearby_task/', activate_nearby_task, name='activate_nearby_task'),
    path('api/start_task/', start_task, name='start_task'),
    path('api/activate_task_by_answer/', activate_task_by_answer, name='activate_task_by_answer'),
]