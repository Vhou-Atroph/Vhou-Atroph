#Lord Lowden Clear toontown
from panda3d.core import *
from direct.directbase import DirectStart
from direct.actor.Actor import Actor

from colors import cogHands
from colors import toonColors

#Base actor model - Cog suit.
cog=Actor('phase_5/models/char/cogA_robot-zero.bam',
#Idle animations
{'idle':'phase_6/models/char/suitA-effort.bam'})
cog.loop('idle')
cog.setH(180)
cog.reparentTo(render)

base.cam.setPos(0,-20,5)
base.run()