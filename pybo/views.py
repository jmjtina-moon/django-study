from django.shortcuts import render
from django.http import HttpResponse  # 페이지 요청에 대한 응답을 할때 사용
from .models import Question
from django.shortcuts import render, get_object_or_404, redirect  # 모델 데이터를 템플릿(html) 파일을 사용하여 화면에 출력할 수 있는 render 함수!
from django.utils import timezone


# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-create_date')  # 작성일시 역순으로 조회(create_date 앞에 -가 붙었으므로)
    context = {'question_list': question_list}  #context란? template에 정보를 넘겨준다.
    return render(request, 'pybo/question_list.html', context)
    # render 함수는 context에 있는 Question 모델 데이터 question_list를 html파일에 적용하여 HTML코드로 변환.


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, "pybo/question_detail.html", context) #context란!!


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # request에 question_detail.html에서 textarea에 입력된 데이터가 파이썬 객체에 담겨 넘어온다.
    # POST형식으로 전송된 form 데이터 항목 중 name==content인 값을 의미!
    return redirect('pybo:detail', question_id=question.id)
