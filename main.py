import requests

# API-ключ от OpenWeatherMap
api_key='c1acd03887d05e07d45977b8a6c8ba21'
# Запрос к API OpenWeatherMap
print('Введите город')
city = input()
url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

response=requests.get(url)

# Проверка статуса ответа
if response.status_code==200:
    # Определение ответа от JSON
    data=response.json()
# Извлечение данных
    city=data['name']
    temperature=data['main']['temp']
    description=data['weather'][0]['description']
    min_temperature=data['main']['temp_min']
    max_temperature=data['main']['temp_max']
    visibil=data['visibility']
# Вывод погоды

    print(f'Погода в городе {city}:')
    print(f'Температура: {temperature}°C')
    print(f'Погодные условия: {description}')
    print(f'Минимальная температура: {min_temperature}')
    print(f'Максимальная температура: {max_temperature}')
    print(f'Видимость: {visibil}')
else:
    print('Ошибка')
res=requests.get('http://api.openweathermap.org/data/2.5/forecast', params={'q' : city, 'units':'metric', 'lang': 'ru', 'APPID':api_key
})
data=res.json()
for i in data['list']:
    print("Дата:",i['dt_txt'])
    print("Температура:",i['main']['temp'])
    print("Погодные условия:",i['weather'][0]['description'])
    print("Минимальная темппература:",i['main']['temp_min'])
    print("Максимальная температура:",i['main']['temp_max'])
    print("Видимость:",i['visibility'])
