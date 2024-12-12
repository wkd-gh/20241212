from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from .models import Question, Answer
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# def index(request):
#     return HttpResponse("나의 첫번째 장고")
def index(request):
    page = request.GET.get('page', '5')
    lists = Question.objects.order_by('-created_at')
    paginator = Paginator(lists,10)
    page_obj = paginator.get_page(page)

    # context = { 'lists' : lists}
    context = { 'lists' : page_obj}
    return render(request, 'board/question_lists.html', context )




def detail(request,id):
    # detail = Question.objects.get(id=id)
    question = get_object_or_404(Question,pk=id)
    context = { 'question' : question}
    return render(request, 'board/question_detail.html', context )

def answer_create(request,id):
    question = get_object_or_404(Question,pk=id)
    answer = Answer(question = question,content = request.POST.get('content'),created_at=timezone.now())
    answer.save()
    # return HttpResponse('등록성공')
    return redirect("detail",id=id)
def answer_delete(request, id):
    answer = get_object_or_404(Answer,pk=id)
    answer.delete()
    return redirect('detail', id=answer.question.id)

@csrf_exempt
def answer_modify(request, id):
    try:
        content =  request.POST.get('content')
        answer = get_object_or_404(Answer,pk=id)
        answer.content = content
        answer.save()
        return JsonResponse({"success":True})
    except:
        return JsonResponse({"success":False, "error":"error"})


def question_create(request):
    question = Question(subject = request.POST.get('subject'), content = request.POST.get('content'),created_at=timezone.now())
    question.save()
    return redirect("/board")




# 대량의 데이터 생성하기 - 테스트용
def make_havy_data(request):
    for i in range(100):
        question = Question(subject = f'제목 {i}', content = f'내용 {i}',created_at=timezone.now())
        question.save()
    return   HttpResponse("대량데이터 등록 성공")