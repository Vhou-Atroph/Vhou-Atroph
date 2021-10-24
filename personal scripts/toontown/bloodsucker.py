#Lord Lowden Clear toontown
from panda3d.core import *
from direct.directbase import DirectStart
from direct.actor.Actor import Actor

from colors import cogHands
from colors import toonColors

#Base actor model - Cog suit.
cog=Actor('phase_3.5/models/char/suitB-mod.bam',
#Idle animations
{'idle':'phase_4/models/char/suitB-squirt-small.bam'})
cog.loop('idle')
cog.setH(180)
cog.reparentTo(render)

#Texture files for Cashbot suit
suitTex=loader.loadTexture('phase_3.5/maps/l_blazer.jpg')
cog.findAllMatches('**/torso').setTexture(suitTex,1)
suitTex=loader.loadTexture('phase_3.5/maps/l_sleeve.jpg')
cog.findAllMatches('**/arms').setTexture(suitTex,1)
suitTex=loader.loadTexture('phase_3.5/maps/l_leg.jpg')
cog.findAllMatches('**/legs').setTexture(suitTex,1)
cog.find('**/hands').setColor(cogHands.b)#these comments henceforth will be inaccurate lol

#Head model
head=loader.loadModel('phase_4/models/char/suitB-heads.bam').find('**/movershaker')
head.reparentTo(cog.find('**/joint_head'))
headTex=loader.loadTexture('phase_4/maps/blood-sucker.jpg')
head.setTexture(headTex,1)

base.cam.setPos(0,-20,5)
base.run()