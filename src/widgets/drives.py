import string
from ctypes import windll
import wmi


def get_drives():
    drives = []
    # first, iterate over all letters in the alphabet and see if they are used
    # to label a drive
    for letter in string.ascii_uppercase:
        if windll.kernel32.GetDriveTypeW(letter + ":/") > 1:
            drives.append(letter + ":/")

        # now, check for the names by the letter found above
    DRIVE_TYPES = {
        0: "Unknown",
        1: "No Root Directory",
        2: "Removable Disk",
        3: "Local Disk",
        4: "Network Drive",
        5: "Compact Disc",
        6: "RAM Disk",
    }

    names = []
    c = wmi.WMI()
    for drive in c.Win32_LogicalDisk():
        names.append(drive.VolumeName)

    return dict(zip(drives, names))


if __name__ == "__main__":
    print(get_drives())
