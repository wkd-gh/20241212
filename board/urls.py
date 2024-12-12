from django.urls import path, include
from . import views
urlpatterns = [
    # 질문 목록
    path('', views.index,name='question'),  # http://127.0.0.1:8000/board/  
    
    # 질문 상세
    path('<int:id>', views.detail ,name='detail'),  # http://127.0.0.1:8000/board/question/

    # 답변 등록
    path('answer/create/<int:id>',views.answer_create, name='answer_create'),
    # 답변 삭제
    path('answer/delete/<int:id>',views.answer_delete, name='answer_delete'),
    # 답변 수정
    path('answer/modify/<int:id>',views.answer_modify, name='answer_modify'),

    # 질문 등록
    path('question/create/', views.question_create, name='question_create'),

    # 대량의 데이터 등록 - 테스트용
    path('test/makehavy/', views.make_havy_data,)
]