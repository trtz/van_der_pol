import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox
from vanderpolgenerator import VanDerPolGenerator
from plot import Plot
import re
import sys


class GUI(tkinter.Tk):
    def __init__(self,):
        tkinter.Tk.__init__(self)
        self.title('Van der Pol Generator Visualizer v1.0')
        self.geometry('800x450')

        self.colors = self.get_colors()

        self.parameters_label = tkinter.Label(self, text='Parameters', font=("Arial", 16))
        self.parameters_label.place(x=20, y=17)

        self.l_parameter_label = tkinter.Label(self, text='l  = ', font=('Times New Roman', 13, 'italic'))
        self.l_parameter_label.place(x=20, y=60)

        self.l_parameter_entry = tkinter.Entry(self)
        self.l_parameter_entry.config(width=8)
        self.l_parameter_entry.place(x=60, y=63)

        self.m_parameter_label = tkinter.Label(self, text='m = ', font=('Times New Roman', 13, 'italic'))
        self.m_parameter_label.place(x=20, y=90)

        self.m_parameter_entry = tkinter.Entry(self)
        self.m_parameter_entry.config(width=8)
        self.m_parameter_entry.place(x=60, y=93)

        self.start_x_label = tkinter.Label(self, text='Start X = ', font=('Arial', 11))
        self.start_x_label.place(x=20, y=160)

        self.start_x_entry = tkinter.Entry(self)
        self.start_x_entry.config(width=8)
        self.start_x_entry.insert(0, '0.0')
        self.start_x_entry.place(x=90, y=163)

        self.start_y_label = tkinter.Label(self, text='Start Y = ', font=('Arial', 11))
        self.start_y_label.place(x=20, y=180)

        self.start_y_entry = tkinter.Entry(self)
        self.start_y_entry.config(width=8)
        self.start_y_entry.insert(0, '0.1')
        self.start_y_entry.place(x=90, y=183)

        self.h_label = tkinter.Label(self, text='h = ', font=('Arial', 11))
        self.h_label.place(x=180, y=160)

        self.steps_label = tkinter.Label(self, text='Steps = ', font=('Arial', 11))
        self.steps_label.place(x=180, y=180)

        self.h_entry = tkinter.Entry(self)
        self.h_entry.config(width=8)
        self.h_entry.insert(0, '0.01')
        self.h_entry.place(x=210, y=163)

        self.steps_entry = tkinter.Entry(self)
        self.steps_entry.config(width=8)
        self.steps_entry.insert(0, '10000')
        self.steps_entry.place(x=240, y=183)

        self.color_label = tkinter.Label(self, text='Color', font=('Arial', 11))
        self.color_label.place(x=20, y=240)

        self.color_box = Combobox(self, values=self.colors)
        self.color_box.set('Black')
        self.color_box.place(x=20, y=265)

        self.add_button = tkinter.Button(self, text='Add', font=('Arial', 13), width=10, command=self.add_graphic)
        self.add_button.place(x=220, y=260)

        self.show_button = tkinter.Button(self, text='SHOW', font=('Arial', 14), width=15, height=2, command=self.show)
        self.show_button.place(x=300, y=350)

        self.plot = Plot()

        self.info_labels = tkinter.Listbox(self, selectmode='MULTIPLE', width=60, height=17)
        self.info_labels.bind('<<ListboxSelect>>', self.on_select)
        self.info_labels.place(x=420, y=20)

    def on_select(self, event):
        selected = event.widget.curselection()
        if not selected:
            return
        num = selected[0]
        self.plot.remove(0)
        self.info_labels.delete(num)

    def show(self):
        self.plot.draw()

    def get_values(self):
        try:
            l_parameter = float(self.l_parameter_entry.get())
        except ValueError:
            self.show_error('l parameter is invalid')
            return
        try:
            m_parameter = float(self.m_parameter_entry.get())
        except ValueError:
            self.show_error('m parameter is invalid')
            return
        start_x = float(self.start_x_entry.get())
        start_y = float(self.start_y_entry.get())
        h = float(self.h_entry.get())
        steps = int(self.steps_entry.get())
        color = self.color_box.get()
        color = re.sub('\s*', '', color)
        return l_parameter, m_parameter, (start_x, start_y), h, steps, color

    def add_graphic(self):
        values = self.get_values()
        if not values:
            return
        l, m, start, h, steps, color = values
        try:
            generator = VanDerPolGenerator(l, m, start, h, steps)
            self.plot.add(generator, color)
            self.info_labels.insert('end', self.plot.str(-1))
        except:
            descr = sys.exc_info()[0]
            self.show_error(descr)

    def show_error(self, description):
        messagebox.showerror('Error', description)

    def get_colors(self):
        file = open('all_colors.txt')
        colors = file.readlines()
        without_spaces = []
        for color in colors:
            new_color = color.replace('\s', '')
            without_spaces.append(new_color)
        file.close()
        return without_spaces


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
