from django.db import models

GRADE_CHOICE = (
    ("Head Chef","Head Chef"),
    ("Chef","Chef"),
    ('Assistant Chef','Assistant Chef')
)

# Create your models here.
class Staff(models.Model):
    staff_name = models.CharField(max_length=128, verbose_name="파티시엘 이름")
    staff_decs = models.TextField(verbose_name="상세 정보")
    staff_grade = models.CharField(max_length=50, choices=GRADE_CHOICE,verbose_name="직급",default='Chef')

    def __str__(self):
        return self.staff_name

    class Meta:
        db_table = "bakery_site_staff" # db이름

        verbose_name = '직원'
        verbose_name_plural = "직원"
        # verbose: 부팅시 상세한 정보를 보여줌

       

