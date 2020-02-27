import os
import operations as opr


class Messages:
    ok = 'Done :-)'
    err = 'Error :-('
    wrong = 'Wrong choice'
    not_found = 'Not Found :-('


BASEDIR = os.path.abspath(os.path.dirname(__file__))
DBNAME = os.path.join(BASEDIR, "phonebook.db")

# get inputs from user 
def get_info():
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    phone_number = input('Phone Number: ')
    return first_name, last_name, phone_number


# input id from user
def get_id():
    try:
        idx = int(input('Contact ID: '))
        return int(idx)
    except ValueError:
        return False


def create():
    info = get_info()
    conn = opr.create_connection()
    if opr.create_contact(conn, info):
        print(messages.get('ok'))
    else:
        print(messages.get('err'))


def display_contacts():
    width = 20
    align = '<'
    header = (f'{"ID": {align}{width-10}}'
              f'{"First Name": {align}{width}}'
              f'{"Last Name": {align}{width}}'
              f'{"Phone Number": {align}{width}}')
    print(header)
    print('-'*len(header))
    for contact in opr.contacts:
        cid, first, last, phone = contact.values()
        s = (f'{cid:{align}{width-10}}'
             f'{first.title():{align}{width}}'
             f'{last.title():{align}{width}}'
             f'{phone:{align}{width}}')
        print(s)


def updaet():
    idx = opr.get_id()
    result = messages.get('ok') if opr.update_contact(
        idx) else messages.get('err')
    print(result)


def delete():
    idx = opr.get_id()
    result = messages.get('ok') if opr.delete_contact(
        idx) else messages.get('err')
    print(result)


def find():
    idx = opr.get_id()
    contact = opr.find_contact(idx)
    if contact:
        print('First Name:', contact.get('first_name'))
        print('Last Number:', contact.get('last_name'))
        print('Phone Number:', contact.get('phone_number'))
    else:
        print(messages.get('err'))


def exit_app():
    opr.save_contacts(DBNAME)
    print('See you later.')
    exit()


def menu():
    menu_items = (
        '1. Create contact\n'
        '2. Read contacts\n'
        '3. Update contact\n'
        '4. Delete contact\n'
        '5. Find contact\n'
        'q. Exit\n'
    )
    actions = {
        '1': create,
        '2': display_contacts,
        '3': updaet,
        '4': delete,
        '5': find,
        'q': exit_app,
    }


    while True:
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print(menu_items)
        respond = input('> ')

        if actions.get(respond) is not None:
            actions.get(respond)()  # run the action if exist
        else:
            print(messages.get('wrong'))

        input('\nTo see menu press ENTER key...')


if __name__ == '__main__':
    menu()
