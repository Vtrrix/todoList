from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json


obj = {
    "tasks": [
        {"task": "abc", "checked": False},
        {"task": "def", "checked": False},
        {"task": "ghi", "checked": False},
        {"task": "jkl", "checked": False},
    ]
}


def get_todo_list(request):
    return JsonResponse(obj)


@csrf_exempt
def add_task(request):
    success = False
    if request.method == "POST":
        # print(f"{request.POST.items()}")
        # print(dict(request.POST.items()))
        # obj['tasks'].append(dict(request.POST.items()))
        # print(obj)
        print(request.POST.get('task_list'))
        obj['tasks'].append(json.loads(request.POST.get('task_list')))
        # obj['tasks'].append(request.POST.get('task_list'))
        # print(obj)
    return JsonResponse(obj)
