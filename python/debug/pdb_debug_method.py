# pdb - 1 侵入式方法 （需要在被调试的代码中添加以下代码然后再正常运行代码）
import pdb;pdb.set_trace()
# pdb - 2 非侵入式（不额外修改源代码，在命令行直接运行调试）
# python3 -m pdb test.py
# pdb命令  ->解释
# break 或 b  ->设置断点
# continue 或 c  ->继续执行程序
# list 或 l  ->查看当前行的代码段
# step 或 s  ->进入函数（进入 for 循环用 next 而不是用 step）
# return 或 r  ->执行代码直到从当前函数返回
# next 或 n  ->执行下一行
# up 或 u  ->返回到上个调用点（不是上一行）
# p x  ->打印变量x的值
# exit 或 q  ->中止调试，退出程序
# help  ->帮助