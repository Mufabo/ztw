MAIN_BUTTONS = ["Meditate", "Settings",  "About"] #, "Donate","Statistics"]
COLOR_GOLDEN_ROD = [0.8549019607843137, 0.6470588235294118, 0.12549019607843137, 1.0]

import json

with open('/home/fatih/ztw/Data/Settings.json') as f:
    SETTINGS = json.load(f)


# class Settings():
#     def __init__(self):
#         file = open("settings.txt", "r")
#         self.DURATION = int(file.readline())
#         self.DTN = int(file.readline())
#         #self.first_side = "right"
#         self.time_for_out= int(file.readline())
#         self.vibrate = file.readline().replace('\n', '')
#         file.close()

# settings = Settings()