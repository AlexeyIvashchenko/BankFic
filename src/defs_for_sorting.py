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
    needed_keys = ["date", "description", "from", "to", "operationAmount"]
    transfer_info = {key: transfers_full_info[key] for key in needed_keys}
    right_date = change_the_date(transfer_info)
    right_frome = get_the_right_from(right_date)
    right_to = get_the_right_to(right_frome)
    return right_to


def get_the_right_from(transfer_info):
    from_point = transfer_info['from']
    right_from_point = ''
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for letter in from_point:
        while letter != numbers:
            right_from_point += letter
            continue
        else:
            for i in range(4):
                right_from_point += letter
            right_from_point += ' '
        for i in range(4):
            right_from_point += '*'
        right_from_point += ' '
        for i in range(4):
            right_from_point += '*'
        right_from_point += ' '
        for i in range(4):
            right_from_point += letter
    transfer_info['from'] = right_from_point
    return transfer_info


def get_the_right_to(transfer_info):
    to_point = transfer_info['to']
    right_to_point = ''
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for letter in to_point:
        while letter != numbers:
            right_to_point += letter
            continue
        else:
            for i in range(2):
                right_to_point += '*'
        for i in range(4):
            right_to_point += letter
    transfer_info['to'] = right_to_point
    return transfer_info
