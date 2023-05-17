import json
from defs_for_sorting import get_the_transfer_info
from defs_for_take_the_operations import sort_the_transfers

with open('D:\Python Projects\BankFic\operations.json') as file:
    transfers = json.load(file)

transfers_right_info = []
for transfer in transfers:
    transfers_right_info = get_the_transfer_info(transfer)

sorted_transfers_right_info = sort_the_transfers(transfers_right_info)

for transfer in range(5):
    print(f"""{sorted_transfers_right_info['date']} {sorted_transfers_right_info['description']}
    {sorted_transfers_right_info['from']} '->' {sorted_transfers_right_info['to']}
    {sorted_transfers_right_info['operationAmount']['amount']} {sorted_transfers_right_info['operationAmount']['currency']['name']}
""")
