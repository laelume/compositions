# Funky Drummer by James Brown (1970)
# https://youtu.be/AoQ4AtsFWVM
# Transcription by laelume

Clock.bpm=98

# full bass drum up front
b0 >> play('vv vvvv vvv',dur=P[2,2,6,3,3,2,2,4,2,3,3]/4,amplify=2,delay=0.01,pan=-0.1)

# a couple bass hits for keeping a bigger sense of time
b1 >> play('XX ',dur=P[2,2,28]/4,amplify=1.3,pan=0.2)

# bassdrum 1st half
b2 >> play('vv vv',dur=P[2,2,6,3,3]/4,amplify=0.2,delay=0.01,pan=0.5)

# bassdrum 2nd half
b3 >> play('vv vvv',dur=P[2,2,4,2,3,3]/4,amplify=0.2,delay=0.01,pan=0.5)

# ride cymbal
r0 >> play('~',sample=[0],amplify=0.8,dur=P[1]/2,delay=0.04)

# closed hihat with stick
h0 >> play('---- -- - -- -  ',dur=P[1/4],amplify=1.2,delay=0.06,pan=-0.5)

# hihat open - 1st pattern
hx >> play(' -',sample=[0],dur=P[3,1]/2,amplify=0.5,delay=0.06,pan=-0.5)

# hihat open - 2nd pattern
hy >> play(' -',sample=[3],dur=P[4,1,2,1]/2,amplify=0.5,delay=0.06,pan=-0.5)

# hihat open - variation on 1st pattern
hi >> play(' - ',sample=[0],dur=P[3,1,4]/2,amplify=0.5,delay=0.06,pan=-0.5)

# open hihat amp experiment -- see if it lines up!
# 1st open hihat pattern
hj >> play(' -',sample=[0],dur=P[3,1]/2,amplify=0.8,delay=0.06,amp=var([1,0],[6,2]) ,pan=0.4)

# 2nd open hihat pattern
hk >> play(' -',sample=[3],dur=P[4,1,2,1]/2,amplify=0.5,delay=0.06,amp=var([0,1],[6,2]),pan=-0.4)

# snare drum most of the time
s0 >> play(' -----',sample=[2],dur=P[4,3,2,2,1,4]/4,amp=var([1,0],[48,16]),amplify=0.9,delay=0.03,pan=0.5)

# snare sometimes
s1 >> play(' ----',sample=[2],dur=P[4,3,2,3,4]/4,amp=var([0,1],[48,16]),amplify=0.9,delay=0.03,pan=-0.5)
