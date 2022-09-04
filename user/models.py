from tabnanny import verbose
from django.db import models

# Create your models here.

GENDER_CHOICE = (
    ('M','남자'),
    ('F','여자'),
    ('etc','그 이외')
)

class User(models.Model):
    username = models.CharField(max_length=128, verbose_name="사용자이름")
    email = models.EmailField(verbose_name="이메일",name="email",unique=True)
    password = models.CharField(max_length=256, verbose_name="비밀번호")
    gender = models.CharField(max_length=10, verbose_name="성별", name="gender",choices=GENDER_CHOICE)
    contact_number = models.CharField(max_length=50, verbose_name="연락처")
    address = models.CharField(max_length=256,verbose_name="주소")

    def __str__(self):
        return self.email

    class Meta:
        db_table = "bakery_site_user" # db이름
        verbose_name = '사용자'
        verbose_name_plural = "사용자"