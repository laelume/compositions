"""import sys
sys.path.append("/Users/timehopper/FoxDot/kitsune/compositions/carride")
"""

import mixer

Class Procedures:
    def startDrums():
        for i in range(len(mix)):
            mix[i]=linvar([0,1],[128,inf],start=now)

    def allsynths():
        synthlist=[]
        for item in SynthDefs:
            synthlist.append(item)
        return synthlist

    def stopAll(self):
        for item in self:
            item.stop()

    def allOn(self):
        for item in self:
            item.amp=1
#allOn(this)
    def allOff(self):
        for item in self:
            item.amp=0
    def mode1():
        allOn(mini)
        allOff(micro)

    def mode2():
        allOn(micro)
        allOff(mini)

    def getPlayerParams(player):
        for item in player.attr:
            print(item)
            return item
#getPlayerParams(d0)


mode1()
mode2()
stopAll(this)


mini=[d0,da]

def fadeOut(player,howlong,wait):
    thisamp=player.amp
    print('prev amp:',thisamp)
    newamp = linvar([thisamp, 0], howlong, start=wait)
    print('new amp:',newamp)
    player.amp=newamp


fadeOut(d0, 5, 5)


def remix(mixgroup, ampmix, howlong):
    for i in range(len(mixgroup)):
        for player in mixgroup:
            player.amp=ampmix[i]

#remix(mini, mix2)


#doesnt work yet...
def cycle_players():
    newlist=allsynths()
    for i in range (len(newlist)):
            plyr= newlist[i]
    return plyr

ww >> plyr([0, 1, 2, 3], dur=2)

"""
think i wanted to use a dictionary to map for some reason...idk why...
mixmap={procedural scripting for switching between different mix settings}


# put this inside of some procedural loop:
# starting in mode1, wait 4 (seconds/steps?), then enter mode2

mode1()
time.sleep(4)
mode2()

while True:
    print("This prints once a minute.")
    time.sleep(60) # Delay for 1 minute (60 seconds).


Unfinished...

def everyOther(pattlist):
    num_patts=len(pattlist)
    for pattern in pattlist:
        #run that pattern 4 times then switch to the other pattern
        #how to count the clock...
"""
"""
https://foxdot.org/docs/player-keys/
"""
