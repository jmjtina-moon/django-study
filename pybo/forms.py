from django import forms
from pybo.models import Question


#ModelForm을 상속받은 QuestionForm 작성. ModelForm은 말그대로 모델과 연결된 폼이다.
#장고 모델폼은 반드시 내부 클래스로 Meta 클래스를 가져야 한다. Meta 클래스에는 모델폼이 사용할 모델과 모델의 필드들을 적어야 함.
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  #QuestionForm은 Question모델과 연결되어있다.
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'contect': '내용',
        }