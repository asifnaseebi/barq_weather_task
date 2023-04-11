def read_csv_file(file_path):
    file_contents = []

    with open(file_path, "r") as file_reader:
        content = file_reader.read()

        for line_value in content.split("\n")[1:-1]:
            column_values = line_value.split(",")
            file_contents.append(column_values)

    return file_contents
