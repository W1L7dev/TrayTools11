import wmi
import customtkinter as ctk


def drives_widget(master):
    frame = ctk.CTkFrame(master, width=270, height=100)
    ctk.CTkLabel(frame, text="Drives", font=("Arial", 15)).pack()

    drives_dict = {}
    drives = wmi.WMI().Win32_LogicalDisk()
    for drive in drives:
        if drive.DriveType in [2, 3]:
            drives_dict[drive.Caption] = {
                "name": drive.VolumeName,
                "capacity": round(int(drive.Size) / 1024**3, 2),
                "free": round(int(drive.FreeSpace) / 1024**3, 2),
            }


    # for each drive in drives_dict, create a frame


    for drive in drives_dict:
        drive_frame = ctk.CTkFrame(frame)
        drive_frame.pack(fill="x", padx=5, pady=5)

        ctk.CTkLabel(drive_frame, text=f"{drive} ({drives_dict[drive]['name']})").pack(
            side="left", padx=5, pady=5
        )

        capacity = float(drives_dict[drive]["capacity"])
        free = float(drives_dict[drive]["free"])
        usage = round((capacity - free) / capacity * 100, 2)

        print(f"[DRIVE] {drives_dict[drive]}\n[CAPACITY] {capacity}\n[FREE] {free}\n[USAGE] {usage}\n-------")
        prgress_bar = ctk.CTkProgressBar(drive_frame, width=100, height=10)
        prgress_bar.pack(side="right", padx=5, pady=5)
        prgress_bar.set(usage/100)
    return frame


if __name__ == "__main__":
    print(drives_widget())
