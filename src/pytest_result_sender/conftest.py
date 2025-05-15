# conftest.py
import pytest
from datetime import datetime,timedelta

from virtualenv.run import Session

data={}

def pytest_collection_finish(session:pytest.Session):
    # 统计需要执行的用例数量
    data['total']=len(session.items)
    print(f"要执行的用例数量 {data['total']}")


def pytest_configure():
    """在所有测试开始前执行"""
    data['start_test']=datetime.now()
    print(f"\n{data['start_test']} pytest开始执行")


def pytest_unconfigure():
    """在所有测试结束后执行"""
    data['end_test']=datetime.now()
    print(f"\n{data['end_test']} pytest结束执行")
    # 计算时间差
    data['time_stamp']=data['end_test']-data['start_test']
    print(f"测试用例执行的时间{data['time_stamp']}")

    assert timedelta(seconds=3) <= data['time_stamp'] <= timedelta(seconds=5)
    assert data['total'] == 3

