# main.py
from . import sends
from . import returns

sends.init()
returns.mixer()

Clock.bpm=111.33

#fade=linvar([0.5,0], [16,inf], start=now)

nx >> pluck(
    #P[P*(0,1,4,4)-1, P*(2,5,7,9)-4, P*(8,7,6,5)+1, P*(4,3,2,1)-1]-[4,3,2,1]
    P[P*(0,2,4,6)-5, P*(0,4,2,6)-4, P*(6,0,2,4)+1, P*(6,2,4,0)-4]-0
    , dur=1
    , amp=mix[0]
    , pan=PStep(3, P*(-1,1))
    ).every(8,'mirror'
    )

sx >> ambi(
    P[-9, -8, -7, -10, -11, -5, -4, -6]
    , dur=8
    , lpf=1000
    , sus=7
    , amp=mix[1]
    ).every(4, 'stutter')

ny >> pulse(
    P[5,8,4,8,7]-1
    , dur=3
    , pan=PStep(4,P*(-0.3,0.3))
    , amp=mix[2]
    , chop=17
    , echo=0.5
    , sus=4
    , lpf=([1000,7000],128)
    )

xz >> play(
    " h ha (kl)"
    , amp=mix[3]
    , room=0.8
    , pan=PStep(4,P*(-0.5, 0.5))
    ).every(16, 'mirror')

xy >> play(
    "< -- --  >"
    , amp=mix[4]
    , pan=PSine(5)
    , chop=var([8,9],4)
    ).every(8,'stutter')

x0 >> play(
    " ha ha m"
    , amp=mix[5]
    , room=0.8
    , pan=PStep(4,P*(-0.5, 0.5))
    ).every(8, 'mirror')

xx >> play(
    "XxVv"
    , pan=PSine(5)
    , amp=mix[6]
    , chop=10
    #, coarse=0.6
    ).every(8,'stutter'
    #).every(8,'rotate'
    )

    #offlayer(lambda x: (x * 2) + 1))

ts >> pluck(
    P[0,4].arp([1,4])
    , dur=3/2
    , amp=mix[7]
    , pan=PStep(3, P*(-0.5,0.5))
    )
