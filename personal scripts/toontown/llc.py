#Lord Lowden Clear toontown
from panda3d.core import *
from direct.directbase import DirectStart
from direct.actor.Actor import Actor

from colors import cogHands
from colors import toonColors

#Base actor model - Cog suit.
llc=Actor({'head':'phase_3/models/char/tt_a_chr_dgm_skirt_head_1000.bam',
'body':'phase_3.5/models/char/suitA-mod.bam'},
#Idle animations
{'head':{'idle':'phase_3/models/char/tt_a_chr_dgm_skirt_head_neutral.bam'},
'body':{'idle':'phase_5/models/char/suitA-fingerwag.bam'}})
llc.attach('head','body','joint_head')
llc.loop('idle')
llc.setH(180)
llc.reparentTo(render)

#Texture files for Cashbot suit
suitTex=loader.loadTexture('phase_3.5/maps/m_blazer.jpg')
llc.findAllMatches('**/torso').setTexture(suitTex,1)
suitTex=loader.loadTexture('phase_3.5/maps/m_sleeve.jpg')
llc.findAllMatches('**/arms').setTexture(suitTex,1)
suitTex=loader.loadTexture('phase_3.5/maps/m_leg.jpg')
llc.findAllMatches('**/legs').setTexture(suitTex,1)
llc.find('**/hands').setColor(cogHands.moneyPolyColor)#This sets LLC's hand color to be that of all cashbots, stored in cogHands.py

#Head coloring
llc.findAllMatches('**/head').setColor(toonColors.brightRed)
llc.findAllMatches('**/head-front').setColor(toonColors.brightRed)

base.cam.setPos(0,-20,5)
base.run()