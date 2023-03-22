from utils.reader import file_read

file_content = file_read( "/home/asif/Desktop/project/barq_weather_task/files/f1.csv")
for row in file_content:
    date = row[0]
    max_tmp = row[1]
    min_tmp = row[3]
    max_min_diff = int(max_tmp) - int(min_tmp)
    average = max_min_diff/2
    print(date,"max and mini average =", average )