from datetime import datetime


def take_the_date(transfer_info):
    return transfer_info['date']


def give_the_right_date(transfer_info):
    date = take_the_date(transfer_info)
    reversed_date = ''
    for letter in date:
        if letter != 'T':
            reversed_date += letter
        else:
            break
    date = datetime.strptime(reversed_date, '%Y-%m-%d').strftime('%d-%m-%Y')
    return date


def change_the_date(transfer_info):
    transfer_info['date'] = give_the_right_date(transfer_info)
    return transfer_info


def get_the_transfer_info(transfers_full_info):
    needed_keys = ["date", "description", "from", "to", "amount", "currency"]
    transfer_info = {key: transfers_full_info[key] for key in needed_keys}
    right_info = change_the_date(transfer_info)
    return right_info
