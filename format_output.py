from datetime import datetime

def format_temperature(temperature):
    return str(int(temperature))+"°C"

def format_pressure(pressure):
    return str(pressure)+"hPa"

def format_humidity(humidity):
    return str(humidity)+"%"

def format_wind_speed(wind):
    return str(wind)+"m/s"

def decode_unix_timestamp(unix_time):
    date_time=datetime.utcfromtimestamp(unix_time).strftime('%Y %m %d %H %M %S')
    return date_time

def get_full_timedate(time):
    return time.strftime('%H:%M:%S %d-%m-%Y')