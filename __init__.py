import flask
import json

app = flask.Flask(__name__)
@app.route("/data/2.5/weather", methods=["GET"])
def weather():
        return json.dumps({
            "coord": {
                "lon": -123.262,
                "lat": 44.5646
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 289.73,
                "feels_like": 289.66,
                "temp_min": 288.2,
                "temp_max": 291.33,
                "pressure": 1021,
                "humidity": 85
            },
            "visibility": 10000,
            "wind": {
                "speed": 4.12,
                "deg": 170
            },
            "clouds": {
                "all": 100
            },
            "dt": 1664469584,
            "sys": {
                "type": 2,
                "id": 2040223,
                "country": "US",
                "sunrise": 1664460511,
                "sunset": 1664503079
            },
            "timezone": -25200,
            "id": 5720727,
            "name": "Corvallis",
            "cod": 200
        })

if __name__ == "__main__":
    app.run(port=80, debug=True)