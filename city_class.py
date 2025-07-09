import requests
import time

URL = 'https://api.open-meteo.com/v1/forecast'

class City():
	def __init__(self):
		self.city = ''
	def input(self):
		self.city = input('В каком городе вы хотите узнать погоду? Введите название города: ').strip()
		
	def get_coordinates(self):
		"""Получение координат города через API"""
		try:
			geocode_url = 'https://geocoding-api.open-meteo.com/v1/search'
			params = {
				'name': self.city,
				'count': 1,
				'language': 'ru',
			}
			geo_response = requests.get(geocode_url, params=params)
			geo_data = geo_response.json()

			if not geo_data.get('results'):
				print('Такой город не найден.')
				return None
			
			location = geo_data['results'][0]
			lat = location['latitude']
			lon = location['longitude']
			print(f'\nГород: {location["name"]}')
			print(f'Координаты:')
			print(f'Широта: {lat}, Долгота: {lon}')
			print(f"Тайм-зона: {location['timezone']}")
			return lat, lon
		except Exception as e:
			print(f'Произошла ошибка в геокодировании региона: {e}')
			return None
	
	def get_weather(self):
		try:
			coordinates = self.get_coordinates()
			print(f'''\nПодождите 1 минуту для точных данных...
ПРИМЕЧАНИЕ: Если пришло сообщение, что города не существует, то прервите процесс (CTRL-C), чтобы не ждать, в любом случае произойдёт ошибка! Убедитесь, что город такой существует и написан правильно.
''')
			time.sleep(60) # можно закомментировать для быстрого ответа или изменить значение (по желанию)
			print(f'Данные для города: {self.city} обновлены')
			return coordinates
		except KeyboardInterrupt:
			print('Процесс получения точных данных прерван пользователем')

	def weather(self):
		"""Основная функция для получения данных погоды"""
		try:
			try:
				lat, lon = self.get_weather()
				params = {
					'latitude': lat, # ширина
					'longitude': lon, # долгота
					'current_weather': True, # не задокументированный параметр API, но рабочий (показывает текущую погоду, по умолчанию с базовыми параметрами: temperature, windspeed, winddirection и weathercode)
					'daily': 'weather_code,temperature_2m_max,temperature_2m_min,wind_speed_10m_max', # данные для прогноза следующих дней
					'timezone': 'auto', # автоматическое распознавание тайм-зоны по координатам города
					'forecast_days': 7, # количество дней для прогноза (неделя)
				}
				response = requests.get(URL, params=params)
				response.raise_for_status()
				weather_data = response.json()
				return weather_data
			except Exception as e:
				if not weather_data:
					print(f'Произошла ошибка в получении JSON: {e}')
		except requests.exceptions.HTTPError as http_err:
			print(f'[ERROR] -- Ошибка API: {http_err} // URL: {http_err.response.url} // Text: {http_err.response.text[:100]}')
		except requests.exceptions.Timeout as t:
			print(f'[ERROR] -- Превышено время ожидания запроса: {t}')