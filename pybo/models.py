# 데이터베이스 관리!!!!!!!!!!!!!!

from django.db import models

# Create your models here.

#질문 모델
class Question(models.Model):
    subject = models.CharField(max_length=200) #질문의 제목
    content = models.TextField() #질문의 내용
    create_date = models.DateTimeField() #질문을 작성한 일시

    def __str__(self):
        return self.subject

#답변 모델
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #질문이 삭제되면 답변도 삭제
    content = models.TextField()
    create_date = models.DateTimeField()