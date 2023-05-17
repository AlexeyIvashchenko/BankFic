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
    transfer_info = {}
    for key in needed_keys:
        if key not in transfers_full_info:
            continue
        else:
            transfer_info[key] = transfers_full_info[key]
    if 'date' in transfer_info:
        right_date = change_the_date(transfer_info)
        if 'from' in transfer_info:
            right_from = get_the_right_from(right_date)
            if 'to' in transfer_info:
                right_to = get_the_right_to(right_from)
                return right_to

    if 'from' in transfer_info:
        right_from = get_the_right_from(transfer_info)
        if 'to' in transfer_info:
            right_to = get_the_right_to(transfer_info)
            return right_to

    if 'to' in transfer_info:
        right_to = get_the_right_to(transfer_info)
        return right_to
    else:
        return transfer_info


def get_the_right_from(transfer_info):
    from_point = transfer_info['from']
    right_from_point = ''
    last_four = from_point[-4:]
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for letter in from_point:
        if letter not in numbers:
            right_from_point += letter
            continue
        else:
            right_from_point += letter
            right_from_point += letter
            right_from_point += '** **** '
            right_from_point += last_four
            break
    transfer_info['from'] = right_from_point
    return transfer_info


def get_the_right_to(transfer_info):
    to_point = transfer_info['to']
    right_to_point = ''
    last_four = to_point[-4:]
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for letter in to_point:
        if letter not in numbers:
            right_to_point += letter
            continue
        else:
            right_to_point += '**'
            right_to_point += last_four
            break
    transfer_info['to'] = right_to_point
    return transfer_info
