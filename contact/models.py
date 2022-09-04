from django.db import models
from user.models import User
# Create your models here.

class Receipt(models.Model):
    user = models.ForeignKey("user.User",on_delete=models.CASCADE,
    verbose_name="사용자")
    email = models.EmailField(verbose_name="이메일",name="email")
    contact_number = models.CharField(max_length=50, verbose_name="연락처")
    message = models.TextField(verbose_name="메세지")
    registered_dttm = models.DateTimeField(verbose_name="등록일자", auto_now_add=True)
    
    def __str__(self):
        return self.email

    class Meta:
        db_table = "bakery_site_receipt" # db이름
        verbose_name = '접수 관리'
        verbose_name_plural = "접수 관리"


