# Apache [cover] by The Incredible Bongo Band (1973)
# https://youtu.be/WY-Z6wm6TMQ
# Transcription by laelume

Clock.bpm=110

# bongo solo!
c0 >> play('c',sample=[1,1,1,1,1,1,0,1,1,1,1,1,0],dur=P[1,1,1,1,1,1,1,2,2,1,1,1,2]/4,amplify=0.67,amp=var([1,0],32),delay=0.088)

# hihat for keeping time
h0 >> play('-',sample=[2],amplify=0.5,dur=P[1],delay=0.04)

# bass drum
b0 >> play('VV   V  ',dur=P[2]/4,amplify=0.35,delay=0.01)

# snare pattern 1st half
s0 >> play(' i',sample=[5],amplify=0.4,dur=P[1],delay=0.03)

# snare examples
#s1 >> play('ii i',sample=[4],amplify=0.4,dur=P[2,1,2,4]/4,delay=0.03)
#s2 >> play('ii i',sample=[4],amplify=0.4,dur=P[1,1,2,4]/4,delay=0.03)
#s3 >> play('ii i',sample=[4],amplify=0.4,dur=P[0.5,1,2,4.5]/4,delay=0.03)
#s4 >> play('ii i',sample=[4],amplify=0.4,dur=P[1,2,1,1]/4,delay=0.03)
#s5 >> play('i ',sample=[4],amplify=0.4,dur=P[1,0.5,1,2,0.5]/2,delay=0.03)
#sounds pretty cool but not quite what we want
#s6 >> play('i ',sample=[4],amplify=0.4,dur=P[1,0.5,2,0.5]/2,delay=0.03)
#getting closer but not there yet!
#s7 >> play('i ',sample=[4],amplify=0.4,dur=P[0.25,0.25,2,1.5]/2,delay=0.03,amp=var([0,1],2))
# snare pattern 2nd half
#s8 >> play(' iiii',sample=[2],amplify=0.2,dur=P[1,1,2,3,1]/4,delay=0.03,amp=var([0,1],[8.25,7.75]))
# snare patt 2nd half, different duration
#s9 >> play(' iiii',sample=[2],amplify=0.2,dur=P[1,1,2,3,1]/4,delay=0.03,amp=var([0,1],[12.25,3.75]))

sx >> play(' iii i',sample=[2],amplify=0.2,dur=P[2,1.5,1,0.5,1,2]/2,delay=0.03,amp=var([0,1],[32]))

# alternating open - closed hihat pattern
h5 >> play('-',sample=[2,3,1,2],amplify=0.5,dur=P[1]/2,delay=0.04)

# alt hat, a bit better with 2 different sounds and samples
h6 >> play('NN--',sample=[3,0,2,0],amplify=0.4,dur=P[1]/2,delay=0.05,amp=var([1,0,1,0],[8,8,8,72]))

h7 >> play('NN----NN',sample=[3,0,2,0],amplify=0.4,dur=P[1]/2,delay=0.05,amp=var([1,0],[16,48]))
