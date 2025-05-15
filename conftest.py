# conftest.py
from datetime import datetime, timedelta

import pytest

data = {'passed': 0, 'failed': 0}


def pytest_runtest_logreport(report: pytest.TestReport):
    if report.when == 'call':
        print(f"本次用例执行的结果：{report.outcome}")
        data[report.outcome] += 1


def pytest_collection_finish(session: pytest.Session):
    data['total'] = len(session.items)
    print(f"要执行的用例数量 {data['total']}")


def pytest_configure():
    """在所有测试开始前执行"""
    data['start_test'] = datetime.now()
    print(f"\n{data['start_test']} pytest开始执行")


def pytest_unconfigure():
    """在所有测试结束后执行"""
    data['end_test'] = datetime.now()
    print(f"\n{data['end_test']} pytest结束执行")
    # 计算时间差
    data['time_stamp'] = data['end_test'] - data['start_test']
    print(f"测试用例执行的时间{data['time_stamp']}")

    formatted_str = "{:.2f}".format(data['passed'] / data['total']*100)
    data['passing_rate'] = formatted_str + "%"
    assert timedelta(seconds=3) <= data['time_stamp'] <= timedelta(seconds=4)
    assert data['total'] == 3

    assert data['passed'] == 2
    assert data['failed'] == 1
    assert data['passing_rate']=="66.67%"
