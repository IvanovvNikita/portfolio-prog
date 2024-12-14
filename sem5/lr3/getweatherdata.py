import requests
import json

def get_weather_data(place, api_key=None):
    """
    Получает данные о погоде для указанного местоположения с использованием             OpenWeatherMap API.

    Аргументы:
    - place (строка): Местоположение, для которого требуется получить данные о         погоде.
    - api_key (строка): Ключ API для доступа к OpenWeatherMap API.

    Возвращает:
    JSON-строку с данными о погоде, или None, если произошла ошибка.

    """
    
    if not place or api_key is None:
        return None

    url = f"https://api.openweathermap.org/data/2.5/weather?units=metric&lang=ru&q={place}&appid={api_key}"
    data = requests.get(url).json()
    response_code = data.get("cod")
    if response_code != 200:
        return None
    result = {
        "name": data.get("name"),
        "coord": {
            "lon": data.get("coord").get("lon"),
            "lat": data.get("coord").get("lat")
        },
        "timezone": data.get("timezone"),
        "country": data.get("sys").get("country"),
        "feels_like": data.get("main").get("feels_like")
    }

    utc_offset = data["timezone"] / 3600
    sign = "+" if utc_offset >= 0 else "-"
    hours = abs(int(utc_offset))
    timezone_string = f"UTC{sign}{hours}"
    result["timezone"] = timezone_string

    return json.dumps(result, ensure_ascii=False)

if __name__ == "__main__":
    import os
    import json
    import pprint
    api_key = os.environ['API_KEY']
    pprint.pprint(get_weather_data("Санкт-Петербург", api_key))
    pprint.pprint(get_weather_data("Северск", api_key))
    