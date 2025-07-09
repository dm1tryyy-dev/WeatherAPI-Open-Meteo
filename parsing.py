from datetime import datetime, timezone

# Парсинг
def cd(corner):
	"""Определение сторон света"""
	corner = corner % 360
	if corner == 0:
		return 'N | Север'
	elif corner == 90:
		return 'E | Восток'
	elif corner == 180:
		return 'S | Юг'
	elif corner == 270:
		return 'W | Запад'
	elif 0 < corner < 90:
		return 'NE | Северо-Восток'
	elif 90 < corner < 180:
		return 'SE | Юго-Восток'
	elif 180 < corner < 270:
		return 'SW | Юго-Запад'
	elif 270 < corner < 360:
		return 'NW | Северо-Запад'
	else:
		return 'N/A'
	
def weather_code(code, wind_speed):
	"""Определение состояния погоды по коду из JSON-ответа"""
	if code == 0:
		return 'Ясное небо. [Code: 0]'
	elif code in [1,2,3]:
		if code == 1:
			return 'Преимущественно ясно. [Code: 1]'
		elif code == 2:
			return 'Переменная облачность. [Code: 2]'
		else:
			return 'Пасмурная погода. [Code: 3]'
	elif code == 45:
		return 'Туман. [Code: 45]'
	elif code == 48:
		return 'Оседающий изморозь. [Code: 48]'
	elif code in [51, 53, 55]:
		if code == 51:
			return 'Слабая морось. [Code: 51]'
		elif code == 53:
			return 'Умеренная морось. [Code: 53]'
		else:
			return 'Интенсивная морось. [Code: 55]'
	elif code == 56:
		return 'Замерзающая морось со слабой интенсивностью. [Code: 56]'
	elif code == 57:
		return 'Замерзающая морось с плотной интенсивностью. [Code: 57]'
	elif code in [61, 63, 65]:
		if code == 61:
			return 'Слабый дождь. [Code: 61]'
		elif code == 63:
			return 'Умеренный дождь. [Code: 63]'
		else:
			return 'Сильный дождь. [Code: 65]'
	elif code == 66:
		return 'Замерзающий дождь со слабой интенсивностью. [Code: 66]'
	elif code == 67:
		return 'Замерзающий дождь с плотной интенсивностью. [Code: 67]'
	elif code in [71, 73, 75]:
		if code == 71:
			return 'Слабый снегопад. [Code: 71]'
		elif code == 73:
			return 'Умеренный снегопад. [Code: 73]'
		else:
			return 'Сильный снегопад. [Code: 75]'
	elif code == 77:
		return 'Погода со снежными зёрнами. [Code: 77]'
	elif code in [80, 81, 82]:
		if code == 80:
			return 'Слабый ливневый дождь. [Code: 80]'
		elif code == 81:
			return 'Умеренный ливневый дождь. [Code: 81]'
		else:
			return 'Сильный ливневый дождь. [Code: 82]'
	elif code == 85:
		return 'Слабый снежный ливень. [Code: 85]'
	elif code == 86:
		return 'Сильный снежный ливень. [Code: 86]'
	elif code == 95:
		if wind_speed < 15:
			return 'Слабая гроза без града [Code: 95]'
		else:
			return 'Умеренная гроза без града [Code: 95]'
	elif code == 96:
		return 'Гроза с небольшим градом. [Code: 96]'
	elif code == 99:
		return 'Гроза с крупным градом. Будьте осторожны! [Code: 99]'
	
def get_time(t):
	"""Форматирование времени"""
	dt = datetime.fromisoformat(t)
	time_utc = dt.replace(tzinfo=timezone.utc)
	formatted_time = time_utc.strftime('%Y-%m-%d %H:%M %Z')
	return formatted_time