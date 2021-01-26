from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

obj={
    "tasks" : [
        {"task" : "abc", "checked" : False},
        {"task" : "def", "checked" : False},
        {"task" : "ghi", "checked" : False},
        {"task" : "jkl", "checked" : False},
    ]
}

def get_todo_list(request):
    return JsonResponse(obj)

@csrf_exempt
def add_task(request):
    success = False
    print("testing")
    if request.method == "POST":
        print(f"{request.POST.items()}")
        print(list(request.POST.items()))
        # error found in posting api ------- list used to list data -------------data found in request.POST 
        success = True
        print("testrun123")
    return JsonResponse(obj)
    
