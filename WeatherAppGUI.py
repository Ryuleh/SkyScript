import tkinter as tk
from tkinter import ttk
import requests

class WeatherAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.label_city = tk.Label(root, text="Enter City:")
        self.label_city.pack()

        self.entry_city = tk.Entry(root)
        self.entry_city.pack()

        self.label_color = tk.Label(root, text="Choose Background Color:")
        self.label_color.pack()

        self.color_options = ["blue", "red", "green", "yellow", "white"]
        self.combobox_color = ttk.Combobox(root, values=self.color_options, state="readonly")
        self.combobox_color.pack()

        self.button_get_weather = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.button_get_weather.pack()

        self.label_weather_info = tk.Label(root, text="")
        self.label_weather_info.pack()

        # Call change_background_color when combobox selection changes
        self.combobox_color.bind("<<ComboboxSelected>>", self.change_background_color)

    def change_background_color(self, event):
        selected_color = self.combobox_color.get()
        self.root.configure(background=selected_color)

    def get_weather(self):
        city = self.entry_city.get()
        selected_color = self.combobox_color.get()

        if city and selected_color:
            api_key = "18f288af74819083651d36a1806616d1"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            response = requests.get(url)
            data = response.json()

            if data["cod"] == 200:
                weather_info = f"Weather in {city}: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}°C"
                self.label_weather_info.config(text=weather_info)
            else:
                self.label_weather_info.config(text="City not found")
        else:
            self.label_weather_info.config(text="Please enter a city and select a color")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherAppGUI(root)
    root.mainloop()
