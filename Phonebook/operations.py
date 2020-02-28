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
    try:
        cur = conn.cursor()
        cur.execute(sql, contact)
        conn.commit()
        return cur.lastrowid
    except sqlite3.Error as e:
        return False


def read_contacts(conn):
    sql = """ SELECT * FROM contact; """

    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()


def update_contact(conn, cid, new_contact):
    sql = """
        UPDATE contact
        SET first = ?,
            last = ?,
            phone = ?
        WHERE id = ?
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, new_contact+(cid,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        return False  # contact not found!

def find_contact(conn, cid):
    """ Return contact if found
    """

    sql = """
        SELECT first, last, phone
        FROM contact
        WHERE id = ?;
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, str(cid))
        return cur.fetchone()
    except sqlite3.Error as e:
        return None  # contact not found!


def delete_contact(conn, cid):
    sql = """
        DELETE FROM contact
        WHERE id = ?;
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, str(cid))
        conn.commit()
        return True
    except sqlite3.Error as e:
        return False  # contact not found!


if __name__ == "__main__":
    conn = create_connection("phonebook.db")

    # create contact table if not exists
    # create_table(conn)

    # a person contact
    # c = ('Joe', "Doe", "123")
    # result = create_contact(conn, c)
    # print(result)

    # print("before update")
    # contacts = read_contacts(conn)
    # print(contacts)

    # new_c = ('Jack', 'Doe', '234', 2)
    # r = update_contact(conn, new_c)
    # print(r)

    # print("After update")
    # contacts = read_contacts(conn)
    # print(contacts)

    # find a contact by id
    # found = find_contact(1)
    # if found is not None:
    #     print('Found')
    #     # if found going to delete
    #     d = delete_contact(conn, 50)
    #     if d:
    #         print('deleted!', d)
    #     else:
    #         print('not delete somthing happend', d)
    # else:
    #     print('Not found')

    # # 
    
