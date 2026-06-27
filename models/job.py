from sqlalchemy import Column,Integer, String, Enum, ForeignKey
from models.company import company
from database import Base,engine,SessionLocal

from models.company import company
from sqlalchemy.orm import declerative_base


Base = declerative_base()

class Job(Base):
    __tablename__="jobs"
    id=Column(Integer, primary_key=True,index=True)
    title=Column(String,nullable=False)
    description= Column(String)
    salary=Column(Integer)
    company_id=Column(Integer, ForeignKey("companies.id"))
    company=relationship("company",back_populates="jobs")