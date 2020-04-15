import time
import sys
#sys.path.append("/Users/timehopper/FoxDot/kitsune/compositions/carride")
#from lib import procedures
#startDrums()
#Clock.bpm=linvar([120, 136.67], [30,inf],start=now)
Clock.bpm=136.67
print(Clock.playing)
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    DRUMS & DRUMS & DRUMS & DRUMS & DRUMS & DRUMS &
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#all_drums = [d0, d1, d2, d3, d4, d5, d6, d7, d8, p0, p1, p2, p3, p4, p5, p6, p7]
# Parameter defs have to be after initializations
lopa=lopa0
hipa=hipa0
mix=mix0
#mix=linvar([mix1,mix2],8)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PATTERNS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
this=[d0, da, db, d1, d2]
next=[d3, d4, d5, d6, d7]
mini=[d0, da, d2]
micro=[d0, db, d3]
dz >> play("V", dur=1, pan=PSine(10))
d0 >> play("V", dur=1, pan=PSine(10), lpf=lopa[0], hpf=hipa[0], amp=mix[0])
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
