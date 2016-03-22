# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 14:17:09 2016

@author: slehar
"""
import matplotlib.pyplot as plt
from vertslider import VertSlider

# Open figure and set axes 1 for drawing Artists
plt.close('all')
fig = plt.figure(figsize=(10,10))
fig.canvas.set_window_title('Op-Amp Hydraulic Analogy')
ax = fig.add_axes([.1, .1, .8, .8])


axSl1 = fig.add_axes([.4, .05, .05, .2])
axSl2 = fig.add_axes([.6, .05, .05, .2])

def updateSl1(num):
    val = vsl1.val
    print 'sl1: val = %4.2f'%val

def updateSl2(num):
    val = vsl2.val
    print 'sl2: val = %4.2f'%val

vsl1 = VertSlider(axSl1, 'vsl1', 0, 1)
vsl2 = VertSlider(axSl2, 'vsl2', 0, 1)

vsl1.on_changed(updateSl1)
vsl2.on_changed(updateSl2)




# Show plot
plt.show()
figmgr=plt.get_current_fig_manager()
figmgr.canvas.manager.window.raise_()
geom=figmgr.window.geometry()
xLoc,yLoc,dxWidth,dyHeight=geom.getRect()
figmgr.window.setGeometry(10,10,dxWidth,dyHeight)
