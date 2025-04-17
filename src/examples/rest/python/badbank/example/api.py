from fastapi import FastAPI
import model
import db_statements

app = FastAPI()

myiban = "DE00 1234 1234 1234 1234 01"  ## TODO iban of authenticated user


@app.get("/iban")
def iban():
    return myiban

@app.get("/balance")
def balance():
    cur = db_statements.get_cursor()
    return db_statements.balance(cur, myiban)

@app.get("/transactions")
def balance():
    cur = db_statements.get_cursor()
    return db_statements.transactions(cur, myiban)

@app.post("/transfer")
## ODO: prevent CSRF
async def transfer_money(transfer: model.BankTransfer):
    con = db_statements.get_connection()
    result = db_statements.transfer(con, myiban, transfer.recipient_iban, transfer.amount_cents, transfer.purpose, transfer.recipient_name)
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
