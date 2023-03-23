from utils.contents import MapperIndex
from utils.reader import read_csv_file
from datetime import datetime


file_path = "/home/asif/Desktop/project/barq_weather_task/files/f2.csv"
csv_data = read_csv_file(file_path)

for content in csv_data:
    date = content[MapperIndex.DATE1]
    date_str = str(date)
    datetime = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = datetime.strftime("%A")
    event = content[MapperIndex.EVENTS]

    if event == "Thunderstorm":
        print(weekday + ' = Thunderstorm')