from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30, null=False)
    titles = models.IntegerField(null=True, default=0)
    top_scorer = models.CharField(max_length=50, null=False)
    fifa_code = models.CharField(max_length=3, unique=True, null=False)
    first_cup = models.DateField(null=True)

    def __repr__(self) -> str:
        return f"<[{self.id}] {self.name} - {self.fifa_code}>"