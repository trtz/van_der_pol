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
- draw graphs (requires setting parameters)
- zoom plot
- add graphs
- remove graphs (double click on right panel)

Run: python main.py
To run program, you need:
- python3
- tkinter - included by default (so does not need to be installed)
- bokeh     /* Lib to draw graphs. Install it via pip install bokeh or pip3 install bokeh */
- web browser



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
