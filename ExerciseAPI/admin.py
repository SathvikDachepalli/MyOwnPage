from django.contrib import admin
from ExerciseAPI.models import ExercisesAPI

# Register your models here.

class AdminExercises(admin.ModelAdmin):
    list_display=['title','imageOfExercise',"recSets","targetMuscle","desc","directions"]

admin.site.register(ExercisesAPI,AdminExercises)