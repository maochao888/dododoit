X = 11                       # Global (module) name/attribute (X, or manynames.X)

def f():
    print(X)                 # Access global X (11)

def g():
    X = 22                   # Local (function) variable (X, hides module X)
    print(X)

class C:
    X = 33                   # Class attribute (C.X)
    def m(self):
        X = 44               # Local variable in method (X)
        self.X = 55          # Instance attribute (instance.X)