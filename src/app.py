import customtkinter as ctk
import json

from widgets import brightness, weather

class App(ctk.CTk):
    def __init__(self, title: str) -> None:
        super().__init__()
        with open("src/widgets/activated.json", "r") as f:
            self.activated = json.load(f)
        self.title(title)

        self.geometry(f"270x700")

        ctk.CTkLabel(self, text="TrayTools11", font=("Arial", 20)).grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        ctk.CTkButton(self, text="X", command=self.destroy, width=25, height=25).grid(row=0, column=3, padx=5, pady=5) #TODO: Close the window into system tray

        brightness.brightness_widget(self).grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        weather.weather_widget(self).grid(row=2, column=0, sticky="nsew", padx=5, pady=5)



if __name__ == "__main__":
    app = App("My App")
    app.overrideredirect(True)
    app.mainloop()