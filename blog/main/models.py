from django.db import models
from django.utils.timezone import now

# Create your models here.


class Course(models.Model):
    class Meta:
        db_table = 'tbl_course'
    title = models.CharField('Заголовок', max_length=80)
    description = models.CharField('Краткое описание', max_length=90)
    start_date = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)
    amount = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
