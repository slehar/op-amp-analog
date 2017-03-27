# -*- coding: utf-8 -*-
"""
OpAmpAnalogFb.py

Created on Fri Feb 12 16:33:03 2016

@author: slehar
"""
#%%
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.widgets import CheckButtons
import matplotlib.lines as mlines
import matplotlib.image as mpimg
from matplotlib import animation
from vertslider import VertSlider

# Global variables
valPlus  = 0.5
valMinus = 0.5
piston = 0.
output = 0.
feedback = 0.
rodLength = .52
rodHeight = .02
hafRod = rodLength/2
pistHeight = .128
pistThickness = .02
hafThick = pistThickness/2
winThresh = .1
dt = .08
offset = 0.045 # Difference between center of fig and center of piston

# Open figure and set axes 1 for drawing Artists
plt.close('all')
fig = plt.figure(figsize=(10,10))
fig.canvas.set_window_title('Op-Amp With Feedback Hydraulic Analogy')
fig.text(.3, .95, 'Op-Amp With Feedback', size=24)
fig.text(.35, .9, 'Hydraulic Analogy', size=24)
ax = fig.add_axes([.1, .1, .8, .8])
ax.set_xticks([])
ax.set_yticks([])

img2 = mpimg.imread('OpAmpAnalog3.png')
(ySize, xSize, zSize) = img2.shape
aspect = float(ySize)/float(xSize)
ax.imshow(img2, extent=[-1., 1., -aspect, aspect])
whitebox = mpatches.Rectangle((-.3, -.7), .75, .15, fc='w', ec='w')
ax.add_patch(whitebox)

# Define blue piston and red piston rod
redbox  = mpatches.Rectangle((-.22, -.100),rodLength,rodHeight, fc='r')
bluebox = mpatches.Rectangle((.05, -.15), pistThickness, pistHeight, fc='b')
ax.add_patch(redbox)
ax.add_patch(bluebox)

# Add Function Line
funcPointsX = [-.2, -.02, .02, .2]
funcPointsY = [ .1,  .1, -.1, -.1]
dx, dy =  .05, -.14
sx, sy = 1.05, 0.65
fPointsX = [(x+dx)*sx for x in funcPointsX]
fPointsY = [(y+dy)*sy for y in funcPointsY]
fLine    = mlines.Line2D(fPointsX,    fPointsY,    color=(1,.5,0),
                         visible=False, lw=3)
ax.add_line(fLine)

# Add load valve lines
#loadValve1 = mpatches.Arc((-.088,.578), .08, .08, theta1=0., theta2=180., fc='r')
loadValveCirc = mpatches.Ellipse((-.088,.577), .08, .08, fc='k')
ax.add_patch(loadValveCirc)
loadValveRect1 = mpatches.Rectangle((-.13,.57), .08, .015, ec=None, fc='w', visible=False)
loadValveRect2 = mpatches.Rectangle((-.08,.536), .08, .015, ec=None, fc='w', angle=90.)
ax.add_patch(loadValveRect1)
ax.add_patch(loadValveRect2)
valveOn = False

# Checkboxes
rax = plt.axes([0.05, 0.05, 0.2, 0.3])
check = CheckButtons(rax, ['Function Line', 'Pause', 'Load'], [False, False, False])


#%%
def func(label):
    global dt, valveOn
    if   label == 'Function Line':
        fLine.set_visible(not fLine.get_visible())
    elif label == 'Pause':
        if check.lines[1][0].get_visible():
            dt = 0
        else:
            dt = 0.1
    elif label == 'Load':
        if check.lines[2][0].get_visible():
            loadValveRect1.set_visible(True)
            loadValveRect2.set_visible(False)
            loadValveCirc.set_facecolor('r')
            valveOn = True
        else:
            loadValveRect1.set_visible(False)
            loadValveRect2.set_visible(True)
            loadValveCirc.set_facecolor('k')
            valveOn = False
    plt.draw()
#%%    
check.on_clicked(func)

axSlMinus = fig.add_axes([.42, .05, .05, .2])
axSlPlus  = fig.add_axes([.565, .05, .05, .2])
axOutput  = fig.add_axes([.65, .61,  .05, .2])
axOutput.set_xlim(0,1)
axOutput.set_ylim(-15.,15.)
axOutput.set_xticks([])
axOutput.set_yticks([])
redRect = plt.Rectangle((0., 0.), 1., 0., color='r')
grnRect = plt.Rectangle((0., 0.), 1.,  0., color='g')
axOutput.add_patch(redRect)
axOutput.add_patch(grnRect)
outText = ax.text(.15, .42, '%4.2f'%0., fontsize=18)
pistonText = ax.text(.0, -.45, '%4.2f'%0., fontsize=18,)
pistonLabel = ax.text(-.1, -.38, 'pistonPos', fontsize=18,)

#%%
def updateSlPlus(num):
    global valPlus
    valPlus = vslPlus.val
    #print 'sl1: val = %4.2f'%val

#%%
def updateSlMinus(num):
    global valMinus
    valMinus = vslMinus.val
    #print 'sl2: val = %4.2f'%val

#%%
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

#%%
def winFunc(piston):
    if piston <= -winThresh:
        return -15
    elif piston > -winThresh and piston < winThresh:
        return 15. * piston * 1./(2.*winThresh)
    else:
        return 15

#%%
def animate(num):
    global piston, output, feedback

    if valveOn:
        load = .1
    else:
        load = 0.
    if check.lines[1][0].get_visible(): # If paused
        piston = valPlus - valMinus
    else:
        piston += dt * (valPlus - valMinus + load) - feedback
    if   piston > 1.:
        piston = 1
    elif piston < -1:
        piston = -1
    pistonText.set_text('%4.2f'%piston)
    output = winFunc(piston)
    feedback = 0.01 * output
    outText.set_text('%4.2f'%output)   
    if output > 0:
        grnRect.set_height(output)
        redRect.set_height(0.)
    else:
        redRect.set_height(output)
        grnRect.set_height(0.)
    #redPos = ( - hafRod - hafThick + offset) + .15 * -piston
    redPos = ( - hafRod + offset) + .15 * -piston
    redbox.set_x(redPos)
    bluePos = redPos + .27
    bluebox.set_x(bluePos)        
    #print 'Piston: %4.2f Output: %4.2f'%(piston, output)

#%%    
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
