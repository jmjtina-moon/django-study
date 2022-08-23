from django.shortcuts import render
from django.http import HttpResponse  # 페이지 요청에 대한 응답을 할때 사용
from .models import Question
from django.shortcuts import render, get_object_or_404, redirect  # 모델 데이터를 템플릿(html) 파일을 사용하여 화면에 출력할 수 있는 render 함수!
from django.utils import timezone
from .forms import QuestionForm
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
    return render(request, "pybo/question_detail.html", context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # 아래에 get('content')는 input태그의 name 값입니다.
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # request에 question_detail.html에서 textarea에 입력된 데이터가 파이썬 객체에 담겨 넘어온다.
    # POST형식으로 전송된 form 데이터 항목 중 name==content인 값을 의미!
    return redirect('pybo:detail', question_id=question.id)


def question_create(request):
    if(request.method == 'POST'): #질문 등록 화면에서 입력값을 채우고 저장하기 버튼을 눌렀을때.
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)   # form으로 Question 모델 데이터를 저장하기 위한 코드. commit=False는 임시 저장을 의미한다. 즉 실제 데이터는 아직 저장되지 않은 상태이다. 임시저장을 하는 이유는 폼으로 질문 데이터를 저장할 경우 Question 모델의 create_date 값이 설정되지 않아 오류가 발생하기 때문.
            question.create_date = timezone.now()
            question.save()  # 임시저장이 아닌, 실제 저장.
            return redirect('pybo:index')

    else:  #GET방식. 질문 목록 화면에서 '질문 등록하기' 버튼을 누르면 이 else문이 호출된다.
         form = QuestionForm()
         context = {'form': form}
         return render(request, 'pybo/question_form.html', context)

    # form = QuestionForm()
    # context = {'form': form}
    # return render(request, 'pybo/question_form.html', context)
