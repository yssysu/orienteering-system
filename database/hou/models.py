from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=50)  # 任务名称
    latitude = models.FloatField()  # 任务所在纬度
    longitude = models.FloatField()  # 任务所在经度
    description = models.TextField()  # 任务描述
    answer = models.CharField(max_length=500)  # 任务答案


class Player(models.Model):
    student_id = models.CharField(max_length=40)  # 学生编号
    task1_active = models.BooleanField(default=False)  # 任务 1 是否激活
    task1_completed = models.BooleanField(default=False)  # 任务 1 是否完成
    task2_active = models.BooleanField(default=False)  # 任务 2 是否激活
    task2_completed = models.BooleanField(default=False)  # 任务 2 是否完成
    task3_active = models.BooleanField(default=False)  # 任务 3 是否激活
    task3_completed = models.BooleanField(default=False)  # 任务 3 是否完成
    task4_active = models.BooleanField(default=False)  # 任务 4 是否激活
    task4_completed = models.BooleanField(default=False)  # 任务 4 是否完成
    latitude = models.FloatField(null=True, blank=True)  # 玩家所在纬度
    longitude = models.FloatField(null=True, blank=True)  # 玩家所在经度
