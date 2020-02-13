import pickle



contacts = []


# save contacts in a pickle file
def save_contacts(filename='contacts.pickle'):
    with open(filename, 'wb') as contact_db:
        # write contacts using pickle 
        pickle.dump(contacts, contact_db)


# read contacts from pickle file
def load_contacts(filename='contacts.pickle'):
    global contacts
    with open(filename, 'rb') as contact_db:
        contacts = pickle.load(contact_db)


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


# get user infromation and create a contact with them
def create_contact(info):
    first, last, phone = info
    contact = {'id': len(contacts)+1,  'first_name': first,
               'last_name': last, 'phone_number': phone}
    contacts.append(contact)
    return True


# get id of the contact and update it with new info
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


# get id of contact if the contact exist, delete
def delete_contact(idx):
    contact = find_contact(idx)
    if contact:
        index = contacts.index(contact)
        del contacts[index]
        return True
    else:
        return False


# get id of the contact and return contact if exist, else return False
def find_contact(idx):
    for contact in contacts:
        cid, *_ = contact.values()
        if int(cid) == idx:
            return contact
    return False


if __name__ == "__main__":
    pass
