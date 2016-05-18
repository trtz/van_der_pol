# Kursach po diffuram

Welcome to Van Der Pol Generator Visualizer v1.0!
This simple graphical application creates phase portrait of Van Der Pol Generator.

Set of equations:
* x' = y
* y' = - x + (l + m * x ** 2 - x ** 4) * y

Portrayal requires:
* parameter l
* parameter m
* start point   |  for classical Runge–Kutta method
* h             |  for classical Runge–Kutta method
* steps         |  for classical Runge–Kutta method

That's all you can:
1. draw graphs (requires setting parameters)
2. zoom plot
3. add graphs
4. remove graphs (double click on right panel)

Run: python main.py
To run program, you need:
1. python3
2. tkinter - included by default (so does not need to be installed)
3. bokeh     /* Lib to draw graphs. Install it via pip install bokeh or pip3 install bokeh */
4. web browser



                    /^\/^\           SssSss
                  _|__|  O|            sSsssSs
         \/     /~     \_/ \            ssSSsss
          \____|__________/  \
                 \_______      \
                         `\     \                 \
                           |     |                  \
                          /      /                    \
                         /     /                       \
                       /      /                         \ \
                      /     /                            \  \
                    /     /             _----_            \   \
                   /     /           _-~      ~-_         |   |
                  (      (        _-~    _--_    ~-_     _/   |
                   \      ~-____-~    _-~    ~-_    ~-_-~    /
                     ~-_           _-~          ~-_       _-~
                        ~--______-~                ~-___-~
