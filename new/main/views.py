import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import PlantData


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class AboutPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')


class PlantDataJsonView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8')) 
            search_by = data.get('searchBy')
            field_name = data.get('searchTerm')

            if field_name:
                try:
                    plant_data = None
                    if search_by == 'scientific_name':
                        plant_data = PlantData.objects.filter(scientific_name=field_name).first()

                    elif search_by == 'hausa_name':
                        plant_data = PlantData.objects.filter(hausa_name__name=field_name).first()

                    elif search_by == 'common_name':
                        plant_data = PlantData.objects.filter(common_name__name=field_name).first()

                    if plant_data:
                        response_data = {
                            "scientific_name": plant_data.scientific_name,
                            "family": plant_data.family,
                        }
                        if plant_data.hausa_name.all():
                            response_data["hausa_name"] = [name.name for name in plant_data.hausa_name.all()]
                        if plant_data.common_name.all():
                            response_data["common_name"] = [name.name for name in plant_data.common_name.all()]
                        if plant_data.synonym.all():
                            response_data["synonym"] = [name.name for name in plant_data.synonym.all()]

                        return JsonResponse(response_data, status=200)
                    else:
                        return JsonResponse({"error": "No data found"}, status=404)
                except AttributeError as e:
                    return JsonResponse({"error": "Invalid field name"}, status=400)
            else:
                return JsonResponse({"error": "Field name parameter missing"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
