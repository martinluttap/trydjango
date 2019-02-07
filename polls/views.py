from django.shortcuts import render, redirect

from .models import Question, Answer

def index(request):
    latest_question_list = Question.objects.all()
    context = {
        'latest_question_list' : latest_question_list,
    }
    
    return render(request, 'polls/index.html', context)

def add_answer(request, question_id):
    q = Question.objects.get(pk=question_id)    
    ans = Answer(question = q, answer_text = request.POST['input-answer'], votes = 0)
    print('request', request, q, ans)
    ans.save()

    return redirect('/polls/')

def delete_answer(request, question_id):
    ans = Question.objects.get(pk=question_id).answer
    ans.delete()    
        
    return redirect('/polls/')

def vote_answer(request, question_id):    
    ans = Question.objects.get(pk=question_id).answer
    ans.votes += 1

    ans.save()

    return redirect('/polls/')

def unvote_answer(request, question_id):    
    ans = Question.objects.get(pk=question_id).answer
    ans.votes -= 1

    ans.save()

    return redirect('/polls/')
