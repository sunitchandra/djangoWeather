from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=30&API_KEY=F9176672-BE3C-4BF8-BE5D-C483FA9C37B5")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api' : api})

def about(request):
    return render(request, 'about.html', {})