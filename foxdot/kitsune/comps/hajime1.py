"""
///////////////////////////////
 ****************************
        HAJIMEMASHITE
    ashlaeblume, june 2019
 ****************************
///////////////////////////////
"""
"""
- Network synchronisation, run:
```python
Clock.connect("<ip address>")
```
"""
#Clock.connect("<some_ipaddress>")
Clock.bpm = 143
def onlyThis(thisitem, somegroup, *anotheritem):
    for item in somegroup:
        if item is not thisitem:
                if item is not anotheritem:
                        item.stop()
fad=linvar([1,0],[32,inf],start=now)
allbass=[a0,a1,a2,ax]
allharmony=[b0,b1,b2,b3,b4]
bassline=[ [(0,9), (7,3)] #a0
        , [ (0,9),(7,3),(5,8),(0,5),(4,10) ] #a1
        , [ 9,5,4,6,3,2,0,4 ] #a2
        , [ (7,3) ] #ax
        ]
harmony=[ [11, 10, 9] #b0.1=
        , [7, 6, 5] #b0.2
        , [(0,9),(3,7),11,(0,2)] #b1
        , [0,4,5,7] #b2
        , [9,3,7,0,11,3,7,0] #b3
        , [4,5,8,9] #b4
        ]
a0 >> bass([bassline[0]], dur=4, pan=(-0.6,0.6), amp=1)
onlyThis(a0, allbass)

a1 >> bass([bassline[1]], dur=4, pan=(-0.6,0.6), amp=1)
onlyThis(a1,allbass)
b0 >> charm(harmony[0], dur=[2/4, 4/4, 6/4], amp=linvar([1,0],[64,inf],start=now))
#onlyThis(b0,allharmony)
#b0 >> charm(harmony[1], dur=[2/4, 4/4, 6/4], amp=1)

b4 >> viola(harmony[5], dur=[3/2,3/2,3/2], pan=0.5, amp=linvar([1,0],[64,inf],start=now))

b2 >> pluck(harmony[3], dur=[3/3,3/2,3/2], amp=linvar([1,0],[64,inf],start=now))

b3 >> soft(harmony[4], dur=(9/3), pan=(-0.7,0.7), amp=linvar([1,0],[64,inf],start=now))

b1 >> scatter(harmony[2],dur=3,pan=(-0.2,0.2),amp=linvar([1,0],[64,inf],start=now))


"""
TRANSITION:
blend out a0, a1 bass and blend a2 bass with b4 viola

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ^^_^^   ^^_^^   HAPPY CALYPSO   ^^_^^   ^^_^^
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
#this_bass=[a2, a3]
#this_melody=[b5, b6, b7]
#this_drums=[d0, d1, d2, d3]

a2 >> bass(bassline[2],dur=[2,2,1,3,2,3,1,2],pan=[-.2,.2],amp=1.1)
onlyThis(a2,allbass)

# ENDING (back to the top)
ax >> bass([bassline[3]], dur=4, pan=(-0.6,0.6), amp=.9)
onlyThis(ax, allbass)
