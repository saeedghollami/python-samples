import shelve
import pickle


contacts = []


# save contacts in a shelve file
def save_contacts(filename='contacts.db'):
    with shelve.open(filename) as contact_db:
        # create a key named 'contacts' in shelve file and bind all contact to it.
        contact_db['contacts'] = contacts


# read contacts from shelv file
def load_contacts(filename='contacts.db'):
    with shelve.open(filename) as contact_db:
        for contact in contact_db['contacts']:
            contacts.append(contact)


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
    save_contacts()
    # load_contacts()
    # print(contacts)
