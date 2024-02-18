# 第457节课 Python学习手册第六部分：类和面向对象编程（OOP）：第29章：重访文档字符串
# 本节将会重访文档字符串，这是一个在Python中用来记录程序的重要工具。
# 本节将会介绍文档字符串的基本语法，以及如何在程序中使用文档字符串。
# 本节还将会介绍如何使用Python的内置工具来提取文档字符串，以及如何使用文档字符串来生成程序文档。
import docstr

print(docstr.__doc__)
print(docstr.func.__doc__)
print(docstr.spam.__doc__)
print('--' * 40)
x = docstr.spam()
print('*' * 40)
x.method()
# 本节将会重访文档字符串，这是一个在Python中用来记录程序的重要工具。
# `x = docstr.spam()` 这行代码在Python中的作用是创建一个 `spam` 类的实例，并将这个实例赋值给变量 `x`。
#
# `docstr.spam` 是对 `spam` 类的引用，它是在 `docstr` 模块中定义的。在Python中，类名后面的括号 `()` 用于创建类的新实例。
#
# 所以，`x = docstr.spam()` 这行代码的作用是创建一个 `spam` 类的新实例，并将这个实例赋值给变量 `x`。之后，你可以通过 `x` 来访问这个实例及其属性和方法。

# print(help(docstr))