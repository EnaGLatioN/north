from django.http import JsonResponse, HttpResponseNotAllowed
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
                    "tags": [{
                        "title": tag.title,
                        "title_eng": tag.title_eng,
                        "title_china": tag.title_china,
                        "color": tag.color,
                        "text_color": tag.text_color
                        } for tag in tabacco.tag.all()
                    ],
                    "weights": [weight.weight for weight in tabacco.weight.all()]

                } for tabacco in line.tabacco_set.all().order_by("order")
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
        return HttpResponseNotAllowed(["POST"])

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
    return JsonResponse(data)


def map_point(request):
    map_points = models.MapPoint.objects.filter(
        is_active=True,
    ).order_by(
        "name"
    )
    return JsonResponse(
        data=[
        {
            "id": map_point.id,
            "name": map_point.name,
            "city": map_point.city,
            "city_eng": map_point.city_eng,
            "city_china": map_point.city_china,
            "address": map_point.address,
            "address_eng": map_point.address_eng,
            "address_china": map_point.address_china,
            "is_active": map_point.is_active,
            "contact": map_point.contact,
            "coordinate_x": map_point.coordinate_x,
            "coordinate_y": map_point.coordinate_y,
            "country": map_point.map_info.country,
            "country_eng": map_point.map_info.country_eng,
            "country_china": map_point.map_info.country_china,
            "created_at": map_point.created_at,
            "updated_at": map_point.updated_at,
            "count": len(map_points),
        } for map_point in map_points
    ],
        safe=False,
    )
