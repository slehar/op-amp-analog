# -*- coding: utf-8 -*-
"""
OpAmpAnalog.py

Created on Fri Feb 12 16:33:03 2016

@author: slehar
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.image as mpimg
from matplotlib import animation
from matplotlib.widgets import CheckButtons
from vertslider import VertSlider

# Global variables
valPlus  = 0.5
valMinus = 0.5
piston = 0.
rodLength = .52
rodHeight = .02
hafRod = rodLength/2
pistHeight = .128
pistThickness = .02
hafThick = pistThickness/2
winThresh = .1
dt = .1
offset = 0.045 # Difference between center of fig and center of piston


# Open figure and set axes 1 for drawing Artists
plt.close('all')
fig = plt.figure(figsize=(10,10))
fig.canvas.set_window_title('Op-Amp Hydraulic Analogy')
fig.text(.3, .9, 'Op-Amp Hydraulic Analogy', size=24)
ax = fig.add_axes([.1, .1, .8, .8])
ax.set_xticks([])
ax.set_yticks([])

# Read background image
img1 = mpimg.imread('OpAmpAnalog1.png')
(ySize, xSize, zSize) = img1.shape
aspect = float(ySize)/float(xSize)
ax.imshow(img1, extent=[-1., 1., -aspect, aspect])

# Define blue piston and red piston rod
redbox  = mpatches.Rectangle((-.27, .047),rodLength,rodHeight, fc='r')
bluebox = mpatches.Rectangle((.05, -.008), pistThickness, pistHeight, fc='b')
ax.add_patch(redbox)
ax.add_patch(bluebox)

# Add Function Line
funcPointsX = [-.2, -.02, .02, .2]
funcPointsY = [.1, .1, -.1, -.1]
(dx, dy) = ( .05, .086)
(sx, sy) = (1.05, .65)
fPointsX = [(x+dx)*sx for x in funcPointsX]
fPointsY = [(y+dy)*sy for y in funcPointsY]
fLine    = mlines.Line2D(fPointsX,    fPointsY, visible = False,
                         color=(1,.5,0), lw=3)
ax.add_line(fLine)

# Function Line Checkbox
rax = plt.axes([0.05, 0.05, 0.2, 0.2])
check = CheckButtons(rax, ['Function Line', 'Pause'], [False, False])

def func(label):
    global dt
    if   label == 'Function Line':
        fLine.set_visible(not fLine.get_visible())
    elif label == 'Pause':
        if check.lines[1][0].get_visible():
            dt = 0
        else:
            dt = 0.1
    plt.draw()
    
check.on_clicked(func)

# Add inverting (minus) and non-inverting (plus) input sliders
axSlMinus = fig.add_axes([.42, .075, .05, .2])
axSlPlus  = fig.add_axes([.57, .075, .05, .2])
axOutput  = fig.add_axes([.75, .61,  .05, .2])
axOutput.set_xlim(0,1)
axOutput.set_ylim(-15.,15.)
axOutput.set_xticks([])
axOutput.set_yticks([])
redRect = plt.Rectangle((0., 0.), 1., 0., color='r')
grnRect = plt.Rectangle((0., 0.), 1.,  0., color='g')
axOutput.add_patch(redRect)
axOutput.add_patch(grnRect)
outText = ax.text(.4, .42, '%4.2f'%0., fontsize=18)

def updateSlPlus(num):
    global valPlus
    valPlus = vslPlus.val
    #print 'sl1: val = %4.2f'%val

def updateSlMinus(num):
    global valMinus
    valMinus = vslMinus.val
    #print 'sl2: val = %4.2f'%val

vslPlus  = VertSlider(axSlPlus,  'vsl+', 0, 1)
vslMinus = VertSlider(axSlMinus, 'vsl-', 0, 1)

vslPlus.label.set_visible(False)
vslMinus.label.set_visible(False)

vslPlus.valtext.set_fontsize(18)
vslMinus.valtext.set_fontsize(18)

vslPlus.valtext.set_position((0.5, -0.1))
vslMinus.valtext.set_position((0.5, -0.1))

vslPlus.on_changed(updateSlPlus)
vslMinus.on_changed(updateSlMinus)

# Window function: linear within thresh, +/- 15 otherwise
def winFunc(piston):
    if piston <= -winThresh:
        return -15
    elif piston > -winThresh and piston < winThresh:
        return 15. * piston * 1./(2.*winThresh)
    else:
        return 15

# The animation function (evaluated repeatedly and endlessly)
def animate(num):
    global piston, dt
    
    if check.lines[1][0].get_visible(): # If paused
        piston = valPlus - valMinus
    else:
        piston += dt * (valPlus - valMinus)
    if   piston > 1.:
        piston = 1
    elif piston < -1:
        piston = -1
                
    output = winFunc(piston)
    outText.set_text('%4.2f'%output)   
    if output > 0:
        grnRect.set_height(output)
        redRect.set_height(0.)
    else:
        redRect.set_height(output)
        grnRect.set_height(0.)
    redPos = ( - hafRod  + offset) + .15 * -piston
    redbox.set_x(redPos)
    bluePos = redPos + .27
    bluebox.set_x(bluePos)        
    #print 'Piston: %4.2f output %4.2f '%(piston, output)

# Matplotlib animation funcion calls animate()    
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
