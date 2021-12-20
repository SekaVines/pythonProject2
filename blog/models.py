from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE,
                             related_name='post_comment')
    text = models.TextField()
    created_data = models.DateField(auto_now_add=True)
