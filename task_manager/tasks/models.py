from django.db import models
from django.utils import timezone
from task_manager.users.models import NewUser
from task_manager.statuses.models import TaskStatus
from django.utils.translation import gettext_lazy as tr


class Task(models.Model):
    name = models.CharField(verbose_name=tr('Имя'), max_length=120,  blank=False)
    description = models.TextField(verbose_name=tr('Описание'), max_length=1000, blank=True)
    status = models.ForeignKey(
        TaskStatus,
        related_name='statuses',
        on_delete=models.PROTECT,
        blank=False,
        verbose_name=tr('Статус')
    )
    author = models.ForeignKey(
        NewUser,
        related_name='authors',
        on_delete=models.PROTECT,
        blank=False,
        verbose_name=tr('Автор')
    )
    executor = models.ForeignKey(
        NewUser,
        related_name='executors',
        on_delete=models.PROTECT,
        blank=True,
        verbose_name=tr('Исполнитель')
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name