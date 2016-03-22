# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 12:50:46 2016

@author: slehar
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Open figure and set axes 1 for drawing Artists
plt.close('all')
fig = plt.figure(figsize=(10,10))
fig.canvas.set_window_title('Op-Amp Hydraulic Analogy')
ax = fig.add_axes([.1, .1, .8, .8])

img1 = mpimg.imread('OpAmpAnalog1.png')
plt.imshow(img1)

# Show plot
plt.show()
figmgr=plt.get_current_fig_manager()
figmgr.canvas.manager.window.raise_()
geom=figmgr.window.geometry()
xLoc,yLoc,dxWidth,dyHeight=geom.getRect()
figmgr.window.setGeometry(10,10,dxWidth,dyHeight)
