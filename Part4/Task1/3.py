"""
С кодом ниже что-то не так. Что именно неправильно и как это исправить?

class A:
    pass

class B(A):
    pass

class C(A, B):
    pass
"""

class A:
    pass

class B(A):
    pass

class C(B, A):
    pass