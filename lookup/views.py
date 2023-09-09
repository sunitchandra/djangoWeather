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

    if api[0]["Category"]["Name"] == 'Good':
        category_desctiption = "(0 - 50) Air quality is Good."
        category_color = "good"
    elif api[0]["Category"]["Name"] == 'Moderate':
        category_desctiption = "(51 - 100) Air Quality is Moderate."
        category_color = "moderate"
    elif api[0]["Category"]["Name"] == 'Unhealthy for Sensitive Groups' :
        category_desctiption = "(101 - 150) Air quality is Unhealthy for Sensitive Groups."
        category_color = "usg"
    elif api[0]["Category"]["Name"] == 'Unhealthy' :
        category_desctiption = "(151 - 200) Air quality is Unhealthy."
        category_color = "unhealthy"
    elif api[0]["Category"]["Name"] == 'Very Unhealthy':
        category_desctiption = "(201 - 300) Air quality is Very Unhealthy."
        category_color = "veryunhealthy"
    elif api[0]["Category"]["Name"] == 'Hazardous' :
        category_desctiption = "(301+) Air quality is Hazardous."
        category_color = "hazardous"

    return render(request, 'home.html', {'api' : api, 
                                         'category_desctiption' : category_desctiption,
                                         'category_color' : category_color})

def about(request):
    return render(request, 'about.html', {})