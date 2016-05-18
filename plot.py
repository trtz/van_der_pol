from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
import webbrowser


class Plot:
    def __init__(self):
        self.graphs = []
        self.colors = []
        self.generators = []

    def add(self, generator, color='black'):
        self.generators.append(generator)
        self.graphs.append(generator.get_graph())
        self.colors.append(color)

    def draw(self):
        p = figure(plot_width=1000, plot_height=600)
        lines = [[], []]
        for i in range(len(self.graphs)):
            line = self.graphs[i]
            x, y = line
            lines[0].append(x)
            lines[1].append(y)
        p.multi_line(lines[0], lines[1], line_width=1, color=self.colors)
        html = file_html(p, CDN, "Van Der Pol Generator Visualizer")
        file = open('graphic.html', 'w')
        file.write(html)
        file.close()
        webbrowser.open('graphic.html')

    def remove(self, num):
        if num >= len(self.graphs):
            return False
        #print(self.colors)
        self.graphs.pop(num)
        self.colors.pop(num)
        return True

    def __len__(self):
        return len(self.graphs)

    def get_instance(self):
        res = []
        for i in range(len(self)):
            res.append(str(i))
        return res

    def str(self, i):
        graph = self.generators[i]
        color = self.colors[i]
        l = graph.l
        m = graph.m
        start = (graph.x0, graph.y0)
        h = graph.h
        steps = graph.steps
        current = '{0} l={1} m={2} start={3} h={4} steps={5}'.format(color, str(l), str(m), str(start),
                                                                     str(h), str(steps))
        return current

    def print_all(self):
        for i in range(len(self.graphs)):
            print(str(i))

    def to_list(self):
        if not self.graphs:
            return 'Nothing to show'
        models = []
        for color in self.colors:
            models.append(color)
        res = ''

        for i, color in enumerate(models):
            res += '{0}. {1}\n'.format(str(i), color)
        return res[:-1]

    def clear(self):
        self.graphs = []
        self.colors = []
