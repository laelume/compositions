Clock.bpm = 140

n=[0,9]
for n in range(10): sq = n*n
print(n, sq)


~~~~~~~~
HAJIMEMASHITE

a_bass = [a0, a1, a2, a3, a4]

a0 >> bass([(0,9), (7,3)], dur=4, pan=(-0.6,0.6), amp=.5)
a1.stop()
a2.stop()
a3.stop()
a4.stop()

a1 >> bass([(0,9),(7,3),(5,8),(0,5),(4,10)], dur=4, pan=(-0.6,0.6), amp=.6)
a0.stop()
a2.stop()
a3.stop()
a4.stop()

b0 >> charm([11, 10, 9], dur=[2/4, 4/4, 6/4], amp=.3)

b1 >> scatter([(0,9),(3,7),11,(0,2)], dur=3, pan=(-0.2,0.2), amp=0.8)

b2 >> pluck([1,7,6,5], dur=[3/3,3/2,3/2], amp=.5)

b3 >> soft([9,3,7,0,11,3,7,0], dur=(9/3), pan=(-0.7,0.7), amp=1)

b4 >> viola([4,5,8,9], dur=[3/2,3/2,3/2], amp=.3)


a2 >> bass([9,5,4,6,3,2,0,4],dur=[2,2,1,3,2,3,1,2],pan=[-.2,.2],amp=.6)
a0.stop()
a1.stop()
a3.stop()
a4.stop()

~~~~~~~~

a3 >> bass([0,(3),(4,2),(6,11)], dur=[2,2,2,2], pan=(-0.6,0.6), amp=.5)
a0.stop()
a1.stop()
a2.stop()
a4.stop()

b5 >> pluck([2,9,4,[(0,4),(3,5)]], dur=[1,1/2,1,1,1/2,1], amp=.5)

b6 >> donk(P[3,4,6,11,2].mirror(), dur=3/2, pan=linvar([-1, 1],8), amp=.6)

b7 >> marimba([-0,2,4,6,9,10], dur=[1/2,1,1,1/2,1,1], amp=2.3)

b8 >> dub([0, 2, 4, 1, 6], amp=.3)

b2.stop()
b3.stop()
b4.stop()
b5.stop()

~~~~~~~~

drums = [d0, d1, d2, d3, d4, d5, d6, d7, d8]

d1 >> play("  x-x[---]x-o-(  -x[--o]){-oxx}", sample=[3,2], pan=[-0.4], amp=.6)

d2 >> play("(x--x,xo  ox)([oo],[---])x-x", sample=4, pan=[0.4], amp=.6)

d3 >> play("x-oox--o([xx-]o-x,xo    ox)", sample=1, pan=[-1.6, 1.6], amp=.5)


~~~~~~~~


a4 >> bass([0,2,(4,8),(0,9),(4,6),(3,5),3,(1,4)], dur=4, pan=(-0.6,0.6), amp=.5)
a0.stop()
a1.stop()
a2.stop()
a3.stop()

c0 >> gong([0,2,4,2,4,6,3,5,7,-1,2,4,-2,2,4], dur=[3/2,3/2,2/2], pan=(-.1,.1), amp=1)

c1 >> blip([5,5,(4,6),2,2,1], dur=[1,3/2,3/2], pan=-.8 amp=.7)

c2 >> pluck([1,10,3,9,8], dur=[2,1,2,2,1,2], pan=.6, amp=.5)

c3 >> blip([0, 5, 5, (3,6), (2,7), (2,8), (1,3), (0,4), (1,2), (0,2)], dur = [3/2, 2, 1, 2, 3/2, 3/2, 2, 3/2, 2, 1], amp=1)

~~~~~

d4 >> play("(x  --x,--  -o)  o-x--oxxo ", sample=3, pan=[-0.4,0.4], amp=.5)

d5 >> play("x oox- -x-oo xx,(x--[xo-oxx],x-- o- -x)", sample=2, pan=.6,amp=.4)

d6 >> play("-x-o-o-ooxxo", sample=7, pan=.5, amp=.3)

d7 >> play("x-oox--o([xx-]o-x, xoo[xoo])", sample=19, pan=[-1.4, 1.9], amp=.3)

d8 >> play("x   ", sample = 6, amp = .4)


IKKAKU NO TABI

print (SynthDefs)

a0 >> sawbass([12,8,7], oct = 4, dur=(4,7,5,3), pan=(0.5, -0.5), amp=.5)
a1 >> bass([7,3,2], oct = 6, dur=(4,7,5,3), pan=(-0.3, 0.3), amp=.4)
a2 >> bass([11,7,6], oct = 6, dur=(4,7,5,3), pan=(-0.3, 0.3), amp=.4)
a3 >> bell([3,2,3,1], dur=[3,2], oct=6, crush=4, bits=4, amp=.6, lpf=linvar([3500,200], 16), lpr = 0.4)
b0 >> space([5], dur=[3,2], pan = -0.2, amp=.6)
b1 >> space([7], dur=[2,2,1], pan = 0.2, amp=.6)
b2 >> space([9], dur=[4,3,3], pan = -0.7, amp=.6)
b3 >> space([11], dur=[3,3,2,2], pan = 0.7, amp=.6)

d0 >> play("x- xo", sample=3, pan=[-0.4,0.4], drive=1, amp=0.2)
d1 >> play("(x  - ,x -  )  o-x-oxx ", sample=9, pan=[-0.6,0.6], amp=.2)
d2 >> play("(  o *, o **)-- -- ** x", sample=6, pan=[-0.8,0.8], amp=.2)
d3 >> play("x  x ( x* o, *xo )", sample=4, pan=[-1,1], amp=.2)

~~~~~~~~
BABY EMU


p0 >> play("x       ", sample=3, amp = 0.9)
p1 >> play("  x     ", sample=2, amp = 0.9)
p2 >> play("    x   ", sample=5, amp = 0.9)
p3 >> play("      x ", sample=6, amp = 0.9)
p4 >> play("  [ o]", sample = 3, pan = [-1, 1], amp = 0.6)
p5 >> play("-*  --  * - ", sample = 4, pan = [-0.5, 0.5], amp = 0.8)
p6 >> play(" [oo] [--]", sample = 5, pan = [-1, 1], amp = .6)

p7 >> bass([3, 6, 9], oct = [4, 5], dur=[1, 1, 2], amp = .8)
p8 >> pluck([2, 4, 5, 6, 8], dur=[1, 2, 2, 1/2, 1/2], amp=0.8, dur=PDur(3,8), chop=4, sus=2)
p9 >> charm([6, 8, 10, rest], dur=[2/4, 4/4, 6/4, 1], amp=.6)


q9 >> space([2], dur = 4, vibdepth = 0.4, vib = 0.4, amp = 0.3, slidefrom=([0.3, 2, 1]), room=4)
q8 >> space([5], dur = 3, amp = 1.)
q7 >> space([6], dur = 7, amp = 1.)
q6 >> space([7], dur = 6, amp = 1.)
q5 >> space([8], dur = 2, amp = 1.)

q9.stop()

q8.stop()

q7.stop()

q6.stop()

q5.stop()

a0.stop()

p9.stop()

p8.stop()

p7.stop()

p6.stop()

p5.stop()

p4.stop()

p3.stop()

p2.stop()

p1.stop()

p0.stop()
