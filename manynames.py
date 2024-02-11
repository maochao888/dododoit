X = 11                       # Global (module) name/attribute (X, or manynames.X)

def f():
    print(X)                 # Access global X (11)

def g():
    X = 22                   # Local (function) variable (X, hides module X)
    print(X)

class C:
    # 类属性（33）：在类定义中，你可以定义类属性。
    # 这些属性属于类本身，而不是类的任何实例。在你的代码中，
    # X是一个类属性，它的值被设置为33。你可以通过
    # ClassName.X来访问这个属性。
    X = 33                   # Class attribute (C.X)
    # 方法中的局部变量（44）：在方法定义中，你可以定义局部变量。这些变量只在方法内部可见，当方法执行完毕后，这些变量就会被销毁。
    # 在你的代码中，X 是一个局部变量，它的值被设置为44。你只能在方法内部访问这个变量。
    def m(self):
        X = 44               # Local variable in method (X)
        self.X = 55          # Instance attribute (instance.X)
        # return X

# 实例属性（55）：当你创建一个类的实例时，你可以为这个实例添加属性。这些属性属于实例本身，而不是类。
# 在你的代码中，X 是一个实例属性，它的值被设置为55。你可以通过 instanceName.X 来访问这个属性。

# 这个程序中的五个X是完全不同的变量。
# 从上到下， 这里对 X 的赋值语句会产生：模块属性（11） 、 函数内的局部变量（ 22 ） 、 类
# 属性（33）、 方法中的局部变量（44）以及实例属性（55）。 虽然这五个都名为X， 但事
# 实上它们都是在原代码内的不同位置进行赋值的， 或者说是赋值了不同的对象， 因此这些
# 名称都是独立的变量。 这个例子展示了赋值语句的重要性： 它们决定了名称所在的作用域

if __name__ == '__main__':
    print(X)                 # 11: module (a.k.a. manynames.X outside)
    print('*' * 5)
    f()
    print('-' * 10)
    print(X)                 # 11: module
    print('#' * 20)
    g()
    print(X)                 # 11: module
    print('-' * 40)
    obj = C()
    # 这行代码obj = C()在Python中创建了一个C类的实例，并将其赋值给变量obj。
    print(obj.X)             # 33: class
    print('^' * 60)
    obj.m()
    print(obj.X)             # 55: instance
    print('*' * 80)
    print(C.X)               # 33: class (a.k.a. C.X)
    # 这行代码print(C.X)在Python中访问了C类的属性X。
    print(C().X)             # 33: class
    print(C().m())           # None: method
    # print(C().m())` 这行代码的输出是 `None`，这是因为 `C().m()` 这个方法没有返回值。
    # 在Python中，如果一个函数或方法没有明确的返回值（即没有 `return` 语句），那么它默认返回 `None`。
    # 在你的代码中，`m` 方法没有 `return` 语句，所以它的返回值是 `None`。当你尝试打印 `C().m()` 的返回值时，
    # 你看到的输出就是 `None`。
