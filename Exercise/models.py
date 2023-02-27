from django.db import models



class ExercisesAPI(models.Model):
    exerciseID=models.AutoField(primary_key=True)
    imageOfExercise=models.ImageField(editable=True,default="img/%y")
    title=models.CharField(editable=True,max_length=100)
    recSets=models.IntegerField(editable=True,default=4)
    targetMuscle=models.CharField(editable=True,max_length=100)
    desc=models.TextField(editable=True)
    directions=models.TextField(editable=True)

    def __str__(self) -> str:
        return self.title