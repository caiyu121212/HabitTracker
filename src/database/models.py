import os
from sqlalchemy import Column,Integer,String,Date,DateTime,Float,Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False,unique=True)
    description = Column(Text)
    category = Column(String(100))
    created_at = Column(DateTime,default=datetime.utcnow)

    def __repr__(self):
        return f"<Habit(id={self.id},name='{self.name}')>"


class HabitRecord(Base):
    __tablename__ = 'habit_records'

    id = Column(Integer, primary_key=True)
    habit_id = Column(Integer, nullable=False)
    record_date = Column(Date, nullable=False)
    completion_status = Column(String(20))  # completed, partial, missed
    value = Column(Float)  # 量化值：跑步公里数、学习小时数等
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)