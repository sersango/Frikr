from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from photos.models import Photo, PUBLIC

def home(request):
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        'photos_list': photos[:5]
    }
    return render(request, 'photos/home.html', context)

def detail(request, pk):
    possible_photos = Photo.objects.filter(pk=pk)
    photo = possible_photos[0] if len(possible_photos) == 1 else None
    if photo is not None:
        context = {
            'photo': photo
        }
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound("No existe la foto.") # 404 Not Found