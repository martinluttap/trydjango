from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/vote_answer', views.vote_answer, name='vote_answer'),
    path('<int:question_id>/unvote_answer', views.unvote_answer, name='unvote_answer'),
    path('<int:question_id>/delete_answer', views.delete_answer, name='delete_answer'),
    path('<int:question_id>/add_answer', views.add_answer, name='add_answer'),
]