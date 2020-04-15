print(SynthDefs)

Clock.bpm=140

~~~~~~~~

a0 >> bass([(7,3)], dur=4, pan=(-0.6,0.6), amp=.0)
a1.stop()
b1.stop()
e1.stop()
f1.stop()

~~~~~~~~

a1 >> bass([(0,9),(7,3),(5,8),(0,5),(4,10)], dur=4, pan=(-0.6,0.6), amp=.3)
a0.stop()
b1.stop()
e1.stop()
f1.stop()

f1 >> bass([9,5,4,6,3,2,0,4],dur=[2,2,1,3,2,3,1,2],pan=[-.2,.2],amp=.5)
a0.stop()
a1.stop()
b1.stop()
e1.stop()

a2 >> charm([11, 10, 9], dur=[2/4, 4/4, 6/4], amp=.3)

a3 >> scatter([(0,9),(3,7),11,(0,2)], dur=3, pan=(-0.2,0.2), amp=1)

a4 >> pluck([1,7,6,5], dur=[3/3,3/2,3/2], amp=.2)

a5 >> soft([9,3,7,0,11,3,7,0], dur=(9/3), pan=(-0.7,0.7), amp=1)

a6 >> viola([4,5,8,9], dur=[3/2,3/2,3/2], amp=.6)

a2.stop()
a3.stop()
a4.stop()
a5.stop()
a6.stop()

~~~~~~~~

b1 >> bass([0,(3),(4,2),(6,11)], dur=[2,2,2,2], pan=(-0.6,0.6), amp=.4)
a0.stop()
a1.stop()
e1.stop()
f1.stop()

b2 >> pluck([2,9,4,[(0,4),(3,5)]], dur=[1,1/2,1,1,1/2,1], amp=.5)

b3 >> donk(P[3,4,6,11,2].mirror(), dur=3/2, pan=linvar([-1, 1],8), amp=.3)

b4 >> marimba([-0,2,4,6,9,10], dur=[1/2,1,1,1/2,1,1], amp=2)

b5 >> dub([0, 2, 4, 1, 6], amp=.3)

b2.stop()
b3.stop()
b4.stop()
b5.stop()

~~~~~~~~

d1 >> play("  x-x[---]x-o-(  -x[--o]){-oxx}", sample=[3,2], pan=[-0.4], amp=.5)

d2 >> play("(x--x,xo  ox)([oo],[---])x-x", sample=4, pan=[0.4], amp=.3)

d3 >> play("x-oox--o([xx-]o-x,xo    ox)", sample=1, pan=[-1.6, 1.6], amp=.3)

d1.stop()
d2.stop()
d3.stop()

~~~~~~~~

e1 >> bass([0,2,(4,8),(0,9),(4,6),(3,5),3,(1,4)], dur=4, pan=(-0.6,0.6), amp=.5)
a0.stop()
a1.stop()
b1.stop()
f1.stop()

e2 >> gong([0,2,4,2,4,6,3,5,7,-1,2,4,-2,2,4],dur=[3/2,3/2,2/2],amp=1.1,pan=(-.1,.1))

e3 >> blip([5,5,[4,6],2,2,1], dur=[1,3/2,3/2],amp=.7,pan=-.8,amp=.7)

e4 >> pluck([1,10,3,9,8], dur=[2,1,2,2,1,2],pan=.6,amp=.5)

e2.stop()
e3.stop()
e4.stop()

~~~~~

d4 >> play("(x  --x,--  -o)  o-x--oxxo ", sample=3, pan=[-0.4,0.4], amp=.5)

d5 >> play("x oox- -x-oo xx,(x--[xo-oxx],x-- o- -x)", sample=2, pan=.6,amp=.4)

d6 >> play("-x-o-o-ooxxo", sample=7, pan=.5, amp=.3)

d7 >> play("x-oox--o([xx-]o-x, xoo[xoo])", sample=19, pan=[-1.4, 1.9], amp=.3)

d4.stop()
d5.stop()
d6.stop()
d7.stop()
