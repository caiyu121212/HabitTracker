# src/services/analysis_service.py
import pandas as pd
from sqlalchemy.orm import Session
from datetime import datetime, date, timedelta
from typing import Dict, List
import matplotlib

# Windows 上可能需要设置 matplotlib 后端
matplotlib.use('TkAgg')  # 或者 'Qt5Agg'
import matplotlib.pyplot as plt


class AnalysisService:
    def __init__(self, session: Session):
        self.session = session

    def get_completion_stats(self, habit_id: int, days: int = 30) -> Dict:
        """获取习惯完成统计"""
        end_date = date.today()
        start_date = end_date - timedelta(days=days)

        # 使用 Pandas 进行数据分析
        query = f"""
        SELECT record_date, completion_status, value
        FROM habit_records 
        WHERE habit_id = {habit_id}
        AND record_date BETWEEN '{start_date}' AND '{end_date}'
        ORDER BY record_date
        """

        df = pd.read_sql(query, self.session.bind)

        if df.empty:
            return {
                'completion_rate': 0,
                'total_days': 0,
                'completed_days': 0,
                'average_value': 0
            }

        total_days = len(df)
        completed_days = len(df[df['completion_status'] == 'completed'])
        average_value = df['value'].mean() if 'value' in df.columns and not df['value'].isna().all() else 0

        return {
            'completion_rate': round(completed_days / total_days * 100, 2) if total_days > 0 else 0,
            'total_days': total_days,
            'completed_days': completed_days,
            'average_value': round(average_value, 2)
        }
