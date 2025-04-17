import sqlite3
from pprint import pprint
from tabulate import tabulate

DB_FILE = "badbank.db"

con = sqlite3.connect(DB_FILE)
cur = con.cursor()


def write_example_data():
    """
    Insert example data into tables created by db_creation.py
    """

    cur.executemany("""INSERT OR REPLACE INTO accounts
        (iban, balance_cents)
        VALUES (?, ?)
        """,
        [('DE00 1234 1234 1234 1234 01', 0),
         ('DE00 1234 1234 1234 1234 02', 0),
         ('DE00 1234 1234 1234 1234 03', 0)]
    )
    ## Warning: this statement is not idempotent
    #cur.executemany("""INSERT INTO account_changes
    #    (changed_at, iban, iban_other, flag, amount_cents, purpose, recipient)
    #    VALUES (datetime('now'), ?, ?, ?, ?, ?, ?)
    #    """,
    #    [('DE00 1234 1234 1234 1234 01', 'DE00 1234 1234 1234 1234 02', '-', 1337, 'donation for your great software', 'my favourite foss developer'),
    #     ('DE00 1234 1234 1234 1234 02', 'DE00 1234 1234 1234 1234 01', '+', 1337, 'donation for your great software', 'my favourite foss developer')]
    #)
    con.commit()


def print_tables():
    for table in ['accounts', 'account_changes']:
        print(f"== {table} ==\n")
    
        res = cur.execute(f"PRAGMA table_info({table})")
        columns = [row[1] for row in res.fetchall()]
    
        cur.execute(f"SELECT * from {table}")
    
        print(tabulate(cur.fetchall(), headers=columns, tablefmt="grid"))
        print()


if __name__ == "__main__":
    write_example_data()
    print_tables()
