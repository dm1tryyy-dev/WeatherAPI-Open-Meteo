# WEATHER API with Open-Meteo // 2025, dm1tryyy-dev, Лицензия: Apache 2.0 (cм. LICENSE.md)
# Зависимости: requests

from parsing import *
from city_class import City

class_city = City()
class_city.input()

def main():
	"""Основная функция для вывода"""
	try:
		weather_data = class_city.weather()

		# Вывод
		weather = weather_data['current_weather']
		daily_weather = weather_data['daily']
		cardinal_direct = cd(weather['winddirection'])
		code = weather_code(weather['weathercode'], weather['windspeed'])
		time = get_time(weather['time'])

		print(f'\n\n⛅ Текущая погода:\n')
		print(f"""Время: {time};
Температура: {weather['temperature']}°C;
Скорость ветра: {weather['windspeed']} км/ч;
Направление ветра: {weather['winddirection']}° | {cardinal_direct};
Описание: {code}
""")
		print('---------------------------------------------\n')
		print('🗓️ Прогноз на 7 дней: \n')
		for i in range(7):
			code = weather_code(daily_weather['weather_code'][i], daily_weather['wind_speed_10m_max'][i])
			print(f'День {i+1}')
			print(f'''
Дата: {daily_weather['time'][i]}
Макс. температура: {daily_weather['temperature_2m_max'][i]}°C
Мин. температура: {daily_weather['temperature_2m_min'][i]}°C
Макс. скорость ветра (на высоте 10 м): {daily_weather['wind_speed_10m_max'][i]} км/ч
Описание: {code}
''')
			print('======================================\n')

	except Exception as e:
		print(f'[ERROR] -- Произошла ошибка: {e}')


if __name__ == '__main__':
	main()
