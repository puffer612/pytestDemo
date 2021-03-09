# pytestDemo
本项目实现接口自动化技术： python+request+Pytest+Yaml+Allure; 通过python+request来发送和处理Http协议的请求
接口，使用pytest作为测试执行器，使用yaml来管理测试数据，使用allure来生成测试报告。

# 项目说明
本项目在实现过程中，把整个项目拆分成请求方法封装，HTTP接口封装，关键字封装，测试用例封装；
首先例用python把Http接口封装成为python接口，接着把这些python接口组装成为一个个关键字，再把这些
关键字组成测试用例，而测试数据则通过yaml文件统一进行管理，然后再通过pytest测试执行器来运行这些脚本。
最后进行Jenkins进行集成。

# 项目结构
 - api  ======>接口封装类，如http接口封装成为python接口
 - common  ======>各种工具类 
 - core  ======> requests 请求封装方法，关键字返回结果
 - config  ======>配置文件
 - data  ======>测试数据文件管理
 - operation ======>关键字封装层，如多个python接口封装成为关键字
 - pytest.ini  ======>pytest配置文件
 - requirements.txt  ======>相关依赖文件  pip install -r requirements.txt
 - testCase  ======>测试用例
 
# 关键字封装说明
关键字应该有一定的业务意义，在封装关键字的时候，可以通过调用多个接口来完成。在某些情况下，需要关联
多个接口来判断执行结果与预期一致。

# 测试报告
在命令行执行命令：''''pytest''' 运行完用例后，会得到一个原始的测试报告文件，需要运行allure。

pytest --cov=messageCenter --cov-report=html 执行测试代码覆盖
