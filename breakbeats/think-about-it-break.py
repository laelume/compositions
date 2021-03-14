# "Think (About It)" by Lyn Collins with James Brown (1972)
# https://youtu.be/HKix_06L5AY
# Transcription by laelume

Clock.bpm=110

# bass drum
b0 >> play('VV   V  ',dur=P[2]/4,amplify=1.2,delay=0.01)

# snare pattern 1st half
s0 >> play(' i',sample=[5],amplify=0.7,dur=P[1],delay=0.03)
# other snare pattern
s1 >> play(' iii i',sample=[2],amplify=0.6,dur=P[2,1.5,1,0.5,1,2]/2,delay=0.03,amp=1)

# hat/cymbals
h0 >> play('NN----NN',sample=[3,0,2,0,3,0,0,5],amplify=0.8,dur=P[1]/2,delay=0.05,amp=1)

#tambourine sounds (shaker)
t0 >> play('s',sample=[1],dur=P[1]/2,amplify=0.7)
t1 >> play('s',sample=[4],dur=P[1]/2,amplify=0.7)

# woodblock sound
w0 >> play('d',sample=[2],dur=P[3,3,4,2,4]/4,amplify=1.1)
