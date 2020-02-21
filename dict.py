weather = {'city': 'Москва', 'temperature': -1}
print(weather['city'])
weather['temperature'] = weather['temperature'] - 5
print(weather)
a = weather.get('country', 'Россия')
print (a)
weather['date'] = '27.05.2019'
print(len(weather))
print(weather)