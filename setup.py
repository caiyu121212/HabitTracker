from setuptools import setup,find_packages

setup(
    #1.基础信息
    name="habittracker",
    version="0.1.0",
    decription="个人习惯追踪分析系统",
    long_description=open("README.md",encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    #2.作者信息
    author="你的名字",
    author_email="你的邮箱@Example.com",
    url="https://github.com/caiyu121212/HabitTracker",
    #包配置
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    include_package_data=True,

    #依赖管理
    install_requires=[
        "sqlalchemy>=1.4.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "python-dotenv>=0.19.0",
        "click>=8.0.0",
    ],

    #命令行工具
    entry_points={
        "console_scripts": [
            "habittracker=cli.main:main",
        ],
    },
     #分类信息
    calssifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    # 其他
    python_requires=">=3.8",
    license="MIT",

)