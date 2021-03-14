# Give It Up or Turn It a Loose by James Brown (1969)
# https://youtu.be/921kqkHOHDo
# Transcription by laelume

Clock.bpm=113.7.

# closed hihat with stick
h0 >> play('-',dur=P[1]/2,amplify=0.9,delay=0.026)

# snare, pretty laid back to create a big pocket
s0 >> play(' -',sample=[2],dur=P[2,2]/2,amplify=2.1,delay=0.073)

# ride cymbal -- switching every X# of bars -- use vars to switch with
r0 >> play('~',sample=[0],amplify=0.7,dur=P[1]/2,delay=0.04,amp=var([0,1],64))

# bassdrum 1st half
b0 >> play('vv vv',dur=P[1.5,2.5,1,1.5,1.5]/2,amplify=0.7,delay=0.026)

# conga!

# not quite right ...
c0 >> play('cc    cccc  ',sample=[0],dur=P[2]/8,amplify=0.2,amp=1 )

# Conga amplitude variation
c0 >> play('cc    cccc  ',sample=[0],dur=P[2]/8,amplify=0.2,amp=var([1,0],[2]) )

# finally, the beat: 1st conga variation
c0 >> play('cc  cc   c  cc  ',sample=[0],dur=P[2]/8,amplify=1.1,amp=1,delay=0.088)

# 2nd conga variation
c0 >> play('cc  cc   cccc  ',sample=[0],dur=P[2]/8,amplify=0.2,amp=1,delay=0.085)

# claps at the end
p0 >> play('h',sample=[2],dur=P[1],amplify=1.1,delay=0.011,amp=var([0,1],[128,64]))
p1 >> play('h',sample=[3],dur=P[1],amplify=0.6,delay=0.018,amp=var([0,1],[128,64]))
