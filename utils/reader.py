import os

def file_read(file_content):
    with open(file_content) as read_content:
        content = read_content.read()
    rows = []
    for row in content.split("\n")[1:-1]:
        rows.append(row.split(","))

    return rows