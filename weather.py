from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "7f9d0481226336e933cf6ceee4a3f526"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not lat or not lon:
        return jsonify({"error": "Location not provided"}), 400

    # Fetch Weather Data using Coordinates
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    if weather_data.get("cod") != 200:
        return jsonify({"error": "Could not fetch weather. Try again!"}), 400

    # Extract Weather Information
    weather_info = {
        "city": weather_data['name'],
        "temperature": weather_data['main']['temp'],
        "description": weather_data['weather'][0]['description'].capitalize(),
        "humidity": weather_data['main']['humidity'],
        "wind_speed": weather_data['wind']['speed']
    }

    return jsonify(weather_info)

if __name__ == '__main__':
    app.run(debug=True)
