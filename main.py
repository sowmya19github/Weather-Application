from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    print("Request:")
    print(json.dumps(req, indent=4))

    res = process_request(req)

    return jsonify(res)

def process_request(req):
    action = req.get('queryResult').get('action')
    if action == 'getWeather':
        return get_weather_response(req)
    else:
        return {}

def get_weather_response(req):
    parameters = req['queryResult']['parameters']
    city = parameters.get('geo-city')
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url).json()
    weather = response['weather'][0]['description']
    temp = response['main']['temp']

    return {
        "fulfillmentText": f"The weather in {city} is {weather} with a temperature of {temp}°C.",
        "source": "weather-app"
    }


if __name__ == '__main__':
    app.run(port=5000, debug=True)
