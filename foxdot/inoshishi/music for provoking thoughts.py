print(SynthDefs)

Clock.bpm=140

a1 >> bass([12,8,7], dur=(4,7,5,3), pan=(-0.4,0.4), amp=.4)

a0 >> bass([7,3,2], dur=(4,7,5,3), pan=(-0.8,0.8), amp=.4)

b0 >> space([7], dur=4, amp=.3)

b1 >> bell([3,2,3,1], dur=[3,2], amp=.3)

d0 >> play("x- xo", sample=5, pan=[-0.4,0.4], amp=.5)

d1 >> play("(x  -x,-  -o)  o-x-oxx ", sample=9, pan=[-0.4,0.4], amp=.2)


