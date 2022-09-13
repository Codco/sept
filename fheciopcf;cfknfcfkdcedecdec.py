import psycopg2


def create_db_client(conn):
    cur.execute(""" 
     CREATE TABLE IF NOT EXISTS client
        (id SERIAL PRIMARY KEY,
         first_name TEXT NOT NULL,
         last_name TEXT NOT NULL,
         email TEXT NOT NULL,
     );
     """)
    conn.commit()


def create_db_phones(conn):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phones
       (id SERIAL PRIMARY KEY  RELATED TO client id,
       phones TUPLE
    );
    """)
    conn.commit()


def add_client(conn, first_name, last_name, email):
    cur.execute("""            
    INSERT INTO client(first_name) VALUES('first_name');
    INSERT INTO client(last_name) VALUES('last_name')
    INSERT INTO client(email) VALUES('email');
    """, (first_name, last_name, email,))
    conn.commit()


def add_phone(conn, phones_id, phones):
    cur.execute("""
        INSERT INTO phones(phones) VALUES('phones');
        """, (phones_id, phones))
    print(cur.fetchone())


def change_client_name(conn, client_id, first_name):
    cur.execute("""
           UPDATE client SET first_name=%s, last_name=%s, email=%s WHERE id=%s;
           """, (client_id, first_name))


def change_client_surname(conn, client_id, last_name):
    cur.execute("""
           UPDATE client SET first_name=%s, last_name=%s, email=%s WHERE id=%s;
           """, (client_id, last_name))


def change_client_email(conn, client_id, email):
    cur.execute("""
        UPDATE client SET first_name=%s, last_name=%s, email=%s WHERE id=%s;
        """, (client_id, email))


def change_client_name_surname(conn, client_id, first_name, last_name):
    cur.execute("""
        UPDATE client SET first_name=%s, last_name=%s, email=%s WHERE id=%s;
        """, (client_id, email, first_name, last_name))


def change_client_name_email(conn, client_id, first_name, email):
    cur.execute("""
        UPDATE client SET first_name=%s, last_name=%s, email=%s WHERE id=%s;
        """, (client_id, first_name, email))


def change_client_surname_email(conn, client_id, last_name, email):
    cur.execute("""
        UPDATE client SET first_name=%s, last_name=%s, email=%s WHERE id=%s;
        """, (client_id, last_name, email))


def change_client(conn, client_id, first_name, last_name, email):
    cur.execute("""
           UPDATE client SET first_name=%s, last_name=%s, email=%s WHERE id=%s;
           """, (client_id, first_name, last_name, email))


def delete_client(conn, client_id):
    cur.execute("""
        DELETE FROM client WHERE id=%s;
        """, (client_id,))
    print(cur.fetchall())


def delete_phone(conn, phones_id, phones):
    cur.execute("""
        DELETE FROM phones WHERE id=%s;
        """, (phones, phones_id))
    print(cur.fetchall())


def first_name_find(conn, first_name):
        cur.execute("""
            SELECT id FROM client WHERE last_name=%s;
            """, (client_id, first_name,))
        print(cur.fetchone())


def last_name_find(conn, last_name):
        cur.execute("""
            SELECT id FROM client WHERE last_name=%s;
            """, ( client_id, last_name,))
        print(cur.fetchone())


def email_find(conn, email):
        cur.execute("""
            SELECT id FROM client WHERE email=%s;
            """, ( client_id, email,))
        print(cur.fetchone())


def first_and_last_name_find(conn, first_name, last_name):
        cur.execute("""
            SELECT id FROM client WHERE first_name=%s, last_name=%s;
            """, ( client_id, first_name, last_name))
        print(cur.fetchone())


def first_name_email_find(conn, first_name, email):
        cur.execute("""
            SELECT id FROM client WHERE first_name=%s, email=%s;
            """, ( client_id, first_name, email,))
        print(cur.fetchone())


def last_name_email_find(conn, last_name, email):
        cur.execute("""
            SELECT id FROM client WHERE last_name=%s, email=%s;
            """, ( client_id, last_name, email,))
        print(cur.fetchone())


def first_last_name_email_find(conn, first_name, last_name, email):
        cur.execute("""
                SELECT id FROM client WHERE first_name=%s, last_name=%s, email=%s;
                """, ( first_name, last_name, email,))
        print(cur.fetchone())


if __name__ == '--main---':
    with psycopg2.connect(database="postgres", user="postgres", password="password") as conn:
        with conn.cursor() as cur:
            create_db_client(conn)

            create_db_phones(conn)

            add_client(conn, first_name='Vasya', last_name='Pupkin', email='asd@yandex.ru')

            add_client(conn, first_name='Vaya', last_name='Pupin', email='ad@yandex.ru')

            add_phone(conn, phones=(22 - 33 - 44), phones_id=1)

            first_name_find(conn, first_name='Vasya')

            last_name_find(conn, last_name='Pupin')

            email_find(conn, email='ad@yandex.ru')

            first_and_last_name_find(conn, first_name='Vasya', last_name='Pupin')

            last_name_email_find(conn, last_name='Pupin', email='ad@yandex.ru')

            first_name_email_find(conn, first_name='Vasya', email='ad@yandex.ru')

            first_last_name_email_find(conn, first_name='Vasya', last_name='Pupin', email='ad@yandex.ru')

            change_client_name(conn, client_id='1', first_name='aaa')

            change_client_surname(conn, client_id='1', last_name='AAA')

            change_client_email(conn, client_id='1', email='a')

            change_client_name_surname(conn, client_id='1', first_name='BBB', last_name='bbb')

            change_client_name_email(conn, client_id='1', first_name='ccc', email='CCC')

            change_client_surname_email(conn, client_id='1', last_name='DDD', email='ddd')

            change_client(conn, client_id='1', first_name='e', last_name='EEE', email='eee')

            delete_phone(conn, phones=(12 - 12 - 12), phones_id=1)

            delete_client(conn, client_id=1)

conn.close()
