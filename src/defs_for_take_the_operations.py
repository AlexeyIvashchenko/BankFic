from datetime import datetime


def sort_the_transfers(transfers_info):
    sorted_lst = sorted(
        (item for item in transfers_info if 'date' in item),
        key=lambda x: datetime.strptime(x['date'], '%d-%m-%Y'),
        reverse=True
    )
    return sorted_lst
