from utils.reader import file_read

file_content = file_read( "/home/asif/Desktop/project/barq_weather_task/files/f2.csv")
for files_value in file_content:
    date = files_value[1]
    events = files_value[-2]

    if events in ["Rain", "Snow","Rain-Snow"]:
        print(events, "date =", date)