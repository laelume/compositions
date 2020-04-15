"""
///////////////////////////////
 *****************************
	# HAJIMEMASHITE
    # ashlaeblume, june 2019
 *****************************
///////////////////////////////

The following doesn't work yet...
all_bass = [a0, a1, a2, a3, a4, a5, a6, a7, a8]
bass = [a0, a1]
harmony = [b0, b1, b2, b3, b4]
allvars=zip(bass, harmony)
print(bass)
"""

Clock.bpm = 150
a0 >> bass([(0,9), (7,3)], dur=4, pan=(-0.6,0.6), amp=.9)
a1.stop()

a1 >> bass([(0,9),(7,3),(5,8),(0,5),(4,10)], dur=4, pan=(-0.6,0.6), amp=1)
a0.stop()
a9.stop()

b0 >> charm([11, 10, 9], dur=[2/4, 4/4, 6/4], amp=1.2)

b0 >> charm([7, 6, 5], dur=[2/4, 4/4, 6/4], amp=2.1)
b0.stop()

b1 >> scatter([(0,9),(3,7),11,(0,2)], dur=3, pan=(-0.2,0.2), amp=4.5)

b1.stop()
b2 >> pluck([0,4,5,7], dur=[3/3,3/2,3/2], amp=4.3)
b2.stop()

b3 >> soft([9,3,7,0,11,3,7,0], dur=(9/3), pan=(-0.7,0.7), amp=1.3)

b4 >> viola([4,5,8,9], dur=[3/2,3/2,3/2], pan=0.5, amp=.7)

all_drums = [d0, d1, d2, d3, d4, d5, d6, d7, d8, p0, p1, p2, p3, p4, p5, p6, p7]
trial_drums = [dx]


d0 >> play("  x-x[---]x-o-(  -x[--o]){-oxx}", sample=[3,2], pan=[-0.4], amp=1)
#dx is a trial drum beat to test for equivalence with d0
dx >> play("  x-x[---]x-o-xx", sample=[3,2], pan=[-0.4], amp=1)

d1 >> play("(x--x,xo  ox)([oo],[---])x-x", sample=4, pan=[0.4], amp=.7)

d2 >> play("x-oox--o([xx-]o-x,xo    ox)", sample=1, pan=[-1.6, 1.6], amp=.8)

d3 >> play(("x   "), amp = 0.9)

d0.stop()
d1.stop()
d2.stop()
d3.stop()

