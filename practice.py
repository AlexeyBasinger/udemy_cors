from sqlalchemy import URL, create_engine, text
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="postgresql+psycopg2",
    username="testuser",
    password="testpassword",
    host="localhost",
    port=5432,
    database="testuser"
)

engine = create_engine(url=url, echo=True)

session_pool = sessionmaker(engine)

with session_pool() as session:
    session.execute(text("SELECT 1"))
    session.execute(text("""
        CREATE TABLE 
    """))
