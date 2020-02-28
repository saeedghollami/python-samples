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
	return Select(c for c in Contact)[:]


@db_session
def find_contact():
	pass


@db_session
def update_contact():
	pass


@db_session
def delete_contact():
	pass



if __name__ == "__main__":
	# create_contact('John', 'Doe', '123')

	contacts = read_contacts()
	print(dir(contacts))
	print(contacts)