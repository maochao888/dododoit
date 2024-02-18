# 第456节课 Python学习手册第六部分：类和面向对象编程（OOP）：第29章：命名空间链接：一 个类树爬升器
# 上一节说明了实例和类的特殊属性 class 和 bases ，但是没有例子说明为什么要注意这些属性。
# 这节将会给出一个例子， 一个类树爬升器。 简而言之， 这些属性让你可以在程序代码内查看继承层次。
# 在Python中，创建一个子类（Subclass）需要在类定义时指定父类（Superclass）。class Tree:
def classtree(cls, indent):
    print('.' * indent + cls.__name__)  # 打印类名，cls.__name__ 是获取类名的方式，cls 是一个类对象，__name__ 是类对象的一个特殊属性，表示类的名称。
                                        # indent 是一个整数，表示缩进的级别。在这个上下文中，每个缩进级别对应3个点号。
    for supercls in cls.__bases__:  # 递归遍历所有父类，在Python中，每个类都有一个特殊的属性 __bases__，它是一个包含所有父类的元组。
        classtree(supercls, indent + 3)  # 递归遍历所有父类
# classtree(cls, indent) 函数接收两个参数，一个类和一个缩进级别。
# 它首先打印类名，然后递归地遍历并打印所有父类的名字，每次递归缩进级别增加3

def instancetree(inst):
    print('Tree of', inst)  # 打印实例名，所以，print('Tree of', inst) 这行代码的作用是打印出 "Tree of" 字符串，
    # 后面跟着 inst 实例的字符串表示形式。这打印结果通常是实例的类名和内存地址。
    classtree(inst.__class__, 3)  # classtree(inst.__class__, 3) 这段代码的作用是调用 classtree 函数，显示 inst 实例的类及其所有父类的继承层次，每个层次的缩进为3个点号。

def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E: pass
    class F(D, E): pass

    instancetree(B())
    instancetree(F())
# selftest() 函数定义了一些类，并创建了它们的实例，然后使用 instancetree 函数来显示这些实例的类树。

if __name__ == '__main__':
    selftest()  # 自测代码
# 这个脚本定义了一个类树爬升器， 它可以显示一个类的继承层次。 这个脚本的核心是两个函数， 一个用来显示类树， 一个用来显示实例树。
# 如果这个脚本是作为主程序运行，那么就会调用 selftest() 函数进行自我测试。