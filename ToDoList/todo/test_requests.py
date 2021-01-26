import requests

response = requests.post("http://127.0.0.1:8000/todo/add_task/", {
    'task_list': {
        "task": "helloBello",
        "checked": False
    }
})
