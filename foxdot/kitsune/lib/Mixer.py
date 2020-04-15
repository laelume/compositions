"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        GAIN  MIXERS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# mix0[0] -> mix[0] -> d0.amp
class Mixer:
    mix0=[1
        , 0
        , 0
        , 0
        , 0
        , 0 #H
        , 0
        , 0
        , 0
        ]
    mix1=[1
        , linvar([0.4, 1.5], 6)
        , linvar([0.5, 2], 4)
        , 0.7
        , 0.7
        , 0 #H
        , 1
        , 0
        , 0
        ]
    mix2=[1
        , 1
        , 1
        , 1
        , 1
        , 1 #H
        , 1
        , 1
        , 1
        ]
    fade=[linvar([1, 0], [32,inf],start=now)
        , linvar([1, 0], [32,inf],start=now)
        , linvar([1, 0], [32,inf],start=now)
        , linvar([1, 0], [32,inf],start=now)
        , linvar([1, 0], [32,inf],start=now)
        , linvar([1, 0], [32,inf],start=now)
        , linvar([1, 0], [32,inf],start=now)
        , linvar([1, 0], [32,inf],start=now)
        , linvar([1, 0], [32,inf],start=now)
        ]
