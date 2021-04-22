import urllib.request
from json import load
import datetime

def input_data():
    city = str(input('Введите название города: ').lower())
    days = str(input('Введите количество дней: '))
    return city, days

def rlink(city, days):
    link = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={days}&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8")
    res = load(link)
    return res

def import_to_file(res):
    with open('19-09-2020-Odessa-5-days-weather-forecast.txt', 'w', encoding='utf-8') as file:
        file.write(str(f"""Город {city.title()}:Дата:    Температура днем:    Температура ночью:    По ощущениям:    """))
        for i in res['list']:
            file.write(datetime.datetime.fromtimestamp(i['dt']).strftime("\n%d-%m-%Y   "))
            file.write((str(i['temp']['day'])).ljust(19))
            file.write((str(i['temp']['night'])).ljust(20))
            file.write(str(i['feels_like']['day']))


city, days = input_data()
res = rlink(city, days)
import_to_file(res)