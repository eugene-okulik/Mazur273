import requests


def get_all_obj():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    print(f'статус-код: {response.status_code}')
    assert response.status_code == 200, 'Что-то пошло не так'
    print(f'тип данных: {type(response.json())}')


get_all_obj()


def one_obj():
    response = requests.get('http://objapi.course.qa-practice.com/object/1')
    print(f'статус-код получения объекта: {response.status_code}')


one_obj()


def new_obj():
    name = 'Mikhail'
    data = {'name': name,
            'data': {
                'key1': 'value1',
                'key2': 'value2',
            }}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=data
    )
    assert response.status_code == 200, 'Status code is incorrect'
    # в доках не сказано какой код ждать при успехе, запускаем и узнаем код, потом подставляем
    post_id = response.json()['id']
    print(f'новый объект создан, id {post_id}')
    return post_id


new_obj()


def put_obj():
    post_id = new_obj()  # для нового теста создаем новый объект, вдруг старый удалили
    name = "Mikhail_UPD"
    data = {'name': name,
            'data': {
                'key1_upd': 'value1_upd',
                'key2_upd': 'value2_upd',
            }}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=data
    )
    assert response.status_code == 200, 'Объект не изменен'
    print(response.status_code)


put_obj()


def patch_obj():
    post_id = new_obj()
    name = "Mikhail_PATCH"
    data = {'name': name,
            'data': {
                'key1_upd': 'value1_upd',
                'key2_upd': 'value2_upd',
            }}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=data
    )
    assert response.status_code == 200, 'Объект не изменен'
    print(response.status_code)


patch_obj()


def delete_obj():
    post_id = new_obj()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    assert response.status_code == 200
    print(f'объект с id {post_id} удален')


delete_obj()


def interesno():
    response = requests.options('http://objapi.course.qa-practice.com/object/')
    print(response.status_code)
    print(response.headers)
    print(response.text)
# не получилось


interesno()
