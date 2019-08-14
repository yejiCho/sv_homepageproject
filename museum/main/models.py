from django.db import models

# 모델 클래스
# 상품 후보 등록
# django에서는 model이름은 대문자, 단수형
# Create your models here.
class Museum(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    area = models.CharField(max_length=15)
    free = models.CharField(max_length=10)

    def __str__(self):
        return self.name