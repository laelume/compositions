all_drums = [d0, d1, d2, d3, d4, d5, d6, d7, d8, p0, p1, p2, p3, p4, p5, p6, p7]

# Parameter defs have to be after initializations
lopa=lopa0
hipa=hipa0
mix=mix0
#mix=linvar([mix1,mix2],8)
#

dur0=[]
dur1=[]
dur2=[]
dur3=[]
durations=[dur0,dur1,dur2,dur3]


this=[d0, da, db, d1, d2]
next=[d3, d4, d5, d6, d7]
mini=[d0, da, d2]
micro=[d0, db, d3]


params=[]
allpatterns=[]
numpatterns=len(allpatterns)
for i in range(numpatterns):
    for item in allpatterns:
        allpatterns[i].thisparameter=params[0]
