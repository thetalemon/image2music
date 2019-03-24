#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pretty_midi
import sys

def makeNote(note, startTime, endTime):
    note_number = pretty_midi.note_name_to_number(note)
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=startTime, end=endTime)
    return note

def makeSound():
    argsList = ['C', 'D', 'E', 'F']

    # argsList = ['C']
    pm = pretty_midi.PrettyMIDI(resolution=960, initial_tempo=120)
    instrument = pretty_midi.Instrument(0)

    list = []

    for item in argsList :
        noteName = item + '4'
        print(noteName),
        list.append(noteName)

    noteTime = 0
    for item in list:
        instrument.notes.append(makeNote(item, noteTime, noteTime+1))
        pm.instruments.append(instrument)
        noteTime = noteTime +1

    return pm
