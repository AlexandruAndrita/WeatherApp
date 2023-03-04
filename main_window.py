import requests
from tkinter import *
from PIL import ImageTk,Image
import datetime

import gather_data
import format_output
import checking

def disable_event():
    pass

window=Tk()
window.geometry("450x490")
window.title("Weather app")
window.resizable(0,0)
window.configure(bg="gray81")

frame_city_name=Frame(window)

city_label=Label(frame_city_name,text="Enter city:\n",font=('Arial',13),fg="black")
city_label.pack()
city_label.configure(bg="gray81")

city_name=Entry(frame_city_name,font=('Arial',13),fg="black")
city_name.pack()

city_status=Label(frame_city_name,font=('Arial',10),text="Location unavailable",fg="Red")
city_status.pack(pady=3)
city_status.configure(bg="gray81")

frame_city_name.pack(pady=10,padx=10)
frame_city_name.configure(bg="gray81")

def check_city_name(city):
    if len(city)==0 or checking.other_characters(city) is True:
        show_weather_button.configure(state='disabled')
        city_status.configure(text="Location unavailable",fg="Red")
        return False
    else:
        global data
        address="https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid={API_KEY}"
        response=requests.get(address)
        data=response.json()

        if "message" not in data:
            show_weather_button.configure(state='active')
            city_status.configure(text="Location available",fg="green")

            return True
        else:
            show_weather_button.configure(state='disabled')
            city_status.configure(text="Location unavailable", fg="Red")
            return False


