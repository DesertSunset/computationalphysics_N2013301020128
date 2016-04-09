# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 14:18:27 2016

@author: AC
"""

from pylab import *
from matplotlib import pyplot
import math
import numpy

g = 9.8
b2m = 4e-5

class flight_state:
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.vx = _vx
        self.vy = _vy
        self.t = _t

#无阻力，只考虑重力作用
class cannon:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.cannon_flight_state = []
        self.cannon_flight_state.append(_fs)
        self.dt = _dt
        print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy

    def next_state(self, current_state):
        global g
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

    def shoot(self):
        while not(self.cannon_flight_state[-1].y < 0):
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
            print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy

        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0

    def show_trajectory(self):
        x = []
        y = []
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)

        matplotlib.pyplot.figure(figsize=(8,6))
        matplotlib.pyplot.plot(x,y,label="cannon",color="blue",linewidth=3,linestyle='--')
        matplotlib.pyplot.xlabel("x(m)")
        matplotlib.pyplot.title("Target")
        matplotlib.pyplot.ylabel("y(m)")
        matplotlib.pyplot.legend(loc='best')
        matplotlib.pyplot.show()
        #show()

#风阻为常数
class drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

#对大气绝热近似下的风阻
class adiabatic_drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        #风阻随高度改变的系数
        pp0 = (1 - 6.5e-3 * current_state.y / 273.15) ** (2.5)
        next_x = current_state.x + current_state.vx * self.dt
        #风阻随高度改变时1
        next_vx = current_state.vx - pp0 * b2m * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        #风阻随高度改变时1
        next_vy = current_state.vy - g * self.dt - pp0 * b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)


#a = cannon(flight_state(0, 0, 500, 100, 0), _dt = 0.1)
#a.shoot()
#b = drag_cannon(flight_state(0, 0, 100, 500, 0), _dt = 0.1)
#b.shoot()
c = adiabatic_drag_cannon(flight_state(0, 0, 100, 500, 0), _dt = 0.1)
c.shoot()
#a.show_trajectory()
#b.show_trajectory()
c.show_trajectory()
show()
