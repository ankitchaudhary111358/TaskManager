from sqlalchemy import Column, Integer,String, Boolean, ForeignKey
from app.config.database import Base

class Task(Base):
    __tablename__="tasks"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    description=Column(String)
    completed=Column(Boolean,default=False)
    owner_id=Column(Integer,ForeignKey.key('users.id'))