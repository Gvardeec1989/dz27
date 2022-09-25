import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


def root(request):
    return JsonResponse({'status': 'ok'})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        result = []
        for cat in categories:
            result.append({"id": cat.id, "name": cat.name})
        return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        data = json.loads(request.body)
        new_category = Category.objects.create(name=data['name'])
        return JsonResponse({'id': new_category.id, 'name': new_category.name}, safe=False,
                            json_dumps_params={'ensure_ascii': False})


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({'id': cat.id, 'name': cat.name}, safe=False,
                            json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        all_ads = Ad.objects.all()
        result = []
        for ad in all_ads:
            result.append(
                {"id": ad.id, "name": ad.name,
                 "author": ad.author, "price": ad.price,
                 "description": ad.description, "is_published": ad.is_published})
        return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        data = json.loads(request.body)
        new_ad = Ad.objects.create(
            name=data['name'],
            author=data['author'],
            price=data['price'],
            description=data['description'],
            is_published=data['is_published'] if 'is_published' in data else False
        )
        return JsonResponse({"id": new_ad.id, "name": new_ad.name,
                             "author": new_ad.author, "price": new_ad.price,
                             "description": new_ad.description, "is_published": new_ad.is_published}, safe=False,
                            json_dumps_params={'ensure_ascii': False})


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({"id": ad.id, "name": ad.name,
                             "author": ad.author, "price": ad.price,
                             "description": ad.description, "is_published": ad.is_published}, safe=False,
                            json_dumps_params={'ensure_ascii': False})
