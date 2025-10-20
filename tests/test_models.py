import unittest
import sys
import os
from datetime import date

# 添加 src 到路径，确保导入正常工作
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from database.models import Habit,HabitRecord


class TestModels(unittest.TestCase):
    def test_habit_creation(self):
        """测试习惯创建"""
        habit = Habit(name="晨跑", category="health", target_frequency="daily")
        self.assertEqual(habit.name, "晨跑")
        self.assertEqual(habit.category, "health")
        self.assertEqual(habit.target_frequency, "daily")

    def test_habit_record_creation(self):
        """测试习惯记录创建"""
        record = HabitRecord(
            habit_id=1,
            record_date=date.today(),
            completion_status="completed",
            value=5.0
        )
        self.assertEqual(record.habit_id, 1)
        self.assertEqual(record.completion_status, "completed")
        self.assertEqual(record.value, 5.0)


if __name__ == '__main__':
    unittest.main()