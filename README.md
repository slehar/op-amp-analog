op-amp-analogy
==============

This is a Python implementation of a hydraulic analogy of the operational principles
of an "Operational Amplifier" or Op-Amp.

OpAmpAnalog.py simulates just the op-amp, with non-inverting (+) and inverting (-) inputs.
When the voltage on the non-inverting input exceeds that of the inverting input, the
op-amp outputs +15 volts, otherwise it outputs -15 volts. So it is a simple bang-bang 
comparator when used by itself.

OpAmpAnalogFb.py simulates an op-amp with a feedback connection from the output back to
the inverting input, to provide a negative-feedback loop that makes the op-amp open its
valve until the pressures (voltages) on both sides of the piston are equal.

A checkbox for Show Function is provided to show an orange function line superimposed on the
piston.

A checkbox for Pause pauses the simulation, but also allows the piston to be moved directly with
a slider to demonstrate the effects of piston location.


