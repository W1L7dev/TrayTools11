import customtkinter as ctk
import screen_brightness_control as sbc


def brightness_widget(master):
    frame = ctk.CTkFrame(master)

    ctk.CTkLabel(frame, text="Brightness", font=("Arial", 15)).pack()

    current_brightness = int(sbc.get_brightness()[0])

    def set_brightness(value):
        sbc.set_brightness(round(value, 0))

    slider = ctk.CTkSlider(
        frame, from_=0, to=100, orientation="horizontal", command=set_brightness
    )
    slider.set(current_brightness)
    slider.pack(padx=5, pady=5)

    return frame
