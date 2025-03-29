import json

with open("laba_6_test.json") as file:
    tables = json.load(file)

for table in tables:
    csv = ""
    # Записываем заголовки
    headers = tables[table][0].keys()
    csv += ",".join(f'"{h}"' for h in headers) + "\n"

    # Записываем данные
    for data in tables[table]:
        row = ",".join(f'"{data[column]}"' for column in headers)
        csv += row + "\n"

    with open(f"{table}.csv", 'w') as file:
        file.write(csv)