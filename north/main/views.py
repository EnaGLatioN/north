from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from main import models


def main(request):
    lines = models.Line.objects.all().prefetch_related("tabacco_set")
    data = [
        {
            "line": line.title,
            "slug": line.slug,
            "tabaccos": [
                {
                    "title": tabacco.name,
                    "image": tabacco.image.url,
                    "description": tabacco.description,
                } for tabacco in line.tabacco_set.all()
            ]
        } for line in lines
    ]
    return JsonResponse(
        data=data,
        safe=False,
    )


@csrf_exempt
def order(request):
    if request.method != "POST":
        raise 
    order = models.Order()
    order.full_name = request.POST["full_name"]
    order.company_name = request.POST["company_name"]
    order.city = request.POST["city"]
    order.contact = request.POST["contact"]
    order.save()
    data = {
        "order": {
            "id": order.id,
            "full_name": order.full_name,
            "company_name": order.company_name,
            "city": order.city,
            "contact": order.contact
        }
    }
    return JsonResponse(
        data=data,
        safe=False,
    )