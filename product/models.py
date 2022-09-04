from django.db import models

# Create your models here.

BREAD_TYPE_CHOICE = (
    ('Baguette','Baguette'),
    ('Bagel','Bagel'),
    ('Muffin','Muffin'),
    ('Croissant','Croissant')
)
class Product(models.Model):
    bread_type = models.CharField(max_length=50, verbose_name='빵 종류', 
                choices=BREAD_TYPE_CHOICE)
    bread_feature = models.CharField(max_length=50, verbose_name='특징')
    bread_desc = models.TextField(verbose_name='설명')
    stock = models.IntegerField(verbose_name="재고",default=30)
    image = models.ImageField(verbose_name="이미지",upload_to='images/product',
    blank=True, null=True)

    def __str__(self):
        return self.bread_type+'_'+self.bread_feature

    class Meta:
        db_table = "bakery_site_product" # db이름
        verbose_name = '제품'
        verbose_name_plural = "제품"