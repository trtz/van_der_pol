class Model:
    def __init__(self, f, g, start, h, steps):
        self.f = f
        self.g = g
        self.x0, self.y0 = start
        self.h = h
        self.steps = steps

    def runge_kutta(self):
        x = [self.x0]
        y = [self.y0]
        for i in range(self.steps):
            k = []
            m = []
            point = (x[i], y[i])
            k.append(self.h * self.f(*point))
            m.append(self.h * self.g(*point))
            point = (x[i] + k[0] / 2, y[i] + m[0] / 2)
            k.append(self.h * self.f(*point))
            m.append(self.h * self.g(*point))
            point = (x[i] + k[1] / 2, y[i] + m[1] / 2)
            k.append(self.h * self.f(*point))
            m.append(self.h * self.g(*point))
            point = (x[i] + k[2], y[i] + m[2])
            k.append(self.h * self.f(*point))
            m.append(self.h * self.g(*point))
            x.append(x[i] + (k[0] + 2 * k[1] + 2 * k[2] + k[3]) / 6)
            y.append(y[i] + (m[0] + 2 * m[1] + 2 * m[2] + m[3]) / 6)
        return x, y

    def get_graph(self):
        x, y = self.runge_kutta()
        return [x, y]

