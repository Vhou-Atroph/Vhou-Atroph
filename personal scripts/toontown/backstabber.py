#Lord Lowden Clear toontown
from panda3d.core import *
from direct.directbase import DirectStart
from direct.actor.Actor import Actor

from colors import cogHands
from colors import toonColors

#Base actor model - Cog suit.
cog=Actor('phase_3.5/models/char/suitA-mod.bam',
#Idle animations
{'idle':'phase_5/models/char/suitA-glower.bam'})
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
cog.find('**/hands').setColor(cogHands.legalPolyColor)#This sets LLC's hand color to be that of all bossbots, stored in cogHands.py

#Head model
head=loader.loadModel('phase_4/models/char/suitA-heads.bam').find('**/backstabber')
head.reparentTo(cog.find('**/joint_head'))

#Dagger
dagger=loader.loadModel('phase_5/models/props/dagger.bam')
dagger.reparentTo(render)
dagger.setPos(0.44,-4.75,2.33)
dagger.setHpr(180,-33,33)
dagger.setScale(0.8)

base.cam.setPos(0,-20,5)
base.run()