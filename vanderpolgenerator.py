from model import Model


class VanDerPolGenerator(Model):
    def __init__(self, l, m, start, h, steps):
        f = lambda x, y: y
        g = lambda x, y: - x + (l + m * x ** 2 - x ** 4) * y
        self.l = l
        self.m = m
        super().__init__(f, g, start, h, steps)
