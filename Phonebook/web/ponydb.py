from pony.orm import *
db = Database()



class Contact(db.Entity):
    first = Required(str)
    email = Required(str)
    phone = Required(str)


db.bind(provider='sqlite', filename='phonebook.sqlite3', create_db=True)
db.generate_mapping(create_tables=True)

# add new contact
@db_session
def create_contact(first, email, phone):
    c = Contact(first=first, email=email, phone=phone)


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
def update_contact(data):
	contact = Contact.get(id=data.get('cid'))
	if contact is not None:
		contact.first = data.get('first')
		contact.last = data.get('email')
		contact.phone = data.get('phone')
		return True
	return False


@db_session
def delete_contact(cid):
	contact = Contact.get(id=cid)
	if contact is not None:
		contact.delete()
		return True
	return False


	
