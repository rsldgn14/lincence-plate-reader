import sqlite3


def get_user_information_by_plate(plate):
    if not isinstance(plate, str):
        raise TypeError("Plate parametresi string olmalıdır.")
    conn = sqlite3.connect('db/customers.sqlite')
    customers = conn.execute("SELECT * FROM customers WHERE LicencePlate= ?", (plate.strip(),))
    result = customers.fetchall()
    conn.close()
    return result


def add_user_information(name, surname, plate, block):
    conn = sqlite3.connect('db/customers.sqlite')

    conn.execute("INSERT INTO customers (Name, Surname, LicencePlate,Block) VALUES (?, ?, ?, ?)",
                 (name, surname, plate, block))

    print("{} {} {} {} added to database".format(name, surname, plate, block))
    conn.commit()
    conn.close()


def delete_user_information(id):
    conn = sqlite3.connect('db/customers.sqlite')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM customers WHERE id = ?", (id,))

    print("ID {} user deleted".format(id))

    conn.commit()
    conn.close()


def update_user_information(id, new_name, new_surname, new_plate, new_block):
    conn = sqlite3.connect('db/customers.sqlite')
    cursor = conn.cursor()

    cursor.execute("UPDATE customers SET Name = ?, Surname = ?, LicencePlate = ?, Block = ? WHERE id = ?",
                   (new_name, new_surname, new_plate, new_block, id,))
    conn.commit()

    print("{} row(s) updated".format(cursor.rowcount))

    conn.close()


def get_all_users():
    conn = sqlite3.connect('db/customers.sqlite')

    cursor = conn.execute("SELECT * FROM customers")

    result = cursor.fetchall()

    return result
