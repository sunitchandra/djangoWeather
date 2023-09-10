from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=30&API_KEY=F9176672-BE3C-4BF8-BE5D-C483FA9C37B5")


        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        category_name = api[0]["Category"]["Name"];
        api_id = 1
        if category_name == 'Good':
            category_desctiption = "(0 - 50) Air quality is Good."
            category_color = "good"
        elif category_name == 'Moderate':
            category_desctiption = "(51 - 100) Air Quality is Moderate."
            category_color = "moderate"
        elif category_name == 'Unhealthy for Sensitive Groups' :
            category_desctiption = "(101 - 150) Air quality is Unhealthy for Sensitive Groups."
            category_color = "usg"
        elif category_name == 'Unhealthy' :
            category_desctiption = "(151 - 200) Air quality is Unhealthy."
            category_color = "unhealthy"
        elif category_name == 'Very Unhealthy':
            category_desctiption = "(201 - 300) Air quality is Very Unhealthy."
            category_color = "veryunhealthy"
        elif category_name == 'Hazardous' :
            category_desctiption = "(301+) Air quality is Hazardous."
            category_color = "hazardous"

        return render(request, 'home.html', {'api' : api, 
                                            'api_id' : api_id,
                                            'category_desctiption' : category_desctiption,
                                            'category_color' : category_color})
    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=30&API_KEY=F9176672-BE3C-4BF8-BE5D-C483FA9C37B5")
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=67052&distance=30&API_KEY=F9176672-BE3C-4BF8-BE5D-C483FA9C37B5")


        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        category_name = api[1]["Category"]["Name"];
        api_id = 1
        if category_name == 'Good':
            category_desctiption = "(0 - 50) Air quality is Good."
            category_color = "good"
        elif category_name == 'Moderate':
            category_desctiption = "(51 - 100) Air Quality is Moderate."
            category_color = "moderate"
        elif category_name == 'Unhealthy for Sensitive Groups' :
            category_desctiption = "(101 - 150) Air quality is Unhealthy for Sensitive Groups."
            category_color = "usg"
        elif category_name == 'Unhealthy' :
            category_desctiption = "(151 - 200) Air quality is Unhealthy."
            category_color = "unhealthy"
        elif category_name == 'Very Unhealthy':
            category_desctiption = "(201 - 300) Air quality is Very Unhealthy."
            category_color = "veryunhealthy"
        elif category_name == 'Hazardous' :
            category_desctiption = "(301+) Air quality is Hazardous."
            category_color = "hazardous"

        return render(request, 'home.html', {'api' : api, 
                                            'api_id' : api_id,
                                            'category_desctiption' : category_desctiption,
                                            'category_color' : category_color})

def about(request):
    return render(request, 'about.html', {})