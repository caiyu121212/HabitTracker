import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

from .models import Base

load_dotenv()


class DatabaseManager:
    def __init__(self, database_url=None):
        # Windows 路径处理
        if database_url is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            db_path = os.path.join(base_dir, 'habittracker.db')
            self.database_url = f"sqlite:///{db_path}"
        else:
            self.database_url = database_url

        # 创建数据库引擎
        self.engine = create_engine(self.database_url, echo=True)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def create_tables(self):
        """创建所有表"""
        try:
            Base.metadata.create_all(bind=self.engine)
            print("✅ 数据库表创建成功")
            return True
        except SQLAlchemyError as e:
            print(f"❌ 创建表失败: {e}")
            return False