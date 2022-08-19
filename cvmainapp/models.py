from django.db import models


# Create your models here.
class Contacts(models.Model):
    user_name = models.CharField("Имя", max_length=50)
    user_email = models.EmailField("Электронная почта", max_length=50)
    message = models.TextField("Сообщение", blank=True)
    sending_time = models.DateTimeField("Время отправки", auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
    
    def __str__(self):
        return self.user_name
        