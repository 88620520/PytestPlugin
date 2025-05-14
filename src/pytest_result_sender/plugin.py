# conftest.py
from datetime import datetime


def pytest_configure():
    """在所有测试开始前执行"""
    print(f"\n{datetime.now()} pytest开始执行")


def pytest_unconfigure():
    """在所有测试结束后执行"""
    print(f"\n{datetime.now()} pytest结束执行")
