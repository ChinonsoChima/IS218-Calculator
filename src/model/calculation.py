class Calculation:
    def __init__(cls, a, b, op):
        cls.a = float(a)
        cls.b = float(b)
        cls.op = op

    def getResult(cls):
        return cls.op(cls.a, cls.b)
