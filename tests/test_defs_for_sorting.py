import sys

sys.path.append('../src')

from defs_for_sorting import (
    take_the_date,
    give_the_right_date,
    change_the_date,
    get_the_right_from,
    get_the_right_to,
    get_the_transfer_info
)


def test_take_the_date():
    transfer_info = {
        'date': '2023-05-17T12:34:56.789'
    }
    assert take_the_date(transfer_info) == '2023-05-17T12:34:56.789'


def test_give_the_right_date():
    transfer_info = {
        'date': '2023-05-17T12:34:56.789'
    }
    assert give_the_right_date(transfer_info) == '17-05-2023'


def test_change_the_date():
    transfer_info = {
        'date': '2023-05-17T12:34:56.789'
    }
    expected_result = {
        'date': '17-05-2023'
    }
    assert change_the_date(transfer_info) == expected_result


def test_get_the_right_from():
    transfer_info = {
        'from': 'Maestro 1234567890123456'
    }
    expected_result = {
        'from': 'Maestro 11** **** 3456'
    }
    assert get_the_right_from(transfer_info) == expected_result


def test_get_the_right_to():
    transfer_info = {
        'to': 'Счет 1234567890123456'
    }
    expected_result = {
        'to': 'Счет **3456'
    }
    assert get_the_right_to(transfer_info) == expected_result


def test_get_the_transfer_info():
    transfers_full_info = {
        'date': '2023-05-17T12:34:56.789',
        'description': 'Transfer',
        'from': 'Maestro 1234567890123456',
        'to': 'Счет 1234567890123456',
        'operationAmount': {
            'amount': '100.00',
            'currency': {
                'name': 'USD',
                'code': 'USD'
            }
        }
    }
    expected_result = {
        'date': '17-05-2023',
        'description': 'Transfer',
        'from': 'Maestro 11** **** 3456',
        'to': 'Счет **3456',
        'operationAmount': {
            'amount': '100.00',
            'currency': {
                'name': 'USD',
                'code': 'USD'
            }
        }
    }
    assert get_the_transfer_info(transfers_full_info) == expected_result
