(// Sinc function is sinx/x, so: 
SynthDef(\sinc, { | out, freq = 440, sustain = 1, pan, amp = 0.1, width = 0.25 |
	var son = SinOsc(freq)/freq;
	OffsetOut.ar(out, Pan2.ar(son, pan, amp));
}, \ir ! 1).add;
)
// \ir is a static control rate, set at start of synth implementation



SynthDef(\fixedwave, { | out, freq = 440, sustain = 1, pan, amp = 0.1, width = 0.25 |
	var env = LFGauss.ar(sustain, width, loop: 0, doneAction: 2);
	var son = FSinOsc.ar(freq, pi, env);
	OffsetOut.ar(out, Pan2.ar(son, pan, amp));
}, \ir ! 2).add;


{Impulse.ar(440)}.play;

(// Arguments of SinGrain.ar(trigger, dur, freq, mul, add)
// Changing the argument of Impulse.kr(freq, phase, mul, add) determines trigger speed
    SynthDef(\singrains, {arg gate = 1, amp = 1;
    Out.ar(0,
        SinGrain.ar(Impulse.kr(5), 0.1, WhiteNoise.kr.range(440, 880), 
            EnvGen.kr(
                Env([0, 1, 0], [1, 1], \sin, 1),
                gate,
                levelScale: amp,
                doneAction: 2)
            )
        )
    }).play;
)
