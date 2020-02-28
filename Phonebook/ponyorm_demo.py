from pony.orm import *



db = Database()



class Contact(db.Entity):
    first = Required(str)
    last = Required(str)
    phone = Required(str)


db.bind(provider='sqlite', filename='phonebook_pony.sqlite', create_db=True)
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
		del contact
		return True
	return False


if __name__ == "__main__":
	# create contacts
	# create_contact('Jeff', 'Doe', '1233')
	# create_contact('Jack', 'Doe', '23424')
	# create_contact('Jim', 'Doe', '122343')
	
	# read contacts
	# contacts = read_contacts()
	# for contact in contacts:
	# 	print(contact.first)
	# 	print(contact.last)
	# 	print(contact.phone)

	# find a contact by id
	# x = find_contact(10)
	# # x.exists()
	# print(x)
	
	# # UPDATE
	# new_contact = {'first': 'Karl', 'last': 'xy', 'phone': '123432'}
	# u = update_contact(1, new_contact)
	# if u:
	# 	print('updated')
	# else:
	# 	print('not update')

	# DELETE
	delete_contact(1)

	# 	# read contacts
	# contacts = read_contacts()
	# for contact in contacts:
	# 	print(contact.first)
	# 	print(contact.last)
	# 	print(contact.phone)
	
