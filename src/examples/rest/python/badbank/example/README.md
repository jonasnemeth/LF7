```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python secrets_handling.py 
source secrets.env

rm badbank.db
python db_creation.py

python db_example_data.py
python db_statements.py

uvicorn api:app --reload
```

[http://localhost:8000/docs](http://localhost:8000/docs)
