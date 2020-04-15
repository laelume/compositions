///////////////////////////////
 *****************************
	# HAJIMEMASHITE
    # ashlaeblume, june 2019
 *****************************
///////////////////////////////

Clock.bpm = 150

#a_bass = [a0, a1, a2, a3, a4, a5, a6, a7, a8]
#a0, a1 -> b0, b1, b2, b3, b4


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

b3 >> soft([9,3,7,0,11,3,7,0], dur=(9/3), pan=(-0.7,0.7), amp=1.9)

b4 >> viola([4,5,8,9], dur=[3/2,3/2,3/2], pan=0.5, amp=.7)

drums = [d1, d2, d3, d4, d5, d6, d7, d8, p0, p1, p2, p3, p4, p5, p6, p7]

b4.stop()
d0 >> play("  x-x[---]x-o-(  -x[--o]){-oxx}", sample=[3,2], pan=[-0.4], amp=1)
#d9 is a trial drum beat to test for equivalence with d0
d9 >> play("  x-x[---]x-o-xx", sample=[3,2], pan=[-0.4], amp=1)


d1 >> play("(x--x,xo  ox)([oo],[---])x-x", sample=4, pan=[0.4], amp=.7)

d2 >> play("x-oox--o([xx-]o-x,xo    ox)", sample=1, pan=[-1.6, 1.6], amp=.8)

d3 >> play(("x   "), amp = 0.9)

d0.stop()
d1.stop()
d2.stop()
d3.stop()

d4.stop(); d5.stop(); d6.stop(); d7.stop();
#blend out a0, a1 bass and blend a2 bass with b4 viola

a2 >> bass([9,5,4,6,3,2,0,4],dur=[2,2,1,3,2,3,1,2],pan=[-.2,.2],amp=1.1)
a1.stop()

#upbeat happy calypso
#a3-> b5, b6, b7
#drums-> d0, d1, d2, d3

a3 >> bass([0,(3),(4,2),(6,11)], dur=[2,2,2,2], pan=(-0.6,0.6), amp=1)
a3.stop()
a2.stop()

b5 >> pluck([2,9,4,[(0,4),(3,5)]], dur=[1,1/2,1,1,1/2,1], amp=2.7)
b5.stop()

b6 >> bell([0,2,4,6,9,10], dur=[1/2,1,1,1/2,1,1], amp=2.2)
b6.stop()
b7 >> dub([0, 2, 4, 1, 6], amp=.3)
b7.stop()


~~~~~~~~~~~
 ** inf **
 ** fin **
~~~~~~~~~~~
