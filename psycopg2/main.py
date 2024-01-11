import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS clients(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(40) NOT NULL,
            last_name VARCHAR(40) NOT NULL,
            email VARCHAR(256) UNIQUE
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS phones(
            client_id INTEGER NOT NULL REFERENCES clients(id),
            phone VARCHAR(25),
            CONSTRAINT pk PRIMARY KEY (client_id, phone)
        );
        """)
        conn.commit()  # фиксируем в БД

def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO clients(first_name, last_name, email)
        VALUES(%s, %s, %s) RETURNING id;
        """, (first_name, last_name, email))

        id_val = cur.fetchone()

        if phones is not None:
            for ph in phones:
                add_phone(conn, id_val, ph)

def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO phones(client_id, phone)
        VALUES(%s, %s);
        """, (client_id, phone))
        conn.commit()  # фиксируем в БД

def change_client(conn, client_id, first_name, last_name, email, phones=None):
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE clients SET first_name=%s, last_name=%s, email=%s 
        WHERE id=%s;
        """, (first_name, last_name, email, client_id))
        conn.commit()  # фиксируем в БД

        delete_all_phones(conn, client_id)
        
        if phones is not None:
            for ph in phones:
                add_phone(conn, client_id, ph)
        conn.commit()  # фиксируем в БД

def delete_all_phones(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM phones WHERE client_id=%s;
        """, (client_id, ))
        conn.commit()  # фиксируем в БД

def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM phones WHERE client_id=%s AND phone=%s;
        """, (client_id, phone))
        conn.commit()  # фиксируем в БД

def delete_client(conn, client_id):
    with conn.cursor() as cur:
        delete_all_phones(conn, client_id)

        cur.execute("""
        DELETE FROM clients WHERE id=%s;
        """, (client_id, ))
        conn.commit()  # фиксируем в БД

def find_client(conn, first_name, last_name, email, phone=None):
    with conn.cursor() as cur:
        cur.execute("""
        SELECT * 
        FROM clients c 
        LEFT JOIN phones ph 
        ON c.id = ph.client_id 
        WHERE c.first_name=%s AND c.last_name=%s 
            AND c.email=%s AND ph.phone=%s;
        """, (first_name, last_name, email, phone))
        print(cur.fetchall())


with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
    create_db(conn)
    add_client(conn, 'Anna', 'Gubanova', 'gubanova.93@mail.ru', None)
    add_client(conn, 'Natalia', 'Gubanova', 'gubanova.71@mail.ru', ['+79161214934'])
    add_phone(conn, 1, '+79779636088')
    change_client(conn, 1, 'Anna', 'Gubanova', 'gubanova.93@mail.ru',
                  phones=['+79161214914', '+79857606565', '+79779636088'])
    delete_phone(conn, 1, '+79779636088')
    delete_client(conn, 2)
    find_client(conn, 'Anna', 'Gubanova', 'gubanova.93@mail.ru', '+79161214914')

conn.close()