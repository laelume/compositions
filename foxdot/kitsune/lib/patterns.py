import sys
print(sys.path)
from .carride import filters
# ch0
d0 >> play("V", dur=1, pan=PSine(10), lpf=lopa[0], hpf=hipa[0], amp=mix[0])
#d0 >> play("V   ", dur=0.25, , amp = 0.8)
#d1 >> play(" x-x[--]x-v -", sample=[3,2], pan=linvar([-0.5,0.5],3), amp=0.7),
#d1.every(8, 'reverse')
# ch1
da >> play(" nd ox-x", sample=[3,2], pan=linvar([-0.5,0.5],3), lpf=lopa[1], hpf=hipa[1], amp=mix[1]).every(16, 'reverse'),
#dx >> play("1234")
# ch2
db >> play("    [--]x-v", sample=[3,2], pan=linvar([0.5,-0.5],5), lpf=lopa[2], hpf=hipa[2], amp=mix[2]).every(16, 'reverse'),
#db.every(4, 'reverse')
#dpatt1="  x-x[---]x-o-(  -x[--o]){-oxx}"
# ch3
d2 >> play("xx xx-   xx -x--", sample=4, pan=[0.4], lpf=lopa[3], hpf=hipa[3], amp=mix[3]).every(128, 'reverse'),
#dpatt2="(x--x,xo  ox)([oo],[---])x-x"
# ch4
d3 >> play("x-oox--([xx]o-x xo    ox)", sample=1, pan=[-1.6, 1.6], lpf=lopa[4], hpf=hipa[4], amp=mix[4]).every(512, 'reverse'),
#dpatt3="x-oox--o([xx-]o-x,xo    ox)"
# ch5
dx >> play(PZip("V(s,h,k)", "n  n  "), sample=2, lpf=lopa[5], hpf=hipa[5], amp=mix[5]).every(3, 'stutter', dur=1),
# ch6
dy >> play("  xtx[vvv]x( -x[--k]){kl}",sample=[3,2], pan=[-0.7, 0.7], lpf=lopa[6], hpf=hipa[6], amp=mix[6]*1.5)
# ch7
e0 >> play("    xxxx", amp=mix[7])
# ch8
e1 >> play("asclkprtyui", amp=mix[8])
