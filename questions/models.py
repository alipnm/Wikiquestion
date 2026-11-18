from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(verbose_name='تیتر', max_length=100)
    content = models.TextField(verbose_name='محتوا')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='نویسنده', related_name='author')
    image = models.ImageField(
        verbose_name='عکس', upload_to="media/%y/%m/%d", null=True, blank=True)
    # views =
    # tags =
    # likes =
    # saves =

    def __str__(self):
        return super().__str__()
