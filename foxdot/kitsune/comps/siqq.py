Clock.bpm=145

P0 = 'wert'
P1 = 'yuio'
P2 = 'pasd'
P3 = 'fghj'
trill=['iIiI'], ['eEeE'], ['wWwW']

r0 >> play(
        "XxVv"
        , dur=1/2
        , amp=1
        , room=var([0.6,0.9],16)
        , mix=0.3
        , lpf=var([800,4000],32)
        , hpf=var([0,200],8)
        , echo=3
        , pan=PSine(3)
        ).every(32,'stutter')
"""
v0 >> play(
        "qwertyuiopasdfghjklzxcvbnm!@#$%^&*"
        )

xx >> play(
        "eertyuiopasdfghjklxcvnm-"
        #, chop=1
        ).every(8,'stutter')
#oh >> play("w")
"""

xy >> play(
        "(vnm-lxc)"
        , lpf=var([400,900],32)
        , spin=4
        ).every(16,'stutter')
#yy.stop()
#xz.stop()

xz >> play(
        "wertyuiopasdfghj"
        , hpf=linvar([800,1000],8)
        #, dist=0.2
        , chop=4
        ).every(32,'stutter')
#yy.stop()

yy >> play(
        [P0,P1,P2,P3]
        #[P2,P1]
        , lpf=linvar([300,900],16)
        )
#xz.stop()
#xy.stop()


r1 >> play(
        "XxVv"
        , dur=1/2
        , amp=0.7
        #, room=var([0.6,0.9],16)
        , mix=0.3
        , lpf=var([800,6000],64)
        #, hpf=var([0,200],8)#want to do this for dur of 16 every 128...
        #, echo=3
        , pan=PSine(3)
        ).every(32,'stutter').every(128,hpf=0)




nx >> pluck(
        P[P*(0, 1, 4, 4)+3, P*(2, 5, 7, 9)+5]+(-5)
        , amp=[0.5, 0.7, 0.8, 0.6]
        , pan=PStep(3, P*(-1, 1))
        , lpf=var([1400,6000],16)
        )

nz >> stretch(400)
help(stretch)
