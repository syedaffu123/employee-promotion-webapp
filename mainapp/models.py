from operator import mod
from pyexpat import model
from telnetlib import SE
from django.db import models

from mainapp.views import predictions
SEX=(
    (0,'Female'),
    (1,'Male')
)
# Create your models here.
class Data(models.Model):
    employee_id=models.PositiveIntegerField(primary_key=True)
    Age=models.PositiveIntegerField(null=True)
    Gender=models.PositiveIntegerField(choices=SEX,null=True)
    Education=models.CharField(max_length=10,null=True)
    Department=models.CharField(max_length=10,null=True)
    Region=models.CharField(max_length=10,null=True)
    Recruitment_Channel=models.CharField(max_length=10,null=True)
    Previous_year_rating=models.PositiveIntegerField(null=True)
    No_of_Trainings=models.PositiveIntegerField(null=True)
    Training_score=models.PositiveIntegerField(null=True)
    Years_of_service=models.PositiveIntegerField(null=True)
    kpi=models.PositiveIntegerField(null=True)
    awards=models.PositiveIntegerField(null=True)
    predictions=models.CharField(max_length=100,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-date']

    def __str__(self):
        return self.name

