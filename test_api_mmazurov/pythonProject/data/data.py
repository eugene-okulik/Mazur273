TEST_DATA = [
    {'name': 'Mikhail', 'data': {'key1': 'value1'}},
    {'name': 'Olga', 'data': {'key2': 'value2'}}
]

NEGATIVE_DATA = [
    {'name': ['Mikhail'], 'data': {'key1': 'value1'}},
    {'name': {'Olga': ''}, 'data': {'key2': 'value2'}}
]

PUT_DATA = [
    {'name': 'Mikhail_UPD_by_PUT', 'data': {'key1': 'value1'}}
]

PATCH_DATA = [
    {'name': 'Mikhail_UPD_by_PATCH'}
]