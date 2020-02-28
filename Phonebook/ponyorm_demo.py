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


if __name__ == "__main__":
	create_contact('John', 'Doe', '123')
