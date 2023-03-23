from utils.contents import MapperIndex
from utils.reader import read_csv_file

file_path = "/home/asif/Desktop/project/barq_weather_task/files/f1.csv"
csv_data = read_csv_file(file_path)

for content in csv_data:
    date = content[MapperIndex.DATE]
    max_temperature = float(content[MapperIndex.MAX_TEMPERATURE])
    min_temperature = float(content[MapperIndex.MIN_TEMPERATURE])
    max_min_difference = int(max_temperature) - int(min_temperature)
    average = max_min_difference/2

    print(date, "max and mini average =", average)
