# store all contacts here
contacts = []
menu_items = """
1. Create contact
2. Read contacts
3. Update contact
4. Delete contact
5. Exit
"""

while True:
    print(menu_items)
    respons = input('\n> ')
    
    # create a contact
    if respons == '1':
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        phone_number = input('Phone Number: ')
        contact = f'{first_name}:{last_name}:{phone_number}\n'
        contacts.append(contact)

    # display all contacts
    elif respons == '2':
        width = 20
        align = '<'
        header = (f'{"First Name": {align}{width}}'
        f'{"Last Name": {align}{width}}'
        f'{"Phone Number": {align}{width}}')
        print(header)
        print('-'*50)
        for contact in contacts:
            first, last, phone = contact.split(':')
            s = (f'{first.strip(): {align}{width}}'
            f'{last.strip(): {align}{width}}'
            f'{phone.strip(): {align}{width}}')
            print(s)

    # Update a contact 
    elif respons == '3':
        phone_number = input('Enter contact phone number to find it: ')
        for contact in contacts.copy():
            _, _, phone = contact.split(':')
            if phone.strip() == phone_number:
                # get new info for the contact
                first = input('First Name: ')
                last = input('Last Name: ')
                phone = input('Phone Number:')
                # make a new contact
                new_contact = f'{first}:{last}:{phone}\n'
                index = contacts.index(contact)  # find index of the contact
                contacts[index] = new_contact  # update contact with new contact
                break  # after update the contact no need for iteration
        else:
            print('Contact not found!')

    # delete a contact
    elif respons == '4':
        phone_number = input('Enter contact phone number to find it: ')
        # read contacts an figuare out is there any contact with the phone_number
        for contact in contacts.copy():
            _, _, phone = contact.split(':')
            if phone.strip() == phone_number:
                contacts.remove(contact)
                print('Removed successfuly')
                break  # no need for iteration after removing the contact.
        else:  # no break
            print('Contact not found!')

    # exit from menu
    elif respons == '5':
        break
    else:
        print('Wrong choice')