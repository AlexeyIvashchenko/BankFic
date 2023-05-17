def get_transfer(list_of_transfers, index):
    return list_of_transfers[index]


def sort_the_transfers(transfers_info):
    needed_key = ['date']
    date_info = {key: transfers_info[key] for key in needed_key}
    sorted_transfers = dict(sorted(date_info))
    return sorted_transfers
