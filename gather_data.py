def gather_temperature(data):
    current_temp=data["main"]["temp"]-272.15
    feelslike_temp=data["main"]["feels_like"]-272.15
    min_temp=data["main"]["temp_min"]-272.15
    max_temp=data["main"]["temp_max"]-272.15
    pressure=data["main"]["pressure"]
    humidity=data["main"]["humidity"]
    return current_temp,feelslike_temp,min_temp,max_temp,pressure,humidity

def gather_wind_data(data):
    wind_speed=data["wind"]["speed"]
    wind_dir=data["wind"]["deg"]
    return wind_speed,wind_dir

def gather_weather_details(data):
    icon_code=data["weather"][0]["icon"]
    weather_description=data["weather"][0]["description"]
    return icon_code,weather_description

def wind_dir(degrees):
    dirs=["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    index=round(degrees/(360./len(dirs)))
    return dirs[index%len(dirs)]

def get_unix_timestamp(data):
    time=data["dt"]
    timezone=data["timezone"]
    sunrise_time=data["sys"]["sunrise"]
    sunset_time=data["sys"]["sunset"]
    return time,timezone,sunrise_time,sunset_time