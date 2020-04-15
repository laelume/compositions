# sends.py

global mix0, fade
mix0=[1
    , 0
    , 0
    , 0
    , 0
    , 0
    , 0
    ]
fade=[expvar([1, 0], [16,inf], start=now)
    , expvar([1, 0], [16,inf], start=now)
    , expvar([1, 0], [16,inf], start=now)
    , expvar([1, 0], [16,inf], start=now)
    , expvar([1, 0], [16,inf], start=now)
    , expvar([1, 0], [16,inf], start=now)
    , expvar([1, 0], [16,inf], start=now)
    , expvar([1, 0], [16,inf], start=now)
    ]
