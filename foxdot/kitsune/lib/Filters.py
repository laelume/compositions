"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FILTERS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
class Filters:
    lp=[0,500,1000,1500,2000,3000,4000,5000,10000]
    lopa0=[0
        , 0
        , 0
        , 0
        , 0
        , 0
        , 0
        , 0
        , 0
        ]
    lopa1=[lp[1]
        , lp[3]
        , lp[1]
        , lp[3]
        , lp[1]
        , lp[3]
        , lp[1]
        , lp[3]
        , lp[1]
        ]
    lopa2=[lp[2]
        , lp[2]
        , lp[2]
        , lp[2]
        , lp[2]
        , lp[2]
        , lp[2]
        , lp[2]
        , lp[2]
        ]
    lopa3=[lp[5]
        , lp[5]
        , lp[5]
        , lp[5]
        , lp[5]
        , lp[5]
        , lp[5]
        , lp[5]
        , lp[5]
        ]
    lopa4=[ linvar( [ lp[2], 20000 ], 128, start=now )
          , linvar( [ lp[2], 20000 ], 128, start=now )
          , linvar( [ lp[2], 20000 ], 128, start=now )
          , linvar( [ lp[2], 20000 ], 128, start=now )
          , linvar( [ lp[2], 20000 ], 128, start=now )
          , linvar( [ lp[2], 20000 ], 128, start=now )
          , linvar( [ lp[2], 20000 ], 128, start=now )
          , linvar( [ lp[2], 20000 ], 128, start=now )
          , linvar( [ lp[2], 20000 ], 128, start=now )
        ]
    hipa0=[8000
        , 15000
        , 4000
        , 0
        , 0
        , var([0,4000], [28,4])
        , 0
        , 0
        , 0
        ]
    hipa1=[0
        , 0
        , 0
        , 0
        , 0
        , 0
        , 0
        , 0
        , 0
        ]
