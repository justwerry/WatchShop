from django.shortcuts import render

from main.models import Watch, Model, Brand


def index(request):
    models = Model.objects.all()
    return render(request, 'main/index.html', {'models': models})


def watch_list(request, slug):
    watches = Watch.objects.filter(models__slug=slug)
    return render(request, 'main/watch_list.html', {'watches': watches})


def brand_detail(request, pk):
    brand = Brand.objects.get(pk=pk)
    brand_watches = brand.watches.all()

    return render(request, 'main/brand_detail.html', {'brand': brand, 'watches': brand_watches})
