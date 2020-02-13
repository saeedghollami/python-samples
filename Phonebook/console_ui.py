import os
import operations as opr


messages = {'ok': 'Done :-)',
            'err': 'Error :-(',
            'wrong': 'Wrong choice',
            'nf': 'Not Found :-('
            }


def get_id():
    try:
        idx = int(input('Contact ID: '))
        return int(idx)
    except ValueError:
        return False


def get_info():
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    phone_number = input('Phone Number: ')
    return first_name, last_name, phone_number


def create_ui():
    info = get_info()
    result = messages.get('ok') if opr.create_contact(
        info) else messages.get('err')
    print(result)


def display_contacts():
    width = 20
    align = '<'
    header = (f'{"ID": {align}{width}}'
              f'{"First Name": {align}{width}}'
              f'{"Last Name": {align}{width}}'
              f'{"Phone Number": {align}{width}}')
    print(header)
    print('-'*len(header))
    for contact in opr.contacts:
        cid, first, last, phone = contact.values()
        s = (f'{cid:{align}{width}}'
             f'{first:{align}{width}}'
             f'{last:{align}{width}}'
             f'{phone:{align}{width}}')
        print(s)


def updaet_ui():
    idx = get_id()
    result = messages.get('ok') if opr.update_contact(
        idx) else messages.get('err')
    print(result)


def delete_ui():
    idx = get_id()
    result = messages.get('ok') if opr.delete_contact(
        idx) else messages.get('err')
    print(result)


def find_ui():
    idx = get_id()
    contact = opr.find_contact(idx)
    if contact:
        print('First Name:', contact.get('first_name'))
        print('Last Number:', contact.get('last_name'))
        print('Phone Number:', contact.get('phone_number'))
    else:
        print(messages.get('err'))


def menu():
    menu_items = (
        '1. Create contact\n'
        '2. Read contacts\n'
        '3. Update contact\n'
        '4. Delete contact\n'
        '5. Find contact\n'
        '6. Exit\n'
    )
    actions = {
        '1': create_ui,
        '2': display_contacts,
        '3': updaet_ui,
        '4': delete_ui,
        '5': find_ui,
        '6': exit
    }
    while True:
        os.system('clear')
        print(menu_items)
        respond = input('\n> ')

        if actions.get(respond) is not None:
            actions.get(respond)()  # run the action if exist
        else:
            print(messages.get('wrong'))

        input('\nTo see menu press ENTER key...')


if __name__ == '__main__':
    menu()
