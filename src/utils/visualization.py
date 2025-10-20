# src/utils/visualization.py
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import os


def plot_habit_trend(habit_data: pd.DataFrame, habit_name: str, save_path: str = None):
    """绘制习惯完成趋势图 - Windows 兼容版本"""
    # 设置中文字体（Windows 系统）
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    plt.figure(figsize=(12, 6))

    # 转换完成状态为数值
    status_map = {'completed': 1, 'partial': 0.5, 'missed': 0}
    habit_data['status_value'] = habit_data['completion_status'].map(status_map)

    plt.plot(habit_data['record_date'], habit_data['status_value'],
             marker='o', linewidth=2, markersize=4)
    plt.title(f'{habit_name} - 习惯完成趋势', fontsize=14, fontweight='bold')
    plt.xlabel('日期', fontsize=12)
    plt.ylabel('完成状态', fontsize=12)
    plt.ylim(-0.1, 1.1)
    plt.yticks([0, 0.5, 1], ['未完成', '部分完成', '完成'])
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    if save_path:
        # Windows 路径处理
        save_dir = os.path.dirname(save_path)
        if save_dir and not os.path.exists(save_dir):
            os.makedirs(save_dir)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

    plt.show()