from pony.orm import *





db = Database()

class Contact(db.Entity):
    first = Required(str)
    last = Required(str)
    phone = Required(str)

db.bind(provider='sqlite', filename='phonebook_pony.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

