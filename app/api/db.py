from sqlalchemy import (Column, Integer, MetaData, 
                        String, Table, create_engine, 
                        ARRAY)

from databases import Database
from dotenv import load_dotenv
from os import getenv

if not load_dotenv("./app/api/.env"):
    raise AssertionError(".env file is not located")
psql_user, psql_pass = getenv("POSTGRES_USER"), getenv("POSTGRES_PASS")

if not psql_user or not psql_pass:
    raise ValueError("pass or username is not in .env")

DATABASE_URL = f"postgresql://{psql_user}:{psql_pass}@localhost/movie_db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    'movies',
    metadata, 
    Column('id', Integer,primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column("casts", ARRAY(String))
)

database = Database(DATABASE_URL)