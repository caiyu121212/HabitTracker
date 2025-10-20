from sqlalchemy.orm import Session
from datetime import datetime, date
from typing import List, Optional, Dict
from database.models import Habit, HabitRecord


class HabitService:
    def __init__(self, session: Session):
        self.session = session

    def create_habit(self, name: str, category: str, target_frequency: str, description: str = "") -> Habit:
        """创建新习惯"""
        # 检查习惯是否已存在
        existing = self.session.query(Habit).filter(Habit.name == name).first()
        if existing:
            raise ValueError(f"习惯 '{name}' 已存在")

        habit = Habit(
            name=name,
            category=category,
            target_frequency=target_frequency,
            description=description
        )
        self.session.add(habit)
        self.session.commit()
        return habit

    def record_habit(self, habit_id: int, record_date: date, status: str, value: float = None,
                     notes: str = "") -> HabitRecord:
        """记录习惯完成情况"""
        record = HabitRecord(
            habit_id=habit_id,
            record_date=record_date,
            completion_status=status,
            value=value,
            notes=notes
        )
        self.session.add(record)
        self.session.commit()
        return record