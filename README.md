op-amp-analogy
==============

This is a Python implementation of a hydraulic analogy of the operational principles
of an "Operational Amplifier" or Op-Amp, where electrical current and voltage are 
represented by water flow and water pressure respectively.

The op-amp is a vital component in analog electronics, it provides the amplification at
each stage that allows the computational results of that stage to be passed on to the
next stage without attenuation.

This repo contains two scripts, OpAmpAnalog.py, which is just a simple op-amp. and 
OpAmpAnalogFb.py which is a simple op-amp with feedback.

OpAmpAnalog.py simulates just the op-amp, with non-inverting (+) and inverting (-) inputs
controlled by sliders representing water pressure acting as voltage. When the voltage on the 
non-inverting input (+) exceeds that of the inverting input (-), the
piston moves toward the left and the op-amp outputs the maximum pressure, corresponding to 
+15 volts, whereas when the voltage on the inverting input exceeds that on the non-inverting 
input the piston moves to the right, and the op-amp outputs the minimum pressure corresponding
to -15 volts. 

So the op-amp is a simple bang-bang comparator when used in this way. 

A "Function Line" checkbox is provided that, when selected, plots an orange function line superimposed on the 
piston showing the positive and negative saturation values at either end, and a small linear section in the middle,
where the output of the op-amp is a linear function of the piston position. This linear portion is significant, 
because under normal circumstances the op-amp spends almost all of its time
in the linear range, as will become apparent in the feedback version.

A "Pause" checkbox pauses the simulation, and allows the piston position to be controlled directly 
with the sliders, where the piston position equals the difference of non-inverting (+) minus inverting (-)
inputs.

The second script, OpAmpAnalogFb.py simulates an op-amp with a feedback connection from the output back to
the inverting input, to provide a negative-feedback loop. When the non-inverting input (+) pressur is increased,
again the output pressure is increased, but that increased output feeds back to join the inverting input (-) where
it helps push the piston back toward the right, until the pressure on opposite sides of the piston is equal,
and the piston stops in dynamic equilibrium. Any increase of the non-inverting input pushes the piston further
left, while also increasing the negative feedback, which pushes the piston back to the right to equalize the
pressure across it again.

If the inverting input is set to zero, the op-amp behaves as a "follower", the output "follows" whatever 
voltage is found on the non-inverting input and copies it on the output, but this is a "regulated" output,
i.e. if a resistor or other load is put on the output, the op-amp will not allow the load to drag the 
voltage down, it will provide extra power to maintain the voltage on the ouput matching that on the
non-inverting input.

If the non-inverting input is set to zero, then the op-amp behaves as a "negative follower", following
the negative of the voltage present on the inverting input. This provides a simple means to negate
any given input.



