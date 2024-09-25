# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Created By Suraj Shaw. 
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

N=200
spin = np.where(np.random.random((N+1,N+1))>0.5,1,-1)
fig=plt.figure()
im=plt.imshow(spin,cmap=plt.cm.cividis)
T=1.5
r=0.5
def  ising(spin):
    for i in range (500):
        x,y=np.random.randint((N+1,N+1))
        if x ==0 or x == N :
            E=-spin[x][y]*(spin[N-x][y]+spin[x-1][y]+\
                             spin[x][N-y]+spin[x][y-1])
        elif  y == 0 or y == N:
            E=-spin[x][y]*(spin[x+1][y]+spin[x-1][y]\
                             +spin[x][N-y]+spin[x][N-y])
        else:
            E=-spin[x][y]*(spin[x+1][y]+spin[x-1][y]+\
                             spin[x][y+1]+spin[x][y-1])
        if E>0:
            spin[x][y] =-1*spin[x][y] 
        elif np.exp(2*E/T)>r:
            spin[x][y] =-1*spin[x][y]
        else :
            spin[x][y]=spin[x][y]
    return spin

def init():
    im.set_data(np.zeros((N,N)))
def anim(i):
    im.set_data(ising(spin))
    plt.suptitle('T:'+str(T)+'K   i:'+str(i))
    return im
#fig.suptitl('Ising model', fontsize=14)
plt.colorbar()
anim = animation.FuncAnimation(fig, anim, init_func=init,\
                               frames=10000,interval=10)

plt.show()