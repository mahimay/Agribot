import pyowm
from pyowm import timeutils
from datetime import timedelta, datetime

degree_sign= u'\N{DEGREE SIGN}'
owm = pyowm.OWM('31e7126f775261614941102fda226d01') # TODO: Replace <api_key> with your API key
try:

    import telepot
    token = '808329271:AAFFaghveDDBBA4t_h-k94Nasmh6_5_2Vmo'
    TelegramBot = telepot.Bot(token)
    a = TelegramBot.getUpdates(649179764+1)
    b = a[-1]["message"]["text"]
    
    city_name = str(b)
    forecaster = owm.three_hours_forecast(city_name)
    print('Three hours forecast')
    print('Rain : ' + str(forecaster.will_have_rain()))
    print('fog : ' + str(forecaster.will_have_fog()))
    print('clouds : ' + str(forecaster.will_have_clouds()))
    time=datetime.now() 
    weather = forecaster.get_weather_at(time)
    wind=weather.get_wind()  
    humidity=weather.get_humidity()    
    temperature=weather.get_temperature(unit='celsius')['temp']
    x = ('The temperature at ' + time.strftime('%Y-%m-%d %H:%M:%S') + ' is ' + str(temperature) + degree_sign +'C')
    y = ('The weather on ' + time.strftime('%Y-%m-%d %H:%M:%S') + ' is ' + str(weather.get_status()))
    z = ('Wind status: ' + str(wind))
    m = ('Humidity status: ' + str(humidity))

    import telegram_send
    telegram_send.send(messages=[x])
    telegram_send.send(messages=[y])
    telegram_send.send(messages=[z])
    telegram_send.send(messages=[m])
    
except:
    print("Oops!  It wasn't valid city.  Try again...")
