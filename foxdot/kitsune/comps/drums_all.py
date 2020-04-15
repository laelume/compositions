import sys
sys.path.append("/Users/timehopper/FoxDot/kitsune")
#Clock.bpm=linvar([120, 143], [30,inf],start=now)
Clock.bpm=143
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    DRUMS & DRUMS & DRUMS & DRUMS & DRUMS & DRUMS &
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import time
#all_drums = [d0, d1, d2, d3, d4, d5, d6, d7, d8, p0, p1, p2, p3, p4, p5, p6, p7]
"""
def startDrums():
    for i in range(len(mix)):
        mix[i]=linvar([0,1],[128,inf],start=now)
"""
#startDrums()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GAIN MIXERS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#fadeamp=linvar([1,0],[16,inf],start=now)
mix0=[1 # mix0[0] -> mix[0] -> d0.amp
    , 0
    , 0
    , 0
    , 0
    , 0 #H
    , 0
    , 0
    , 0
    ]
mix1=[1
    , linvar([0.4, 1.5], 6)
    , linvar([0.5, 2], 4)
    , 0.7
    , 0.7
    , 0 #H
    , 1
    , 0
    , 0
    ]
mix2=[1
    , 1
    , 1
    , 1
    , 1
    , 1 #H
    , 1
    , 1
    , 1
    ]
mix3=[linvar([1, 0], [32,inf],start=now)
    , linvar([1, 0], [32,inf],start=now)
    , linvar([1, 0], [32,inf],start=now)
    , linvar([1, 0], [32,inf],start=now)
    , linvar([1, 0], [32,inf],start=now)
    , linvar([1, 0], [32,inf],start=now)
    , linvar([1, 0], [32,inf],start=now)
    , linvar([1, 0], [32,inf],start=now)
    , linvar([1, 0], [32,inf],start=now)
    ]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FILTERS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
lp=[0,500,1000,1500,2000,3000,4000,5000,10000]
lopa0=[0
    , 0
    , 0
    , 0
    , 0
    , 0
    , 0
    , 0
    , 0
    ]
lopa1=[lp[1]
    , lp[3]
    , lp[1]
    , lp[3]
    , lp[1]
    , lp[3]
    , lp[1]
    , lp[3]
    , lp[1]
    ]
lopa2=[lp[2]
    , lp[2]
    , lp[2]
    , lp[2]
    , lp[2]
    , lp[2]
    , lp[2]
    , lp[2]
    , lp[2]
    ]
lopa4=[ linvar( [ lp[2], 20000 ], 128, start=now )
      , linvar( [ lp[2], 20000 ], 128, start=now )
      , linvar( [ lp[2], 20000 ], 128, start=now )
      , linvar( [ lp[2], 20000 ], 128, start=now )
      , linvar( [ lp[2], 20000 ], 128, start=now )
      , linvar( [ lp[2], 20000 ], 128, start=now )
      , linvar( [ lp[2], 20000 ], 128, start=now )
      , linvar( [ lp[2], 20000 ], 128, start=now )
      , linvar( [ lp[2], 20000 ], 128, start=now )
    ]
hipa0=[8000
    , 15000
    , 4000
    , 0
    , 0
    , var([0,4000], [28,4])
    , 0
    , 0
    , 0
    ]
hipa1=[0
    , 0
    , 0
    , 0
    , 0
    , 0
    , 0
    , 0
    , 0
    ]
# Parameter defs have to be after initializations
lopa=lopa
hipa=hipa0
#mix=mix0
mix=linvar([mix1,mix2],8)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PATTERNS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
this=[d0, da, db, d1, d2]
next=[d3, d4, d5, d6, d7]
mini=[d0, da, d2]
micro=[d0, db, d3]
d0 >> play("V", dur=1, pan=PSine(10), lpf=lopa[0], hpf=hipa[0], amp=mix[0]),
p0= "V"
#print(d0.amp)
#d0 >> play("V   ", dur=0.25, , amp = 0.8)
#d1 >> play(" x-x[--]x-v -", sample=[3,2], pan=linvar([-0.5,0.5],3), amp=0.7),
#d1.every(8, 'reverse')
da >> play(" nd ox-x", sample=[3,2], pan=linvar([-0.5,0.5],3), lpf=lopa[1], hpf=hipa[1], amp=mix[1]).every(16, 'reverse'),
#dx >> play("1234")
db >> play("    [--]x-v", sample=[3,2], pan=linvar([0.5,-0.5],5), lpf=lopa[2], hpf=hipa[2], amp=mix[2]).every(16, 'reverse'),
#db.every(4, 'reverse')
#dpatt1="  x-x[---]x-o-(  -x[--o]){-oxx}"
d2 >> play("xx xx-   xx -x--", sample=4, pan=[0.4], lpf=lopa[3], hpf=hipa[3], amp=mix[3]).every(128, 'reverse'),
#dpatt2="(x--x,xo  ox)([oo],[---])x-x"
d3 >> play("x-oox--([xx]o-x xo    ox)", sample=1, pan=[-1.6, 1.6], lpf=lopa[4], hpf=hipa[4], amp=mix[4]).every(512, 'reverse'),
#dpatt3="x-oox--o([xx-]o-x,xo    ox)"
dx >> play(PZip("V(s,h,k)", "n  n  "), sample=2, lpf=lopa[5], hpf=hipa[5], amp=mix[5]).every(3, 'stutter', dur=1),
dy >> play("  xtx[vvv]x( -x[--k]){kl}",sample=[3,2], pan=[-0.7, 0.7], lpf=lopa[6], hpf=hipa[6], amp=mix[6]*1.5)
e0 >> play("    xxxx", amp=mix[7])
e1 >> play("asclkprtyui", amp=mix[8])
"""
d4 >> play("(x  --x --  -o)  o-x--oxxo ", sample=5, pan=[-0.4,0.4], amp=.6)
d5 >> play("x oox- -x-oo xx (x--[xo-oxx] x-- o- -x)", sample=8, pan=.6,amp=.6)
d6 >> play("--o-o-ooxx", sample=9, pan=.5, amp=.6)
d7 >> play("x-oox--([xx-]o-x  xoo[xoo])", sample=19, pan=[-1.4, 1.9], amp=.6)
"""

def stopAll(self):
    for item in self:
        item.stop()

def allOn(self):
    for item in self:
        item.amp=1
def allOff(self):
    for item in self:
        item.amp=0
def mode1():
    allOn(mini)
    allOff(micro)
def mode2():
    allOn(micro)
    allOff(mini)

allOn(this)
mode1()
mode2()

stopAll(this)

"""
think i wanted to use a dictionary to map for some reason...idk why...
mixmap={procedural scripting for switching between different mix settings}
"""

# put this insode of some loop
mode1()
time.sleep(4)
mode2()

while True:
    print("This prints once a minute.")
    time.sleep(60) # Delay for 1 minute (60 seconds).

"""
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

print(d0.amp)
print(d0.degree)
print(d0.pan)
print(d0.dur)
print(d0.attr)

def getPlayerParams(player):
    for item in player.attr:
        print(item)
getPlayerParams(d0)

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

print(Clock.playing)
