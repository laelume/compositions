print(Samples)

xy >> play(
        "<vnm-lxc><    rr  rr    r >"
        , lpf=var([400,900],32)
        , spin=4
        ).every(16,'stutter'
        #).every(16,'stutter'
        #).every(8,'mirror'
        )
