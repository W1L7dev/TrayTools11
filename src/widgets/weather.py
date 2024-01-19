import geocoder
import requests
import customtkinter as ctk


def weather_widget(master):
    frame = ctk.CTkFrame(master, width=400, height=100)
    ctk.CTkLabel(frame, text="Weather", font=("Arial", 15)).pack()

    ip = geocoder.ip("me")
    latitute = ip.latlng[0]
    longitude = ip.latlng[1]

    # weather api
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    payload = {
        "lat": latitute,
        "lon": longitude,
        "units": "metric",
        "APPID": "3e1e6fe426a0d5b112fd0aead01703aa",
    }
    r = requests.get(base_url, params=payload)

    data = r.json()

    ctk.CTkLabel(frame, text=f"Currently is {round(data["main"]["temp"])}°C in {data['name']}").pack(padx=5, pady=5)

    return frame
