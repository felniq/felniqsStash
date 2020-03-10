from django.shortcuts import render
from django.http import HttpResponse
from .models import AvailableImages


def index(request):
    all_images_list = AvailableImages.objects.order_by('-pub_date')[:5]
    context = {'all_images_list': all_images_list}
    return render(request, 'felniqsMedia/index.html', context)
