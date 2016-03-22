import matplotlib
import numpy
def num_pic(v0,a,b):
    v=[]
    v.append(v0)
    t=numpy.linspace(0,0.1,1000)
    for i in range(999):
        v_next=v[i]+(a-b*v[i])*t[1]
        v.append(v_next)

    v_a = a/b-(a-b*v0)*(numpy.exp(-b*t))/b


    matplotlib.pyplot.figure(figsize=(8,6))
    matplotlib.pyplot.plot(t,v,label="Euler method",color="blue",linewidth=3,linestyle='--')
    matplotlib.pyplot.plot(t,v_a,label="analytic method",color="red",linewidth=3,linestyle=':')
    matplotlib.pyplot.xlabel("Time(t)")
    matplotlib.pyplot.title("Frictional Force")
    matplotlib.pyplot.ylabel("Velocity")
    matplotlib.pyplot.legend(loc='best')
    matplotlib.pyplot.show()

a = float(raw_input('a='))    
v0 = float(raw_input('v0='))
b = float(raw_input('b='))
num_pic(v0,a,b)