from django.http import JsonResponse


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)
def hello(request):
    data = {"message": "API is running!"}
    return JsonResponse(data)