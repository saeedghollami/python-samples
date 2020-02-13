
contacts = []


def save_contacts(filename='contacts.txt'):
    all_contacts = ''

    for contact in contacts:
        for _, value in contact.items():
            all_contacts += f'{value}:'
        # remove last colon from each contact
        all_contacts = all_contacts[:-1]
        # add new line to each contact
        all_contacts += '\n'
    # write all contacts in the textfile
    with open(filename, 'w') as contact_file:
        contact_file.write(all_contacts)


def load_contacts(filename='contacts.txt'):
    # read contacts
    with open(filename, 'r') as contact_file:
        all_contacts = contact_file.readlines()
    
    for contact in all_contacts:
        cid, first, last, phone = contact.split(':')
        contact_row = {'id': cid,  'first_name': first,
                        'last_name': last, 'phone_number': phone.strip()}
        # load contacts
        contacts.append(contact_row)
    print(contacts)


def get_info():
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    phone_number = input('Phone Number: ')
    return first_name, last_name, phone_number


def get_id():
    try:
        idx = int(input('Contact ID: '))
        return int(idx)
    except ValueError:
        return False


def create_contact(info):
    first, last, phone = info
    contact = {'id': len(contacts)+1,  'first_name': first,
               'last_name': last, 'phone_number': phone}
    contacts.append(contact)
    return True


def update_contact(idx):
    contact = find_contact(idx)
    if contact:
        # get new info for the contact
        first, last, phone = get_info()
        # make a new contact
        contact['first_name'] = first
        contact['last_name'] = last
        contact['phone_number'] = phone
        return True
    else:
        return False


def delete_contact(idx):
    contact = find_contact(idx)
    if contact:
        index = contacts.index(contact)
        del contacts[index]
        return True
    else:
        return False


def find_contact(idx):
    for contact in contacts:
        cid, *_ = contact.values()
        if int(cid) == idx:
            return contact
    return False


if __name__ == "__main__":
    load_contacts()
