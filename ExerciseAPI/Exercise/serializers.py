from rest_framework import serializers
from  .models import *


class ExerciseAPISerializer(serializers.ModelSerializer):
    class Meta:
        model=ExercisesAPI
        fields=('title','imageOfExercise',"recSets","targetMuscle","desc","directions")