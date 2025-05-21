import pytest
from pathlib import Path
from pytest_result_sender import plugin
pytest_plugins = 'pytester'

@pytest.fixture(autouse=True)
def mock():
    bak_data = plugin.data
    plugin.data = {
        "passed":0,
        "failed":0,
    }
    yield
    plugin.data = bak_data

@pytest.mark.parametrize('send_when', ['every', 'on_fail'])
def test_send_when(send_when, pytester: pytest.Pytester, tmp_path: Path):
    # 动态注册配置项（修复点：为每个addini添加help参数）
    conftest_path = tmp_path / "conftest.py"
    conftest_path.write_text("""
def pytest_addoption(parser):
    parser.addini(
        "send_when", 
        type="string", 
        default="on_fail",
        help="When to send reports: 'every' or 'on_fail'"
    )
    parser.addini(
        "send_api", 
        type="string", 
        default="https://baidu.com",
        help="API endpoint for sending reports"
    )
    parser.addini(
        "smtp_server", 
        type="string", 
        default="smtp.163.com",
        help="SMTP server address"
    )
    parser.addini(
        "smtp_port", 
        type="string", 
        default="465",
        help="SMTP server port"
    )
    parser.addini(
        "email_user", 
        type="string", 
        default="18320429962@163.com",
        help="Email account username"
    )
    parser.addini(
        "email_password", 
        type="string", 
        default="YZjjD7hcjVjdKt6v",
        help="Email account password"
    )
    parser.addini(
        "receiver_emails", 
        type="string", 
        default="2922616461@qq.com",
        help="Comma-separated recipient email addresses"
    )
""")

    config_path = tmp_path / "pytest.ini"
    config_path.write_text(f"""
[pytest]
send_when = {send_when}
send_api = https://baidu.com
smtp_server = smtp.163.com
smtp_port = 465
email_user = 18320429962@163.com
email_password = YZjjD7hcjVjdKt6v
receiver_emails = 2922619461@qq.com
""")

    # 测试配置读取
    config = pytester.parseconfig(config_path)
    assert config.getini('send_when') == send_when

    # 运行测试用例
    pytester.makepyfile("""
        def test_pass():
            assert True
    """)
    pytester.runpytest("-c", str(config_path))
    if send_when == 'every':
        assert plugin.data['email_done'] == 1
    else:
        assert plugin.data.get('api_done') is None

    print(plugin.data)
    # assert 1 + 1 == 3

@pytest.mark.parametrize('send_api', ['https://baidu.com', ''])
def test_send_api(send_api, pytester: pytest.Pytester, tmp_path: Path):
  # 动态注册配置项
  conftest_path = tmp_path / "conftest.py"
  conftest_path.write_text("""
def pytest_addoption(parser):
  parser.addini("send_when", type="string", default="on_fail", help="When to send reports")
  parser.addini("send_api", type="string", default="", help="API endpoint")
  # 其他配置...
""")

  # 生成无缩进的pytest.ini
  config_path = tmp_path / "pytest.ini"
  config_path.write_text(f"""[pytest]
send_when = on_fail
send_api = {send_api}
smtp_server = smtp.163.com
smtp_port = 465
email_user = 18320429962@163.com
email_password = YZjjD7hcjVjdKt6v
receiver_emails = 2922619461@qq.com
""")

  # 测试配置读取
  config = pytester.parseconfig(config_path)
  assert config.getini('send_api') == send_api

  # 运行测试
  pytester.makepyfile("def test_pass(): assert True")
  pytester.runpytest("-c", str(config_path))


  if send_api == 'every':
     assert plugin.data['email_done'] == 1
     assert plugin.data['api_done'] == 1
  else:
     assert plugin.data.get('email_done') is None
     assert plugin.data.get('api_done') is None

  print(plugin.data)

