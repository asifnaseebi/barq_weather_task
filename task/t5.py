from utils.contents import MapperIndex
from utils.reader import read_csv_file

file_path = "/home/asif/Desktop/project/barq_weather_task/files/f2.csv"
csv_data = read_csv_file(file_path)

for content in csv_data:
    date = content[MapperIndex.DATE1]
    events = content[MapperIndex.EVENTS]

    if events in ["Rain", "Snow", "Rain-Snow"]:
        print(events, "date =", date)
