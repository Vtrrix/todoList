from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
import uuid

obj = {
    "tasks": [
        {"id": uuid.uuid1(), "task": "abc", "checked": False},
        {"id": uuid.uuid1(), "task": "def", "checked": False},
        {"id": uuid.uuid1(), "task": "ghi", "checked": False},
        {"id": uuid.uuid1(), "task": "jkl", "checked": False},
    ]
}

# GET - Get all the tasks


def get_todo_list(request):
    return JsonResponse(obj)

# POST - Add a new task and save it to DJANGO server


@csrf_exempt
def add_task(request):
    if request.method == "POST":
        print(request.POST.get('task_list'))
        obj['tasks'].append(json.loads(request.POST.get('task_list')))
    return JsonResponse(obj)

# To find element from tasks


def find(lst, value):
    for i, dic in enumerate(lst):
        print(dic["id"])
        if str(dic['id']) == str(value):
            return i
    return -1

# POST - To delete task by id


@csrf_exempt
def del_task(request):
    if request.method == "POST":
        obj['tasks'].remove(
            obj['tasks'][int(find(obj['tasks'],  request.POST.get('task_id')))])
    return JsonResponse(obj)

# POST - To change the status of the task


@csrf_exempt
def change_check(request):
    if request.method == "POST":
        index = int(find(obj['tasks'],  request.POST.get('task_id')))
        if obj['tasks'][index]["checked"]:
            obj['tasks'][index]["checked"] = False
        else:
            obj['tasks'][index]["checked"] = True
    return JsonResponse(obj)
