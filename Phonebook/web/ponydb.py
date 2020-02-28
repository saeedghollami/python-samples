from pony.orm import *



db = Database()



class Contact(db.Entity):
    first = Required(str)
    last = Required(str)
    phone = Required(str)


db.bind(provider='sqlite', filename='phonebook.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

# add new contact
@db_session
def create_contact(first, last, phone):
    c = Contact(first=first, last=last, phone=phone)


@db_session
def read_contacts():
	return select(c for c in Contact)[:]


@db_session
def find_contact(cid):
	query = select(contact for contact in Contact if contact.id == cid)
	
	if query.exists():
		return query.fetch()
	else:
		return False


@db_session
def update_contact(cid, new_contact):
	contact = Contact.get(id=cid)
	if contact is not None:
		contact.first = new_contact.get('first')
		contact.last = new_contact.get('last')
		contact.phone = new_contact.get('phone')
		return True
	return False


@db_session
def delete_contact(cid):
	contact = Contact.get(id=cid)
	if contact is not None:
		contact.delete()
		return True
	return False


if __name__ == "__main__":
	create_contact(first='John', last='Doe', phone='1223')
	create_contact(first='Jim', last='Harper', phone='434')
	create_contact(first='Tom', last='Kroze', phone='324')

	
