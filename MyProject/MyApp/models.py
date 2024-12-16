from django.db import models


class BBCodeEntry(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    bbcode_content = models.TextField(verbose_name="BBCode контент")
    html_content = models.TextField(verbose_name="HTML контент", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title
