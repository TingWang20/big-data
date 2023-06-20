# 快速了解和学习一个项目、代码的步骤和思路
# 1.首先找项目的入口（入口文件），若有Dockerfile或Docker compose就找这个文件中的run和cmd命令，然后顺藤摸瓜
# 2.Supervisor进程控制系统，查看supervisor的配置（命令可大概百度看一看即可），重点是：查看执行命令 类似python test.py
# supervisor官方网址：http://supervisord.org/
# 3.大概了解每个py文件的功能
# 4.@，Python中的@符号表示装饰器,让函数不停息
# 5.位置参数，关键字参数
# 6.yield
def test(*arg, **kwargs):
    a,b,c,d,e,f,g = arg
    print(d)
    print(kwargs["g"])
if __name__ == "__main__":
    test(1,2,3,4,5,6,7,a=1, d='5',g='1')

# 代码规范
# 1.前几行导入Python自带的包(import os)，空一行，然后代码展示Python的三方包(import pandas)。
