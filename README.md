# pytest-result-sender

# dist文件夹
存放打包的插件

#  插件的使用
1.pycharm中使用
把dist文件夹下后缀为whl的文件拷贝到要使用的项目目录下，使用pip install +{拷贝过去的插件名} 进行插件的安装，安装好后就可以在项目使用插件了
  
# src文件
项目的主文件夹，插件的主要代码放在该目录下
 
# pyproject.toml
项目的配置文件
详细：
1.核心项目元数据 ([project])
 [project]
name = "pytest-result-sender"   # 包名称（必须与代码目录名一致）
version = "0.1.0"               # 版本号
description = "Default template for PDM package"  # 包描述
authors = [{name = "", email = ""}]  # 作者信息（需完善）
dependencies = ["pytest>=8.3.5"]     # 依赖项（正确）
requires-python = ">=3.8"            # Python版本要求
readme = "README.md"                 # 文档文件
license = {text = "MIT"}             # 许可证类型

2.构建系统配置 ([build-system])
[build-system]
requires = ["pdm-backend"]     # 构建工具依赖
build-backend = "pdm.backend"  # 指定PDM作为构建后端

3.插件入口点 ([project.entry-points.pytest11])
[project.entry-points.pytest11]
result_log = "pytest_result_sender.plugin"  # pytest插件入口

4.PDM构建配置 ([tool.pdm.build])
[tool.pdm.build]
package-dir = "src"  # 指定源代码目录为src

5.PDM扩展配置 ([tool.pdm])
[tool.pdm]
distribution = true  # 允许生成可分发的包
 # 使用教程：
一、下载插件
pip install pytest-result-sender-jms

二、创建配置文件

在项目的根目录下创建配置文件pytest.ini,配置文件内容如下
[pytest]
# Api服务器配置
# 何时发送，always: 总是发送，on_fail: 失败时发送
send_when = always
# 发送API地址 ，你需要发送信息的接口，例如微信机器人
send_api = https://baidu.com
# 邮箱服务器配置，发送者的邮箱的配置，这里用的是163，具体自行百度
smtp_server = smtp.163.com
# 端口
smtp_port = 465
# 发送邮箱的用户，更改为你需要发送邮箱的用户
email_user = 183...@163.com
# 邮箱授权码，具体获取方法自行百度
email_password = ....
# 接收者邮箱，多个用，隔开
receiver_emails = 2922...@qq.com

三、启动项目
控制台输入pytest -v
