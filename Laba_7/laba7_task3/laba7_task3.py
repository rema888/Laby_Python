import json

input_file_path = 'json files/ex3.json'
output_file_path = 'json files/updated_ex3.json'

with open(input_file_path) as json_file:
    data = json.load(json_file)

new_invoice = {
    "id": 3,
    "total": 333.00,
    "items": [
        {
            "name": "item 4",
            "quantity": 3,
            "price": 111.00
        }
    ]
}

# Добавление нового объекта в массив invoices
data['invoices'].append(new_invoice)

with open(output_file_path, 'w') as updated_json_file:
    json.dump(data, updated_json_file, indent=4)

print(f"Новый объект добавлен и сохранен как {output_file_path}.")