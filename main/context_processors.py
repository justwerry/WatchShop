from .models import Brand

def navbar(request):
    brands = Brand.objects.all()
    return {'brands': brands}
