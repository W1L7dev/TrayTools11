import customtkinter as ctk
import json

from widgets import brightness, weather, drives

class App(ctk.CTk):
    def __init__(self, title: str) -> None:
        super().__init__()
        with open("src/widgets/activated.json", "r") as f:
            self.activated = json.load(f)
        self.title(title)

        self.geometry(f"270x700")

        ctk.CTkLabel(self, text="TrayTools11", font=("Arial", 20)).pack(padx=5, pady=5)

        brightness.brightness_widget(self).pack(padx=5, pady=5)
        weather.weather_widget(self).pack(padx=5, pady=5)
        drives.drives_widget(self).pack(padx=5, pady=5)


if __name__ == "__main__":
    app = App("My App")
    app.overrideredirect(True)
    app.mainloop()