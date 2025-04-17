from pydantic import BaseModel, conint

class BankTransfer(BaseModel):
    recipient_iban: str
    recipient_name: str
    purpose: str
    amount_cents: conint(gt=0)  ## transactions must not be negativ!
