from django.db import models


class Department(models.Model):
    class Meta:
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.code}'

