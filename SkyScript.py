import tkinter as tk
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.label_city = tk.Label(root, text="Enter City:")
        self.label_city.pack()

        self.entry_city = tk.Entry(root)
        self.entry_city.pack()

        self.button_get_weather = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.button_get_weather.pack()

        self.label_weather_info = tk.Label(root, text="")
        self.label_weather_info.pack()

    def get_weather(self):
        city = self.entry_city.get()

        if city:
            api_key = ""
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            response = requests.get(url)
            data = response.json()

            if data["cod"] == 200:
                weather_info = f"Weather in {city}: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}°C"
                self.label_weather_info.config(text=weather_info)
            else:
                self.label_weather_info.config(text="City not found")
        else:
            self.label_weather_info.config(text="Please enter a city")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
