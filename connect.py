from sqlalchemy import create_engine,text

db_url = "mysql+pymysql://root:password@localhost/sqlalchemy"
engine = create_engine(db_url,echo=True)

with engine.connect() as conn:
    result = conn.execute(text('select "Hello" '))
    print(result.all())