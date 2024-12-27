from sqlalchemy import create_engine, Column, Integer, Date
from sqlalchemy.orm import registry, Session

# import db_uri from db_uri.py file.
import os, sys
parent_dir = os.path.dirname(os.path.abspath(__file__)) # path for current directory
parent_dir = os.path.dirname(parent_dir) # path for parent directory
sys.path.append(parent_dir) # add path to sys.path
from db_uri import db_uri # import db_uri

engine = create_engine(db_uri, echo=True)

mapper_registry = registry()

Base = mapper_registry.generate_base()

# create HealthData models in sqlalchemy and create tables based on them in database.
class HealthData(Base):
    __tablename__ = 'health_data'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    exercise = Column(Integer, nullable=False)
    meditation = Column(Integer, nullable=False)
    sleep = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<HealthData {self.id}>'

Base.metadata.create_all(engine)

# run this file to create health_table in database.