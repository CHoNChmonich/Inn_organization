from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseNotFound
from .utils import fetch_organization_by_inn

def home(request):
    return render(request, "main/home.html")

def org_info(request, inn):
    org_data = fetch_organization_by_inn(inn)
    if org_data:
        management = org_data.get("management")  # Извлекаем данные об основателе
        return render(
            request,
            "main/org_info.html",
            {
                "org_data": org_data,
                "inn": inn,
                "management": management,
            },
        )
    return HttpResponseNotFound("<h1>Организация с указанным ИНН не найдена.</h1>")

