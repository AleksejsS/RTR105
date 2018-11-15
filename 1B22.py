import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *
x = linspace(0, 4, 11)
y = sin(x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$')

plt.plot(x, y, color = "#00FF00")

y1 = x
y2 = y1 - x**3/(1*2*3)
y3 = y2 + x**5/(1*2*3*4*5)
y4 = y3 - x**7/(1*2*3*4*5*6*7)
plt.plot(x, y1, color = "#000FFF")
plt.plot(x, y2, color = "#0000FF")
plt.plot(x, y3, color = "#FF0000")
plt.plot(x, y4, color = "#FFF000")


plt.show()

