# 第455节课 Python学习手册第六部分：类和面向对象编程（OOP）：第29章：命名空间字典：复习
# 在Python中，创建一个子类（Subclass）需要在类定义时指定父类（Superclass）。
# 这可以通过在类名后的括号中添加父类的名称来实现。子类会继承父类的所有属性和方法，
# 你也可以在子类中添加新的属性和方法，或者重写父类的方法。
#
# 假设我们有一个父类`Super`，我们可以创建一个名为`Sub`的子类，如下所示：
#

class Super:
    def hello(self):
        self.data1 = 'spam'

class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'

# 在这个例子中，`Sub`类继承自`Super`类。`Sub`类有一个新的方法`hola`，
# 并且它也继承了`Super`类的`hello`方法。
# 当然，我们可以创建一个新的子类，比如叫做`AnotherSub`，它也继承自`Super`类，
# 并且添加一个新的方法`bonjour`，这个方法定义了一个新的实例变量`data3`。
class AnotherSub(Super):
    def bonjour(self):
        self.data3 = 'toast'

# 在这个例子中，`AnotherSub`类继承自`Super`类。`AnotherSub`类有一个新的方法`bonjour`，
# 并且它也继承了`Super`类的`hello`方法。

# 创建一个 Sub 类的实例，并将其赋值给变量 X
X = Sub()

# 打印实例 X 的所有属性，这是一个字典
print(X.__dict__)  # 输出：{}

# 打印实例 X 的类，也就是 Sub
print(X.__class__)  # 输出：<class '__main__.Sub'>

print('-'*40)
# 打印 Sub 类的所有父类，也就是 Super
print(Sub.__bases__)  # 输出：(<class '__main__.Super'>,)

# 打印 Super 类的所有父类，也就是 object
print(Super.__bases__)  # 输出：(<class 'object'>,)