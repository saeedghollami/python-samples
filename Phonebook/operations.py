import console_ui as ui

contacts = []


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
        first, last, phone = ui.get_info()
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
        if cid == idx:
            return contact
    return False
