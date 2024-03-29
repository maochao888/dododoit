# 第452节课 Python学习手册第六部分：类和面向对象编程（OOP）：第29章：属性名称： 对象命名空间
# object.X引用与赋值的区别

# 在Python中，当你执行赋值语句 `object.X = value` 时，你正在在 `object` 的命名空间内创建或修改一个名为 `X` 的属性，
# 并将其值设置为 `value`。这个操作只影响 `object` 的命名空间，不会影响其他对象或作用域。
#
# 当你引用一个属性，如 `object.X`，Python会首先在 `object` 的命名空间中查找 `X`。
# 如果在 `object` 的命名空间中找不到 `X`，Python会继续在 `object` 的父类（如果有的话）的命名空间中查找，这个过程会沿着继承树向上进行，
# 直到找到 `X` 或者到达继承树的顶部。这就是所谓的继承树搜索。
#
# 然而，当你执行赋值操作 `object.X = value` 时，Python不会进行继承树搜索。无论 `X` 是否在 `object` 的父类的命名空间中存在，
# Python都会在 `object` 的命名空间中创建或修改 `X`。这意味着，如果 `X` 在 `object` 的父类的命名空间中存在，
# `object.X = value` 不会影响父类的 `X`，它只会影响 `object` 的 `X`。