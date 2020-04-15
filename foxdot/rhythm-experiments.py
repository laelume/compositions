Clock.bpm = 120
print (Clock.latency)
print(BufferManager())


(
#inspired by PZip("Vs", "  n  ") from Ryan Kirkbride https://www.youtube.com/watch?v=CXrkq7u69vU
d0 >> play(
    PZip("V(s,h,k)", "n  n  "),
    sample=2,
    hpf=var([0,4000], [28,4]),
#    amp=linvar([0.5,1.5])
    amp=1
    ).every(3, 'stutter', dur=1),
#pattern ideas
#play(PZip("V(a:0,s,h,k)", "n  n  "))
)

d1 >> rave([0,2,1,3],
    dur=4,
    amp=0.2,
    pan=linvar(0,2)
    ).every(32, 'stutter', dur=2)

print(SynthDefs)

# Character types for play function
#melodic: qweajzcb
#textural: kl
#rhythmic: tyuiopsdfghxvnm
(
#pattern based on ashlaeblume composition "HAJIMEMASHITE"
#d3 >> play("  xtx[vvv]x( -x[--k])rand(k,l)",
d3 >> play("  xtx[vvv]x( -x[--k]){kl}",
    sample=[3,2],
    pan=[-0.7, 0.7],
    amp=linvar([2,0])
)
)

PDur()
'mirror'
.layer
var()
PZip()
rate=
bits=
fmod=(0,1)
oct=var([4,5])
lpf=linvar([600,5000])
pan = linvar([-1,1],4) + var([0,2,4]-3)
rate=P[:64]*(1,2)
delay=(0,.5)
chop=4
dur=PDur(3,8)
rate=every(5,'stutt')
sus=4



p1 >> blip(
    [
    var([0,2,4]),
    [3,4,5],
    var([4,8,9]),
    [6,7,11]
    ],
    dur=1/2,
    sus=2.5,
    oct=(6,7)
)
p1.stop()


# Try some other mathematical operators and see what results you get.
print(P[1,2,3] * (1,2))

# Pattern objects also automatically lace any nested lists

# Normal list
# Prints as [0,1,2,[3,4],5]
for n in [0,1,2,[3,4],5]:
    print(n)

# Pattern
# Prints as [0,1,2,3,5,0,1,2,4,5]
for n in P[0,1,2,[3,4],5]:
    print(n)

pattern=[  [  x-x[---]x-o-(  -x[--o]){-oxx}]
