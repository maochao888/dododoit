# 第450节课 Python学习手册第六部分：类和面向对象编程（OOP）：第29章：类接口技术
# 这段代码演示了Python中类的继承、方法重写（覆盖）、扩展以及如何通过委托实现期望的接口。
# 代码定义了一个基类Super和四个子类Inheritor、Replacer、Extender、Provider，
# 展示了不同的继承和多态行为。

class Super:
    def method(self):
        print('in Super.method')  # Default behavior
        print('changshixiugai')
    def delegate(self):
        self.action()  # Expected to be defined
#Super类定义了一个method方法，打印一条消息，和一个delegate方法，
# 该方法调用一个action方法，期望在子类中定义。
# class Inheritor(Super):  # Inherit method verbatim
#     pass
# #Inheritor类直接继承Super类，没有做任何改动，继承了Super的所有方法。
# class Replacer(Super):  # Replace method completely
#     def method(self):
#         print(8*8)
#         print('in Replacer.method')
# #Replacer类重写了Super的method方法，提供了不同的实现。
# class Extender(Super):  # Extend method behavior
#     def method(self):
#         print('starting Extender.method')
#         Super.method(self)
#         print('ending Extender.method')
#Extender类扩展了Super的method方法，调用了父类的method方法之前和之后分别添加了额外的行为。
class Provider(Super):  # Fill in a required method
    def action(self):
        print('in Provider.action')
# Provider类就提供了action方法的实现。当Provider的实例调用delegate方法时，
# delegate方法会调用Provider类中定义的action方法。这就是说，Super类将action方法的实现委托给了Provider类。
#Provider类实现了Super类中预期要被定义的action方法，满足了delegate方法的需求。

# 代码中的Super类和Provider类就是一个接口和一个实现的例子。
class ActionProvider(Super):  # Fill in a required method
    def action(self):
        print('in ActionProvider.action')


if __name__ == '__main__':
    # for klass in (Inheritor, Replacer, Extender, Provider,ActionProvider):
    for klass in (Provider, ActionProvider):
        print('\n' + klass.__name__ + '...')
        # klass().method()
        klass().delegate()
    # print('\nProvider...')
    # x = Provider()
    # x.delegate()


# 最后的if __name__ == '__main__':部分是Python的常用模式，用于判断当前脚本是否作为主程序运行，
# 如果是，则执行下面的代码块。代码块中创建了每个子类的实例并调用了它们的method方法，
# 然后创建了Provider类的实例并调用了delegate方法。
#  观察这个例子末尾的自我测试程序代码是如何在 for 循环中建立
# 三个不同类实例的。 因为类是对象， 所以你可以将它们存储在元组中， 并采用通用方式来
# 创建实例， 而无须额外语法（稍后会再谈这个概念）。 类与模块 一 样也有特殊的 name
# 属性。 它默认是类头部行中的类名称字符串。