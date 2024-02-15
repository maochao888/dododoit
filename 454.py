# 第454节课 Python学习手册第六部分：类和面向对象编程（OOP）：第29章：嵌套的类：重温LEGB作用域规则
X = 1  # 定义全局变量X

def nester():
    print(X)  # 打印全局变量X: 1
    class C:
        print(X)  # 打印全局变量X: 1
        def method1(self):
            print(X)  # 打印全局变量X: 1
        def method2(self):
            X = 3  # 在此方法内部定义局部变量X，隐藏了全局变量X
            print(X)  # 打印局部变量X: 3

    I = C()  # 创建类C的实例I
    I.method1()  # 调用method1，打印全局变量X: 1
    I.method2()  # 调用method2，打印局部变量X: 3
    print(X)  # 打印全局变量X: 1
print('_'*40)  # 打印分隔线
nester()  # 调用nester函数，打印：1, 1, 1, 3
print('-'*40)  # 打印分隔线