d4.stop(); d5.stop(); d6.stop(); d7.stop();
"""
blend out a0, a1 bass and blend a2 bass with b4 viola
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
HAPPY CALYPSO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
this_bass=[a2, a3]
this_melody=[b5, b6, b7]
this_drums=[d0, d1, d2, d3]

a2 >> bass([9,5,4,6,3,2,0,4],dur=[2,2,1,3,2,3,1,2],pan=[-.2,.2],amp=1.1)
a1.stop()

a3 >> bass([0,(3),(4,2),(6,11)], dur=[2,2,2,2], pan=(-0.6,0.6), amp=1)
a3.stop()
a2.stop()

b5 >> pluck([2,9,4,[(0,4),(3,5)]], dur=[1,1/2,1,1,1/2,1], amp=2.7)
b5.stop()

b6 >> bell([0,2,4,6,9,10], dur=[1/2,1,1,1/2,1,1], amp=2.2)
b6.stop()
b7 >> dub([0, 2, 4, 1, 6], amp=.3)
b7.stop()


~~~~~~~~

#a4->c0, c1, c2, c3
#drums d4, d5, d6, d7

a4 >> bass([0,2,(4,8),(0,9),(4,6),(3,5),3,(1,4)], dur=4, pan=(-0.7,0.7), amp=.6)
a3.stop()
a2.stop()

c0 >> gong([0,2,4,2,4,6,3,5,7,-1,2,4,-2,2,4], dur=[3/2,3/2,2/2], pan=(-.4,.4), amp=5.3)
c0.stop()
c1 >> dub([5,5,(4,6),2,2,1], dur=[1,3/2,3/2], pan=.2, oct=6, amp=0.35)
c1.stop()
c2 >> pluck([1,10,3,9,8], dur=[2,1,2,2,1,2], pan=-.2, amp=3.3)
c2.stop()
c3 >> blip([0, 5, 5, (3,6), (2,7), (2,8), (1,3), (0,4), (1,2), (0,2)], dur = [3/2, 2, 1, 2, 3/2, 3/2, 2, 3/2, 2, 1], pan=0.5, amp=1)
c3.stop()



d4 >> play("(x  --x,--  -o)  o-x--oxxo ", sample=3, pan=[-0.4,0.4], amp=.6)
d5 >> play("x oox- -x-oo xx,(x--[xo-oxx],x-- o- -x)", sample=2, pan=.6,amp=.6)
d6 >> play("-x-o-o-ooxxo", sample=7, pan=.5, amp=.6)
d7 >> play("x-oox--o([xx-]o-x, xoo[xoo])", sample=19, pan=[-1.4, 1.9], amp=.6)

d0.stop()
d1.stop()
d2.stop()
d3.stop()

d4.stop()
d5.stop()
d6.stop()
d7.stop()

p0.stop()
p1.stop()
p2.stop()
p3.stop()

p4.stop()
p5.stop()
p6.stop()
p7.stop()

~~~~

#c3 works with a4, sounds rly weird and cool!!
c3 >> blip([0, 5, 5, (3,6), (2,7), (2,8), (1,3), (0,4), (1,2), (0,2)], dur = [3/2, 2, 1, 2, 3/2, 3/2, 2, 3/2, 2, 1], pan=0.5, amp=1)
c3.stop()
#CARRIDE (drums)

p0 >> play("x       ", sample=3, amp = 0)
p1 >> play("  x     ", sample=2, amp = 0)
p2 >> play("    x   ", sample=5, amp = 0)
p3 >> play("      x ", sample=6, amp = 0)
p4 >> play("-*  --  * - ", sample = 3, pan = [-0.5, 0.5], amp = 0)
p5 >> play(" [oo] [--]    ", sample = 3, pan = [-1, 1], amp = 0)
p5 >> play(" [oo] [--]", sample = 3, pan = [-1, 1], amp = 0)
p5 >> play("  [ o]", sample = 3, pan = [-1, 1], amp = 0)

p5.stop()
p4.stop()
p3.stop()
p2.stop()
p1.stop()
p0.stop()

~~~~~~~~~~~~~~~~~~~~~~~

IKKAKU NO TABI

Clock.bpm=133

# a5->

a4.stop()

a6 >> glass([7,3,2], dur=[4,7,5,3], pan=0.5, amp=2.2)
a6.stop()

a5 >> bass([12,8,7], dur=(4,7,5,3), pan=(-0.5), amp=.5)
a4.stop()

f0 >> space([5], dur=(4), pan=0.2, amp=1.2)
f4 >> space([7], dur=(6), pan=-0.2, amp=1.4)
f5 >> space([9], dur=(10), pan=0.6, amp=1.4)
f6 >> space([11], dur=(13), pan=-0.6, amp=1.4)

f0.stop()
f4.stop()
f5.stop()
f6.stop()

#slightly new section, keep space running...
#

f7 >> bell([3,2,3,1], dur=[3,2], amp=1.7)
f7 >> charm([3,2,3,1], dur=[3,2], amp=1.9)

d8 >> play("x- xo", sample=5, pan=[-0.4,0.4], amp=.5)
d8.stop()
d9 >> play("(x  -x,-  -o)  o-x-oxx ", sample=9, pan=[-0.6,0.6], amp=.2)

a7 >> bass([3,2,3,1], dur=[3], amp=.9)
a5.stop()
~~~~~~~~
#CARRIDE (drums) p0, p1, p2, p3, p4, p5, p6, p7

p0 >> play("x       ", sample=3, amp = 1.6)
p1 >> play("  x     ", sample=2, amp = 1.6)
p2 >> play("    x   ", sample=5, amp = 1.6)
p3 >> play("      x ", sample=6, amp = 1.6)

p3.stop()

p4 >> play("-*  --  * - ", sample = 3, pan = [-0.5, 0.5], amp = .9)
p5 >> play(" [oo] [--]    ", sample = 3, pan = [-1, 1], amp = .9)
p5 >> play(" [oo] [--]", sample = 3, pan = [-1, 1], amp = .9)

p7 >> play("  [ o]", sample = 3, pan = [-1, 1], amp = 0.6)

p7.stop()
~~~~~

#a8, a9-> p8, p9, q0, q1, q2, q3

a7 >> bass([3,2,3,1], dur=[3], amp=.8)
a7 >> bass([3,2,3,1,0,5,7,1], dur=[3], amp=1.1)
f7 >> bell([3,2,3,1], dur=[3,2], amp=1.7)
f7 >> charm([3,2,3,1], dur=[3,2], amp=1.9)

a7.stop()
f7.stop()
a8 >> bass([3, 6, 9], oct = [4,5], dur=[1, 1, 2], amp = 1.2)
a8 >> bass([0, 4, 6], oct = [4,5], dur=[1, 1, 2], amp = 1.2)


f7 >> bell([3,2,3,1], dur=[3,2], amp=1)
p8 >> bell([2, 4, 5, 6, 8], dur=[1, 2, 2, 1/2, 1/2], pan = [-0.1, 0.1], amp=1)

f7.stop()
p8.stop()

p9 >> charm([6, [7,8], [9,11,13]], dur=[2/4, 4/4, 6/4, 1], pan = [-0.2, 0.2], amp=1.3)
p9.stop()

a9 >> bass([0,1,2,5,6, 7, 2, 5, 0,1, 3, 4], dur = 4, amp = .9)
f7 >> bell([3,2,3,1], dur=[3,2], amp=1.7)
f7 >> charm([3,2,3,1], dur=[3,2], amp=1.9)
f7.stop()
a7.stop()
a8.stop()
a9 >> bass([0,1,2,7,9, 10, 2, 5, 0,1, 3, 4], dur = 3, amp = .9)

a9.stop()

q0 >> space([0,1,2,4,3,5], dur = [4,4,4,3,1/2, 1/2], pan = [-0.3, 0.3], amp = 1.2)
q1 >> space([5], dur = 5/2, pan = [-0.4, 0.4], amp = 1)
q2 >> space([6], dur = 3, pan = [-0.5, 0.5], amp = 1)
q3 >> space([7], dur = 5, pan = [-0.6, 0.6], amp = 1)
q4 >> space([8], dur = 3/2, pan = [-0.7, 0.7], amp = 1)

p0.stop()
