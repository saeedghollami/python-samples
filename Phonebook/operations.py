import csv


contacts = []


def save_contacts(filename='contacts.csv'):
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = ['id', 'first_name', 'last_name', 'phone_number']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # write fieldnames as the header
        writer.writeheader()
        # write each dict(a contact) as row in the csv file
        writer.writerows(contacts)


def load_contacts(filename='contacts.csv'):
    # read contacts
    with open(filename, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        # store content of the first row in header and go to next row
        header = next(reader)

        for row in reader:
            contacts.append(dict(zip(header, row)))


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
