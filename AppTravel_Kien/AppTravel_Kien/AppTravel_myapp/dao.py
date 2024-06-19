from django.db.models import Count

from .models import Category, Tour


def load_tour(params = {}):
    q = Tour.onjects.all()
    kw = params.get('kw')
    if kw:
        q = q.objects.filter(name__icontaints=kw)
    cate = params.get('cate_id')
    if cate:
        q = q.objects.filter(category_id=cate)


def count_tour_by_cat():
    return Category.objects.annotate(count = Count('tour__id')).values('id', 'name', 'count')