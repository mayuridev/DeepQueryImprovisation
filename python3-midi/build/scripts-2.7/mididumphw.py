#!/usr/bin/python2
"""
Print a description of the available devices.
"""
import midi.sequencer as sequencer

s = sequencer.SequencerHardware()

print(s)
