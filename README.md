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
 
