from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database connection
DATABASE = {
    'drivername': 'pgsql',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': '123456',
    'database': 'pruebas2'
}

engine = create_engine(
    f'postgresql+psycopg2://{DATABASE["username"]}:{DATABASE["password"]}@{DATABASE["host"]}/{DATABASE["database"]}'
) # Usando psycopg. No usar psycopg2 por errores



meta = MetaData()
conn = engine.connect()
SessionTemp = sessionmaker(bind=engine, autoflush=False, autocommit=False)

BaseTable = declarative_base(metadata=meta)
BaseTable.metadata.create_all(engine)

def get_db():
    db = conn
    try:
        yield db
    finally:
        db.close()
