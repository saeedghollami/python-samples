import os


contacts = []

menu_items = """
1. Create contact
2. Read contacts
3. Update contact
4. Delete contact
5. Exit
"""

while True:
    os.system('clear')
    print(menu_items)
    respons = input('\n> ')

    # create a contact
    if respons == '1':
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        phone_number = input('Phone Number: ')
        contact = {'id': len(contacts)+1,  'first_name': first_name,
                   'last_name': last_name, 'phone_number': phone_number}
        contacts.append(contact)
        print('Added.')

    # display all contacts
    elif respons == '2':
        width = 20
        align = '<'
        header = (f'{"ID": {align}{width}}'
                  f'{"First Name": {align}{width}}'
                  f'{"Last Name": {align}{width}}'
                  f'{"Phone Number": {align}{width}}')
        print(header)
        print('-'*len(header))
        for contact in contacts:
            cid, first, last, phone = contact.values()
            s = (f'{cid:{align}{width}}'
                 f'{first:{align}{width}}'
                 f'{last:{align}{width}}'
                 f'{phone:{align}{width}}')
            print(s)

    # Update a contact
    elif respons == '3':
        idx = int(input('Contact ID: '))
        for contact in contacts.copy():
            cid, *_ = contact.values()
            if cid == idx:
                # get new info for the contact
                first = input('First Name: ')
                last = input('Last Name: ')
                phone = input('Phone Number:')
                # make a new contact
                contact['first_name'] = first
                contact['last_name'] = last
                contact['phone_number'] = phone
                print('Updated.')
                break  # after update the contact no need for iteration
        else:
            print('Contact not found!')

    # delete a contact
    elif respons == '4':
        idx = int(input('Contact ID: '))
        
        for contact in contacts.copy():
            cid, *_ = contact.values()
            if cid == idx:
                index = contacts.index(contact)
                del contacts[index]
                print('Removed.')
                break  # no need for iteration after removing the contact.
        else:  # no break
            print('Contact not found!')

    # exit from menu
    elif respons == '5':
        break
    else:
        print('Wrong choice')
        continue  # skip blowe codes and back to while
    input('To see menu press ENTER key...')