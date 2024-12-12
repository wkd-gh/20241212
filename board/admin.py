from django.contrib import admin
from .models import Question
# Register your models here.

# 관리자화면에서 제목으로 검색
class QAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QAdmin)


