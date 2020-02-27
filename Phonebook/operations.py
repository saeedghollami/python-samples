import sqlite3



def create_connection(db_file="phonebook.db"):
    """ Create a connection to db file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn


def create_table(conn):
    sql = """
        CREATE TABLE IF NOT EXISTS contact(
            id INTEGER PRIMARY KEY,
            first TEXT NOT NULL,
            last TEXT,
            phone TEXT NOT NULL
        )
    """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        return True
    except sqlite3.Error as e:
        print(e)


def create_contact(conn, contact):
    """ get a contact: tuple a insert it to contact table

    """
    sql = """
        INSERT INTO contact(first, last, phone)
        VALUES (?, ?, ?);
    """
    cur = conn.cursor()
    cur.execute(sql, contact)
    conn.commit()
    return cur.lastrowid


def read_contacts(conn):
    sql = """ SELECT * FROM contact; """

    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()


def update_contact(conn, new_contact):
    sql = """
        UPDATE contact
        SET first = ?,
            last = ?,
            phone = ?
        WHERE id = ?
    """
    cur = conn.cursor()
    cur.execute(sql, new_contact)
    return True





if __name__ == "__main__":
    conn = create_connection("phonebook.db")

    # create contact table if not exists
    create_table(conn)

    # a person contact
    c = ('Joe', "Doe", "123")
    # result = create_contact(conn, c)
    # print(result)

    print("before update")
    contacts = read_contacts(conn)
    print(contacts)

    new_c = ('Jack', 'Doe', '234', 2)
    r = update_contact(conn, new_c)
    print(r)

    print("After update")
    contacts = read_contacts(conn)
    print(contacts)
