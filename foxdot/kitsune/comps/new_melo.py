"""
newmelody
eastbound in a plane over the atlantic, 4.4.2020
@ashlaeblume @ukiyobang
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
bassline=[ P[2,5,6,9]
        , [0,3,4,3,4,0]
        , []
        , []
        ]
harmony=[ []
        , []
        , []
        , []
        ]
b0 >> bass(bassline[0], dur=[4,4,4,4], pan=-0.5, amp=1).every(4,*2)

b1 >> bass(bassline[1], dur=[2,1,1,1,3,8], scale=Scale.egyptian, pan=0.5, amp=1)

help(every())
print(P[2:15:3])

print(Scale.names())
