import sys
sys.path.append("../example")

import db_statements
import api
import model

app = api.app
myiban = api.myiban


@app.get("/transactions/vulnerable_example")
def vulnerable_example1(purpose):
    """
    This is an example of a query vulnerable against sql-injections.
    The intended behaviour would be returning all transactions for the iban of the logged in user matching the pattern defined by the argument `purpose`.

    What happens if you use an input like:

    ' OR TRUE --
    """

    cur = db_statements.get_cursor()
    ## Warning: string concatenation in sql-statements is evil!
    query = "SELECT * from account_changes WHERE iban = '" + myiban + "' AND purpose LIKE '%" + purpose + "%'"
    print(query)
    cur.execute(query)
    result = cur.fetchall()
    print(f"returned {len(result)} rows")
    return result


@app.post("/transfer/vulnerable_example")
def vulnerable_example2(transfer: model.BankTransfer):
    """
    This is an example of a statement vulnerable against sql-injections.

    For `recipient_iban` try:

    "'; UPDATE accounts SET balance_cents = 100000000 WHERE iban = 'DE00 1234 1234 1234 1234 01' --"
    """

    con = db_statements.get_connection()
    cur = con.cursor()
    ## Warning: string concatenation in sql-statements is evil!
    statements = f"UPDATE accounts SET balance_cents = balance_cents - '{transfer.amount_cents}' WHERE iban = '{myiban}'; " + \
                 f"UPDATE accounts SET balance_cents = balance_cents + '{transfer.amount_cents}' WHERE iban = '{transfer.recipient_iban}'; " + \
                 f"INSERT INTO account_changes (changed_at, iban, iban_other, flag, amount_cents, purpose, recipient)" + \
                 f"       VALUES (datetime('now'), '{myiban}', '{transfer.recipient_iban}', '-', {transfer.amount_cents}, '{transfer.purpose}', '{transfer.recipient_name}'); " \
                 f"INSERT INTO account_changes (changed_at, iban, iban_other, flag, amount_cents, purpose, recipient)" + \
                 f"       VALUES (datetime('now'), '{transfer.recipient_iban}', '{myiban}', '+', {transfer.amount_cents}, '{transfer.purpose}', '{transfer.recipient_name}')"
    print(statements)
    cur.executescript(statements)
    con.commit()
    return True


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
