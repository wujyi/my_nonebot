import json
import requests


async def get_weather_of_city(city: str) -> str:
    res = requests.get(
        f'https://api.seniverse.com/v3/weather/now.json?key=SjS16fRudAvyYFP_s&location={city}&language=zh-Hans&unit=c')
    obj_dic = json.loads(res.text)
    weather1 = obj_dic['results'][0]['now']['text']
    weather2 = obj_dic['results'][0]['now']['temperature']
    return f'{city}的天气是:{weather1}' + '\n' + f'温度是：{weather2}'


async def get_weather_of_city_text(city: str) -> str:
    res = requests.get(
        f'https://geoapi.qweather.com/v2/city/lookup?&location={city}&key=329efb5be5d14df2ba3fa7180d85eca9')
    obj_dic = json.loads(res.text)
    location_id = obj_dic['location'][0]['id']
    message = requests.get(
        f'https://devapi.qweather.com/v7/weather/now?&location={location_id}&key=329efb5be5d14df2ba3fa7180d85eca9')
    obj = json.loads(message.text)
    temp = obj['now']['temp']
    feels_like = obj['now']['feelsLike']
    weather = obj['now']['text']
    wind2 = obj['now']['windDir']
    wind3 = obj['now']['windScale']
    wind4 = obj['now']['windSpeed']
    humidity = obj['now']['humidity']
    return f'{city}天气情况如下:\n温度：{temp}\n体感温度:{feels_like}\n天气情况:{weather}\n' \
           f'风向:{wind2}\n风力等级:{wind3}\n风速:{wind4}\n相对湿度:{humidity}'
