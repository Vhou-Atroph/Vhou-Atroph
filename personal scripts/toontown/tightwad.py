#Lord Lowden Clear toontown
from panda3d.core import *
from direct.directbase import DirectStart
from direct.actor.Actor import Actor

from colors import cogHands
from colors import toonColors

#Base actor model - Cog suit.
cog=Actor('phase_3.5/models/char/suitC-mod.bam',
#Idle animations
{'idle':'phase_5/models/char/suitC-sidestep-left.bam'})
cog.loop('idle')
cog.setH(180)
cog.reparentTo(render)

#Texture files for Cashbot suit
suitTex=loader.loadTexture('phase_3.5/maps/m_blazer.jpg')
cog.findAllMatches('**/torso').setTexture(suitTex,1)
suitTex=loader.loadTexture('phase_3.5/maps/m_sleeve.jpg')
cog.findAllMatches('**/arms').setTexture(suitTex,1)
suitTex=loader.loadTexture('phase_3.5/maps/m_leg.jpg')
cog.findAllMatches('**/legs').setTexture(suitTex,1)
cog.find('**/hands').setColor(cogHands.moneyPolyColor)#This sets LLC's hand color to be that of all bossbots, stored in cogHands.py

#Head model
head=loader.loadModel('phase_3.5/models/char/suitC-heads.bam').find('**/tightwad')
head.reparentTo(cog.find('**/joint_head'))

base.cam.setPos(0,-20,5)
base.run()