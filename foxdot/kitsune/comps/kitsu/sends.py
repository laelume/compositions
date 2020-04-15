# sends.py
def init():
    global mix0, fade
    mix0=[1
        , 0
        , 0
        , 0
        , 0
        , 0
        , 0
        , 0
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
