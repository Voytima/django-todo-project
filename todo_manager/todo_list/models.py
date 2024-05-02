from django.db import models


class ToDoItem(models.Model):
    title = models.CharField(max_length=250)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('done',)
        verbose_name = 'ToDo Item'
        verbose_name_plural = 'ToDo Items'

    def __str__(self) -> str:
        return f'{self.title}'
