from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'


class Materials(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='раздел', related_name='materials')
    image = models.ImageField(upload_to='materials/', verbose_name='изображение', null=True, blank=True)
    content = models.TextField(verbose_name='содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'


class Tests(models.Model):
    materials = models.ForeignKey(Materials, on_delete=models.CASCADE, verbose_name='материалы', related_name='tests')
    question = models.TextField(verbose_name='вопрос')
    correct_answer = models.CharField(max_length=150, verbose_name='правильный ответ')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'



