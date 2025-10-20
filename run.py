import sys
import os

# 添加 src 目录到 Python 路径
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.insert(0, src_path)

try:
    from cli.main import main
    main()
except ImportError as e:
    print(f"Import error: {e}")
    print(f"Python path: {sys.path}")
    print(f"Current directory: {current_dir}")
    print(f"Files in current directory: {os.listdir(current_dir)}")
    if os.path.exists(src_path):
        print(f"Files in src directory: {os.listdir(src_path)}")