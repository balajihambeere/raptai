import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from databases import Database
from src.core.config import settings
import sqlalchemy

metadata = sqlalchemy.MetaData()

database = Database(settings.DATABASE_URL, force_rollback=settings.DB_FORCE_ROLL_BACK)

# Create tables
async def create_tables():
    engine = sqlalchemy.create_engine(settings.DATABASE_URL)
    metadata.create_all(bind=engine)

async def connect():
    await database.connect()

async def disconnect():
    await database.disconnect()

