from django.urls import path, include
from .views import *

app_name = "mainpage"
urlpatterns = [
    path('', intropage, name="intropage"),
    path('loadingpage/', loadingpage, name="loadingpage"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('mainpage/', mainpage, name="mainpage"),
    path('qnapage/', include('qnapage.urls', namespace='qnapage')),
    path('<int:id>/', detail, name="detail"),
    path('likes/<int:ticket_id>', likes, name="likes"),
    path('delete/<int:id>', delete, name="delete"),
    path('delete_comment/<int:id>', delete_comment, name="delete_comment"),
    path('update_comment/<int:id>', update_comment, name="update_comment"),
    path('ticketlistnew/', ticketlistnew, name="ticketlistnew"),
]