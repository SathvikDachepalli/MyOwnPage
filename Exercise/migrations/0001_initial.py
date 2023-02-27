# Generated by Django 4.1.6 on 2023-02-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExercisesAPI',
            fields=[
                ('exerciseID', models.AutoField(primary_key=True, serialize=False)),
                ('imageOfExercise', models.ImageField(default='img/%y', upload_to='')),
                ('title', models.CharField(default='', max_length=100)),
                ('recSets', models.IntegerField(default=4)),
                ('targetMuscle', models.CharField(default='', max_length=100)),
                ('desc', models.CharField(default='', max_length=100)),
                ('directions', models.CharField(default='', max_length=100)),
            ],
        ),
    ]