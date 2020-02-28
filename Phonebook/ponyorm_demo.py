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
def update_contact():
	pass


@db_session
def delete_contact():
	pass



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
	x = find_contact(10)
	# x.exists()
	print(x)
