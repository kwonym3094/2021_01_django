from django.db import models

# Create your models here.
class Question(models.Model):
    """
    Create Question Table
    """

    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    """
    Create Answer Table related to Question Table
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content