import sqlite3
import db_example_data

DB_FILE = "badbank.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def get_cursor():
    con = get_connection()
    return con.cursor()


def balance(cur, iban):
    cur.execute("""SELECT balance_cents from accounts
        WHERE iban = ?
        """,
        (iban,)
    )
    return cur.fetchone()[0]


def transactions(cur, iban):
    cur.execute("""SELECT * from account_changes
        WHERE iban = ?
        """,
        (iban,)
    )
    return cur.fetchall()


def transfer(con, from_iban, to_iban, amount_cents, purpose, recipient):
    """
    transfer money

    What could possibly go wrong? ;)
    """

    assert(amount_cents > 0)
    ## TODO: maybe we also want set some limit (depending on the current balance?)

    cur = con.cursor()
    try:
        cur.execute("""UPDATE accounts
            SET balance_cents = balance_cents - ?
            WHERE iban = ?
            """,
            (amount_cents, from_iban)
        )
        if cur.rowcount == 0:
            raise ValueError(f"Update failed: No account found with IBAN: '{from_iban}'.")

        cur.execute("""UPDATE accounts
            SET balance_cents = balance_cents + ?
            WHERE iban = ?
            """,
            (amount_cents, to_iban)
        )
        if cur.rowcount == 0:
            raise ValueError(f"Update failed: No account found with IBAN: '{to_iban}'.")

        cur.executemany("""INSERT INTO account_changes
            (changed_at, iban, iban_other, flag, amount_cents, purpose, recipient)
            VALUES (datetime('now'), ?, ?, ?, ?, ?, ?)
            """,
            [(from_iban, to_iban, '-', amount_cents, purpose, recipient),
             (to_iban, from_iban, '+', amount_cents, purpose, recipient)]
        )
        con.commit()
        return True

    except Exception as e:
        con.rollback()
        print(f"Error occurred: {e}. Transaction rolled back.")
        return False


if __name__ == '__main__':
    con = get_connection()
    transfer(con, 'DE00 1234 1234 1234 1234 01', 'DE00 1234 1234 1234 1234 02', 1337, 'donation for your great software', 'my favourite foss developer')
    transfer(con, 'DE00 1234 1234 1234 1234 01', 'DE00 1234 1234 1234 1234 03', 4223, 'licence fees', 'bigcorp.com')
    db_example_data.print_tables()
