print(SynthDefs)

# b = bass, d = drums, everything else = fair game!

Clock.bpm = 160

a1 >> spark([2,6,5,0,1,5,4,0], delay = (0))

b1 >> sawbass([0,1,4], dur=4)

d1 >> play("[xxxx] oo [xxx]-- --", )

d2 >> play("(ooooo)")

triad_0 = (0,2,4)
triad_1 = (2,4,7)
triad_2 = (4,7,9)

dom7_0 = (0,2,4,6)
dom7_1 = (2,4,6,7)
dom7_2 = (4,6,7,9)
dom7_3 = (6,7,9,11)



i1 >> gong([dom73])
