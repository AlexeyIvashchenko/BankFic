import json
import os
from defs_for_sorting import get_the_transfer_info
from defs_for_take_the_operations import sort_the_transfers

# Получение абсолютного пути к файлу operations.json
file_path = os.path.join(os.getcwd(), 'operations.json')

# распаковал json в список для удобства
with open(file_path) as file:
    transfers = json.load(file)

# создал словарь только с нужной информацией
transfers_right_info = []
for transfer in transfers:
    transfers_info = get_the_transfer_info(transfer)
    transfers_right_info.append(transfers_info)

# сортировка по убыванию даты
sorted_transfers_right_info = sort_the_transfers(transfers_right_info)

# вывод первых 5 позиций
for transfer in range(5):
    transfer_info = sorted_transfers_right_info[transfer]
    date = transfer_info.get('date', '-')
    description = transfer_info.get('description', '-')
    _from = transfer_info.get('from', '-')
    to = transfer_info.get('to', '-')
    amount = transfer_info.get('operationAmount', {}).get('amount', '-')
    currency_name = transfer_info.get('operationAmount', {}).get('currency', {}).get('name', '-')

    print(f"{date} {description}\n{_from} -> {to}\n{amount} {currency_name}\n")
