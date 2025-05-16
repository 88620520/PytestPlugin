# conftest.py
from datetime import datetime, timedelta
import requests
import pytest

from httpx import request

data = {'passed': 0, 'failed': 0}


def pytest_addoption(parser):
    # 读取pytest.ini配置文件信息
    parser.addini(
        'send_when',
        help="何时发送"
    )
    parser.addini(
        'send_api',
        help="发送到哪里"
    )


def pytest_runtest_logreport(report: pytest.TestReport):
    # 统计测试用例执行情况
    print(report)
    if report.when == 'call':
        print(f"本次用例执行的结果：{report.outcome}")
        data[report.outcome] += 1


def pytest_collection_finish(session: pytest.Session):
    # 统计测试用例数量
    data['total'] = len(session.items)
    print(f"要执行的用例数量 {data['total']}")


def pytest_configure(config: pytest.Config):
    """在所有测试开始前执行"""
    data['start_test'] = datetime.now()
    print(f"\n{data['start_test']} pytest开始执行")
    print(config.getini('send_when'))
    print(config.getini('send_api'))


def pytest_unconfigure():
    """在所有测试结束后执行"""
    data['end_test'] = datetime.now()
    print(f"\n{data['end_test']} pytest结束执行")
    # 计算时间差
    data['time_stamp'] = data['end_test'] - data['start_test']
    print(f"测试用例执行的时间{data['time_stamp']}")

    formatted_str = "{:.2f}".format(data['passed'] / data['total'] * 100)
    data['passing_rate'] = formatted_str + "%"
    # assert timedelta(seconds=3) <= data['time_stamp'] <= timedelta(seconds=4)
    # assert data['total'] == 3
    #
    # assert data['passed'] ==2
    # assert data['failed'] == 1
    # assert data['passing_rate']=="66.67%"


def send_result():
    if data['send_when'] == 'on_fail' and data['failed'] == 0:
        return

    if not data['send_api']:
        return

    url = data['send_api']

    content = f"""
    python自动化测试结果


    测试时间：{data['end_test']}
    用例数量：{data['total']}
    执行时常：{data['time_stamp']}
    测试通过：<font color='green'>{data['passed']}</font>
    测试失败：<font color='red'>{data['passed']}</font>
    测试通过率：{data['passing_rate']}</br>
    """

    try:
        requests.post(url, json={"msgtype": "markdown",
                                "markdown": {"content": content}})

    except Exception:
        pass


