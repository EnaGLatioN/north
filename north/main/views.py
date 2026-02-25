from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from main import models


def main(request):
    lines = models.Line.objects.all().prefetch_related("tabacco_set").order_by("order")
    data = [
        {
            "line": line.title,
            "slug": line.slug,
            "line_china": line.title_china,
            "slug_china": line.slug_china,
            "line_eng": line.title_eng,
            "slug_eng": line.slug_eng,
            "tabaccos": [
                {
                    "title": tabacco.name,
                    "image": tabacco.image.url,
                    "description": tabacco.description,
                    "title_eng": tabacco.name_eng,
                    "description_eng": tabacco.description_eng,
                    "title_china": tabacco.name_china,
                    "description_china": tabacco.description_china,
                    "order": tabacco.order,
                    "tags": [{
                        "title": tag.title,
                        "title_eng": tag.title_eng,
                        "title_china": tag.title_china,
                        "color": tag.color,
                        "text_color": tag.text_color
                        } for tag in tabacco.tag.all()
                    ],
                    "weights": [weight.weight for weight in tabacco.weight.all()]

                } for tabacco in line.tabacco_set.all()
            ],

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