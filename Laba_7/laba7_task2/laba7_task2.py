# Приводим файл к читабельному виду
import json

input_file_path = 'json files/ex2.json'
output_file_path = 'json files/formatted_ex2.json'

with open(input_file_path) as json_file:
    data = json.load(json_file)

with open(output_file_path, 'w') as formatted_json_file:
    json.dump(data, formatted_json_file, indent=4)

print(f"Файл отформатирован и сохранен как {output_file_path}.")


# Извлечение данных в словарь
def extract_user_data(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
        user_dict = {user['name']: user['phoneNumber'] for user in data}
    return user_dict

file_path = 'json files/formatted_ex2.json'
user_data = extract_user_data(file_path)

for name, phone in user_data.items():
    print(f"Имя: {name}, Телефон: {phone}")