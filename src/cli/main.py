import click
from datetime import datetime,date
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from database.database_manager import DatabaseManager
from services.habit_service import HabitService
from services.analysis_service import AnalysisService


@click.group()
def main():
    """个人习惯追踪分析系统"""
    pass


@main.command()
def init():
    """初始化数据库"""
    db_manager = DatabaseManager()
    if db_manager.create_tables():
        click.echo("✅ 数据库初始化成功")
    else:
        click.echo("❌ 数据库初始化失败")


@main.command()
@click.option('--name', prompt='习惯名称', help='习惯名称')
@click.option('--category', prompt='分类', help='习惯分类')
@click.option('--frequency', prompt='目标频率', type=click.Choice(['daily', 'weekly', 'monthly']), help='目标频率')
@click.option('--description', prompt='描述', default='', help='习惯描述')
def add_habit(name, category, frequency, description):
    """添加新习惯"""
    db_manager = DatabaseManager()
    session = db_manager.get_session()
    habit_service = HabitService(session)

    try:
        habit = habit_service.create_habit(name, category, frequency, description)
        click.echo(f"✅ 习惯 '{habit.name}' 添加成功 (ID: {habit.id})")
    except Exception as e:
        click.echo(f"❌ 添加习惯失败: {e}")
    finally:
        session.close()


if __name__ == '__main__':
    main()