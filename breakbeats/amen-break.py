# Classic breakbeat from Amen Brother by The Winstons (1969)
# https://youtu.be/GxZuq57_bYM
# Transcription by laelume

Clock.bpm=102.6

# ride cymbal
h0 >> play('~',sample=[0],amplify=0.7,dur=P[1]/2,delay=0.04)

# bass drum
b0 >> play('vv ',dur=P[2,2,6,1,1,4]/4,amplify=3.0,delay=0.01)

# snare
s0 >> play(' ----',sample=[2],amplify=0.9,dur=P[4,3,2,3,4]/4,delay=0.03)

# Using amplitude (and a little duration) to change the bass drum -- same results musically!!
b0 >> play('v ',dur=1/4,amplify=0.2,delay=0.01,amp=var([1,0],[1,3]))

b1 >> play('v ',dur=1/8,amplify=0.2,delay=0.01,amp=var([0,1,0],[2.5,0.5,1]))

s0 >> play(' ----',sample=[2],amplify=0.6,dur=P[4,3,2,3,4]/4,delay=0.03)
