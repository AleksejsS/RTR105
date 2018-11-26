# Fails: 170.py
# Autors : Aleksejs Saraps
# Apliecibas numurs 181REB312
# Datums 26.11.2018
# Sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi

# -*- coding : utf -8 -*-
from math import sin, fabs
from time import sleep

def f(x):
    return sin(x)

# definejam argumenta x robezhas :
a = 1.1
b = 3.2

# Aprekinam funkcijas vertibas dotajos punktos:
funa = f(a)
funb = f(b)

#parbaudam, vai dotajaa intervalaa ir saknes:
if ( funa * funb > 0.0 ) :
     print "dotajaa intervalaa [%s, %s] saknju nav"%(a,b)
     sleep(1); exit()   # zinjo uz ekrana, gaida 1 sec. un darbu pabeidz
else:
    print "Dotaaja intervalaa sakne(s) ir!"

# Definejam precizitati, ar kaadu mekleesim sakni:
deltax = 0.01

# Sashaurinam saknes mekleshanas robezhas:
while ( fabs(b-a) > deltax ):
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
        b=x
    else:
        a=x

print "Sakne ir: " , x

    
