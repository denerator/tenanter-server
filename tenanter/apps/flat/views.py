from django.http import HttpResponse
from .models import Flat


def get_all(request):
    flat = Flat.objects.get(id=2)
    print(flat)
    return HttpResponse(flat)
