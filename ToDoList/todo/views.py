from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
import uuid

a = uuid.uuid1()
b = uuid.uuid1()
c = uuid.uuid1()
d = uuid.uuid1()
obj = {
    "tasks": [
        {"id": 1, "task": "abc", "checked": False},
        {"id": 2, "task": "def", "checked": False},
        {"id": 3, "task": "ghi", "checked": False},
        {"id": 4, "task": "jkl", "checked": False},
    ]
}


def get_todo_list(request):
    return JsonResponse(obj)


@csrf_exempt
def add_task(request):
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


def find(lst, value):
    # print(lst)
    for i, dic in enumerate(lst):
        # print(i)
        print(dic["id"])
        # print(value)
        if int(dic['id']) == int(value):
            print("----------")
            print(value)
            print(dic['id'])
            print("----------")
            return i
    return -1
    # res = [dic['id'] for dic in lst]
    print(res)


@csrf_exempt
def del_task(request):
    if request.method == "POST":
        print(request.POST.get('task_id'))
        obj['tasks'].remove(
            obj['tasks'][int(find(obj['tasks'],  request.POST.get('task_id')))])
    return JsonResponse(obj)
