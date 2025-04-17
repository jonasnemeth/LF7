import sqlite3
from pprint import pprint
import re

DB_FILE = "badbank.db"

con = sqlite3.connect(DB_FILE)
cur = con.cursor()


## Create tables

print("This script creates the required db tables.")
print("Existing tables are not changed.")
print("WARNING: schema changes are not applied!")
## For now no migration script exists. Please delete the old db when needed
print()

cur.execute("""CREATE TABLE IF NOT EXISTS accounts ( 
	iban TEXT NOT NULL PRIMARY KEY,
	balance_cents INTEGER NOT NULL DEFAULT 0
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS account_changes (
	change_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	changed_at TEXT NOT NULL, 
    iban TEXT NOT NULL, 
    iban_other TEXT NOT NULL, 
	flag TEXT NOT NULL, 
	amount_cents INTEGER NOT NULL, 
	purpose TEXT,
    recipient TEXT
);
""")


## List tables

res = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [row[0] for row in res.fetchall()]
print("The database contains the following tables:")
pprint(tables)
print()

for table in tables:
    ## PRAGMA doesn't allow parameterized queries.
    ## The following statement would be vulnerable against injections!
    ## We better ensure the variable contains only a trustworthy string
    pattern_allowed_tablenames = r'^[a-z_]+$'
    assert(re.match(pattern_allowed_tablenames, table))

    res = cur.execute(f"PRAGMA table_info({table})")
    columns = [row[1] for row in res.fetchall()]
    print(f"The table '{table}' contains the columns:")
    pprint(columns)
    print()