def show_weather(data):
    show_weather_button.configure(state='disabled')
    city_name.configure(state='disabled')

    for widget in buttons_frame.winfo_children():
        widget.destroy()
    buttons_frame.destroy()

    current_temp,feelslike_temp,min_temp,max_temp,pressure,humidity=gather_data.gather_temperature(data)
    current_temp=format_output.format_temperature(current_temp)
    feelslike_temp=format_output.format_temperature(feelslike_temp)
    min_temp=format_output.format_temperature(min_temp)
    max_temp=format_output.format_temperature(max_temp)
    pressure=format_output.format_pressure(pressure)
    humidity=format_output.format_humidity(humidity)

    wind_speed,wind_dir=gather_data.gather_wind_data(data)
    wind_speed=format_output.format_wind_speed(wind_speed)
    wind_dir=gather_data.wind_dir(wind_dir)

    icon_code,weather_description=gather_data.gather_weather_details(data)
    weather_description=weather_description.capitalize()

    unix_date_time,timezone,sunrise_time,sunset_time=gather_data.get_unix_timestamp(data)

    date_time=format_output.decode_unix_timestamp(unix_date_time)
    date_time=date_time.split()

    sunrise_time=format_output.decode_unix_timestamp(sunrise_time)
    sunrise_time=sunrise_time.split()

    sunset_time=format_output.decode_unix_timestamp(sunset_time)
    sunset_time=sunset_time.split()

    """
    local time
    """
    current_time=datetime.datetime(int(date_time[0]), int(date_time[1]), int(date_time[2]), int(date_time[3]),
                                     int(date_time[4]), int(date_time[5]))
    current_time=current_time + datetime.timedelta(seconds=timezone)
    current_time=format_output.get_full_timedate(current_time)

    """
    sunrise time
    """
    sunrise_current_time=datetime.datetime(int(sunrise_time[0]), int(sunrise_time[1]), int(sunrise_time[2]), int(sunrise_time[3]),
                                     int(sunrise_time[4]), int(sunrise_time[5]))
    sunrise_current_time=sunrise_current_time + datetime.timedelta(seconds=timezone)
    sunrise_current_time=format_output.get_full_timedate(sunrise_current_time)
    sunrise_current_time=sunrise_current_time[:5]

    """
    sunset time
    """
    sunset_current_time=datetime.datetime(int(sunset_time[0]), int(sunset_time[1]), int(sunset_time[2]),int(sunset_time[3]),
                                           int(sunset_time[4]), int(sunset_time[5]))
    sunset_current_time=sunset_current_time + datetime.timedelta(seconds=timezone)
    sunset_current_time=format_output.get_full_timedate(sunset_current_time)
    sunset_current_time=sunset_current_time[:5]


    image_name="images/"+icon_code+".png"
    icon=ImageTk.PhotoImage(Image.open(image_name))

    image_frame=Frame(window)
    image_label=Label(image_frame, image=icon)
    image_label.image=icon
    image_label.pack()
    image_frame.pack()
    image_frame.configure()
    image_label.configure(bg="gray81")

    description_frame=Frame(window)
    decription_label=Label(description_frame,text=f"{weather_description}",font=('Arial',13))
    decription_label.pack()
    description_frame.pack(pady=2)
    decription_label.configure(bg="gray81")

    weather_details=Frame(window)

    current_temp_label=Label(weather_details,text=f"Now: {current_temp}   ",font=('Arial',13))
    current_temp_label.grid(row=1,column=0)
    current_temp_label.configure(bg="gray81")

    feelslike_temp_label=Label(weather_details,text=f"Feels like: {feelslike_temp}",font=('Arial',13))
    feelslike_temp_label.grid(row=1,column=1)
    feelslike_temp_label.configure(bg="gray81")

    min_temp_label=Label(weather_details,text=f"Min: {min_temp}",font=('Arial',10))
    min_temp_label.grid(row=2,column=0)
    min_temp_label.configure(bg="gray81")

    max_temp_label=Label(weather_details,text=f"Max: {max_temp}",font=('Arial',10))
    max_temp_label.grid(row=2,column=1)
    max_temp_label.configure(bg="gray81")

    pressure_label=Label(weather_details,text=f"Pressure: {pressure}",font=('Arial',10))
    pressure_label.grid(row=3,column=0)
    pressure_label.configure(bg="gray81")

    humidity_label=Label(weather_details,text=f"Humidity: {humidity}",font=('Arial',10))
    humidity_label.grid(row=3,column=1)
    humidity_label.configure(bg="gray81")

    wind_speed_label=Label(weather_details,text=f"Wind speed: {wind_speed}",font=('Arial',10))
    wind_speed_label.grid(row=4,column=0)
    wind_speed_label.configure(bg="gray81")

    wind_dir_label=Label(weather_details,text=f"Wind direction: {wind_dir}",font=('Arial',10))
    wind_dir_label.grid(row=4,column=1)
    wind_dir_label.configure(bg="gray81")

    sunrise_image_path="images/sunrise.png"
    icon = ImageTk.PhotoImage(Image.open(sunrise_image_path))
    sunrise_img_label=Label(weather_details, image=icon)
    sunrise_img_label.image=icon
    sunrise_img_label.grid(row=5,column=0)
    sunrise_img_label.configure(bg="gray81")

    sunset_image_path="images/sunset.png"
    icon = ImageTk.PhotoImage(Image.open(sunset_image_path))
    sunset_img_label=Label(weather_details, image=icon)
    sunset_img_label.image=icon
    sunset_img_label.grid(row=5, column=1)
    sunset_img_label.configure(bg="gray81")

    sunrise_label=Label(weather_details,text=f"{sunrise_current_time}",font=('Arial',10))
    sunrise_label.grid(row=6,column=0)
    sunrise_label.configure(bg="gray81")

    sunset_label=Label(weather_details,text=f"{sunset_current_time}",font=('Arial',10))
    sunset_label.grid(row=6,column=1)
    sunset_label.configure(bg="gray81")

    weather_details.pack()
    weather_details.configure(bg="gray81")

    date_time_frame=Frame(window)
    date_time_label=Label(date_time_frame,text=f"Local time: {current_time}",font=('Arial',10))
    date_time_label.pack()
    date_time_label.configure(bg="gray81")
    date_time_frame.pack(pady=2)

    note_frame=Frame(window)
    note_label=Label(note_frame, text="Note: Reopen the app to run it again", font=('Arial', 10))
    note_label.pack()
    note_label.configure(bg="gray81")
    note_frame.pack(side=BOTTOM)


buttons_frame=Frame(window)
check_city_weather=Button(buttons_frame,text="Check city name",command=lambda :check_city_name(city_name.get()),font=('Arial',13),fg="black",width=15)
check_city_weather.pack()

show_weather_button=Button(buttons_frame,text="Show weather",state='disabled',command=lambda :show_weather(data),font=('Arial',13),fg="black",width=15)
show_weather_button.pack(pady=3)

buttons_frame.pack(pady=6,padx=10)
buttons_frame.configure(bg="gray81")

if __name__=='__main__':
    window.mainloop()