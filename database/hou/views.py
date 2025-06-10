from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from.models import Player, Task
import logging
logger = logging.getLogger(__name__)
from django.db import DatabaseError
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def receive_user_location(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student_id = data.get('studentId')
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            logger.info(f"Received data: student_id={student_id}, latitude={latitude}, longitude={longitude}")
            try:
                player, created = Player.objects.get_or_create(student_id=student_id)
                player.latitude = latitude
                player.longitude = longitude
                player.save()
                tasks = Task.objects.all()
                for task in tasks:
                    # 简单的距离范围检查，可使用更精确的地理空间计算
                    if (latitude - 0.0004 <= task.latitude <= latitude + 0.0004) and (
                            longitude - 0.01 <= task.longitude <= longitude + 0.01):
                        if task.name == 1:
                            player.task1_active = True
                        elif task.name == 2:
                            player.task2_active = True
                        elif task.name == 3:
                            player.task3_active = True
                        elif task.name == 4:
                            player.task4_active = True
                player.save()
                return JsonResponse({'message': '用户位置接收成功'}, status=200)
            except DatabaseError as e:
                logger.error(f"Database error: {str(e)}")
                return JsonResponse({'error': '数据库操作错误', 'details': str(e)}, status=500)
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error: {str(e)}")
            return JsonResponse({'error': '请求体不是有效的JSON格式', 'details': str(e)}, status=400)
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def get_player_info(request):
    if request.method == 'GET':
        student_id = request.GET.get('studentId')
        try:
            player = Player.objects.get(student_id=student_id)
            player_info = {
                'student_id': player.student_id,
                'task1_active': player.task1_active,
                'task1_completed': player.task1_completed,
                'task2_active': player.task2_active,
                'task2_completed': player.task2_completed,
                'task3_active': player.task3_active,
                'task3_completed': player.task3_completed,
                'task4_active': player.task4_active,
                'task4_completed': player.task4_completed,
                'latitude': player.latitude,
                'longitude': player.longitude
            }
            return JsonResponse(player_info, status=200)
        except Player.DoesNotExist:
            return JsonResponse({'error': '未找到玩家'}, status=404)
@csrf_exempt
def check_user(request):
    if request.method == 'POST':
        logger.info("开始处理check_user请求")
        try:
            data = json.loads(request.body)
            student_id = data.get('studentId')
            logger.info("即将查询数据库")
            exists = Player.objects.filter(student_id = student_id).exists()
            logger.info("数据库查询完成")
            return JsonResponse({'exists': exists})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': '请求体不是有效的JSON格式', 'details': str(e)}, status = 400)
        except Exception as e:
            logger.error("出现错误: %s", str(e))
            return JsonResponse({'error': '内部错误', 'details': str(e)}, status = 500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status = 405)
@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student_id = data.get('studentId')
            if Player.objects.filter(student_id = student_id).exists():
                return JsonResponse({'message': '该学号已注册'}, status = 400)
            Player.objects.create(student_id = student_id)
            return JsonResponse({'message': '注册成功'}, status = 201)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': '请求体不是有效的JSON格式', 'details': str(e)}, status = 400)
        except DatabaseError as e:
            return JsonResponse({'error': '数据库操作错误', 'details': str(e)}, status = 500)
        except Exception as e:
            return JsonResponse({'error': '内部错误', 'details': str(e)}, status = 500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status = 405)\
@csrf_exempt
def update_player_location(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student_id = data.get('studentId')
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            player = Player.objects.get(student_id=student_id)
            player.latitude = latitude
            player.longitude = longitude
            player.save()
            tasks = Task.objects.all()
            for task in tasks:
                # 简单的距离范围检查，可使用更精确的地理空间计算
                if (latitude - 0.01 <= task.latitude <= latitude + 0.01) and (longitude - 0.01 <= task.longitude <= longitude + 0.01):
                    if task.name == 1:
                        player.task1_active = True
                    elif task.name == 2:
                        player.task2_active = True
                    elif task.name == 3:
                        player.task3_active = True
                    elif task.name == 4:
                        player.task4_active = True
            player.save()
            return JsonResponse({'message': '玩家位置更新成功'}, status=200)
        except Player.DoesNotExist:
            return JsonResponse({'error': '未找到玩家'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
@csrf_exempt
def submit_task_answer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student_id = data.get('studentId')
            task_id = data.get('taskId')
            if student_id is None:
                return JsonResponse({'error': '学生 ID 缺失'}, status=400)
            if task_id is None:
                return JsonResponse({'error': '任务 ID 缺失'}, status=400)
            try:
                player = Player.objects.get(student_id=student_id)
                if task_id == 1:
                    player.task1_completed = True
                elif task_id == 2:
                    player.task2_completed = True
                elif task_id == 3:
                    player.task3_completed = True
                elif task_id == 4:
                    player.task4_completed = True
                player.save()
                return JsonResponse({'message': '任务完成成功', 'task_completed': True}, status=200)
            except Player.DoesNotExist:
                return JsonResponse({'error': '未找到玩家'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({'error': '请求体格式错误，请使用 JSON 格式'}, status=400)
    else:
        return JsonResponse({'error': '无效的请求方法，仅支持 POST 请求'}, status=405)
def get_task_locations(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        task_locations = []
        for task in tasks:
            task_locations.append({
                'latitude': task.latitude,
                'longitude': task.longitude,
                'description': task.description
            })
        return JsonResponse(task_locations, safe=False)
@csrf_exempt
def get_nearby_task(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student_id = data.get('studentId')
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            tasks = Task.objects.all()
            nearby_task = None
            for task in tasks:
                if (latitude - 0.0004 <= task.latitude <= latitude + 0.0004) and (
                        longitude - 0.01 <= task.longitude <= longitude + 0.01):
                    # 获取玩家信息
                    try:
                        player = Player.objects.get(student_id=student_id)
                        # 检查任务完成状态
                        task1_completed = player.task1_completed if task.name == 'Task1' else False
                        task2_completed = player.task2_completed if task.name == 'Task2' else False
                        task3_completed = player.task3_completed if task.name == 'Task3' else False
                        task4_completed = player.task4_completed if task.name == 'Task4' else False

                        # 激活任务状态
                        if task.name == 'Task1':
                            player.task1_active = True
                        elif task.name == 'Task2':
                            player.task2_active = True
                        elif task.name == 'Task3':
                            player.task3_active = True
                        elif task.name == 'Task4':
                            player.task4_active = True
                        player.save()

                        nearby_task = {
                            'id': task.id,
                            'name': task.name,
                            'description': task.description,
                            'task1_completed': task1_completed,
                            'task2_completed': task2_completed,
                            'task3_completed': task3_completed,
                            'task4_completed': task4_completed
                        }
                    except Player.DoesNotExist:
                        return JsonResponse({'error': '未找到玩家'}, status=404)
                    break

            return JsonResponse(nearby_task, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
@csrf_exempt
def get_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        task_list = []
        for task in tasks:
            task_info = {
                'id': task.id,
                'name': task.name,
                'description': task.description
            }
            task_list.append(task_info)
        return JsonResponse(task_list, safe=False, status=200)
@csrf_exempt
def activate_nearby_task(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student_id = data.get('studentId')
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            tasks = Task.objects.all()
            nearby_task = None
            for task in tasks:
                if (latitude - 0.002 <= task.latitude <= latitude + 0.002) and (
                        longitude - 0.1 <= task.longitude <= longitude + 0.1):
                    # 获取玩家信息
                    try:
                        player = Player.objects.get(student_id=student_id)
                        # 激活任务状态
                        if task.name == 'Task1':
                            player.task1_active = True
                        elif task.name == 'Task2':
                            player.task2_active = True
                        elif task.name == 'Task3':
                            player.task3_active = True
                        elif task.name == 'Task4':
                            player.task4_active = True
                        player.save()
                        break
                    except Player.DoesNotExist:
                        return JsonResponse({'error': '未找到玩家'}, status=404)

            return JsonResponse({'message': '附近任务已激活'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
@csrf_exempt
def start_task(request):
    if request.method == 'GET':
        try:
            # 从请求的查询参数中获取任务编号
            task_number = request.GET.get('taskNumber')
            if not task_number:
                return JsonResponse({'error': '任务编号缺失'}, status=400)

            # 根据任务编号获取任务
            try:
                task = Task.objects.get(name=f'Task{task_number}')
            except Task.DoesNotExist:
                return JsonResponse({'error': '任务不存在'}, status=404)

            # 获取玩家信息（从查询参数中获取学生 ID）
            student_id = request.GET.get('studentId')
            if not student_id:
                return JsonResponse({'error': '学生 ID 缺失'}, status=400)

            try:
                player = Player.objects.get(student_id=student_id)
            except Player.DoesNotExist:
                return JsonResponse({'error': '玩家不存在'}, status=404)

            # 检查任务是否已激活且未完成
            task_active_key = f'Task{task_number}_active'
            task_completed_key = f'Task{task_number}_completed'
            is_active = getattr(player, task_active_key)
            is_completed = getattr(player, task_completed_key)

            if is_active and not is_completed:
                # 这里可以添加开始任务的逻辑，例如记录任务开始时间等
                # 简单示例：返回任务信息
                task_info = {
                    'id': task.id,
                    'name': task.name,
                    'description': task.description
                }
                return JsonResponse(task_info, status=200)
            else:
                return JsonResponse({'error': '任务未激活或已完成，无法开始'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from.models import Task, Player


@csrf_exempt
def activate_task_by_answer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student_id = data.get('studentId')
            answer = data.get('answer')

            tasks = Task.objects.all()
            for task in tasks:
                if task.answer == answer:
                    # 获取玩家信息
                    try:
                        player = Player.objects.get(student_id=student_id)
                        # 激活任务状态
                        if task.name == 'Task1':
                            player.task1_active = True
                        elif task.name == 'Task2':
                            player.task2_active = True
                        elif task.name == 'Task3':
                            player.task3_active = True
                        elif task.name == 'Task4':
                            player.task4_active = True
                        player.save()
                        return JsonResponse({'message': '任务已激活'}, status=200)
                    except Player.DoesNotExist:
                        return JsonResponse({'error': '未找到玩家'}, status=404)
            return JsonResponse({'error': '未找到匹配的任务'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)