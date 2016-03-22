# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:38:12 2016

@author: slehar
"""

import matplotlib.pyplot as plt
from matplotlib import animation

# Open figure and set axes 1 for drawing Artists
plt.close('all')
fig = plt.figure(figsize=(10,10))
fig.canvas.set_window_title('Op-Amp Hydraulic Analogy')
ax = fig.add_axes([.1, .1, .8, .8])


axSlMinus = fig.add_axes([.3, .7, .2, .1])
axSlPlus  = fig.add_axes([.5, .7, .2, .1])
slMinus = plt.Slider(axSlMinus, label='Minus',  valmin=0, valmax=1,
                    valinit=.5)
slPlus  = plt.Slider(axSlPlus, label='Plus',  valmin=0, valmax=1,
                    valinit=.5)

def animate(num):
    pass

    
anim = animation.FuncAnimation(fig, animate, 
                               repeat=True,
                               interval=0)

# Show plot
plt.show()
figmgr=plt.get_current_fig_manager()
figmgr.canvas.manager.window.raise_()
geom=figmgr.window.geometry()
(xLoc,yLoc,dxWidth,dyHeight)=geom.getRect()
figmgr.window.setGeometry(10,10,dxWidth,dyHeight)
