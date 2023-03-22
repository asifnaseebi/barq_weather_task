from utils.reader import file_read
from datetime import datetime


file_content = file_read("/home/asif/Desktop/project/barq_weather_task/files/f2.csv")
for file_value in file_content:
    date = file_value[1]
    datetime = datetime.strptime(date,"%Y-%m-%d")
    weekday = datetime.strftime("%A")
    event = file_value[-2]

    if event == "Thunderstorm":
        print(weekday + ' = Thunderstorm')