#!/usr/bin/env python3

S = '\u266F' # sharp sign
F = '\u266D' # flat sign

from itertools import cycle
from util import get_note_index

class Note():
    def __init__(self, i, name, octave):
        self.i = i # note index
        self.name = name
        self.octave = octave
        self.fname = f'{self.name}{self.octave}'

    def __str__(self):
        return self.fname

class Interval():
    def __init__(self, semitones, inversion=False):
        self.name = Theory.I[semitones]
        self.semitones = semitones if not inversion else semitones * -1
        self.inversion = Interval(abs(semitones - 12), inversion=True) if not inversion else None
        self.is_inversion = inversion

    def __str__(self):
        return ', '.join([  f'name: {self.name}',
                            f'semitones: {self.semitones}',
                            f'inversion_name: {self.inversion.name}',
                            f'inversion_semitones: {self.inversion.semitones}'
                        ])

class Chord():
    def __init__(self, name, inversion=0, position=None):
        # tokenise chord name to parse root note, chord quality and any alterations
        # self.root = 
        # self.quality = 
        # self.alterations = 

        self.inversion = inversion
        self.position =  position

class Theory():

    NOTE_NAMES = cycle([ 'A' , f'A{S}/B{F}', 'B', 'C', f'C{S}/D{F}', 'D', f'D{S}/E{F}', 'E', 'F', f'F{S}/G{F}', 'G', f'G{S}/A{F}' ])

    I = { # intervals
        0: 'unison',
        1: 'm2',
        2: 'M2',
        3: 'm3',
        4: 'M3',
        5: 'p4',
        6: 'tritone',
        7: 'p5',
        8: 'm6',
        9: 'M6',
        10: 'm7',
        11: 'M7',
        12: '8ve'
    }

    def __init__(self):

        # populate notes
        octave = 0
        self.notes = {}
        for i in range(1, 89): # the 88 piano keys correspond to note indices (A0 to C8)
            name = next(Theory.NOTE_NAMES)
            if name == 'C':
                octave += 1
            self.notes[i] = Note(i, name, octave)

        # populate intervals


        # populate chords


    def get_note_sequence(self, start_note, num_notes, step=1):
        """ return a given note range """
        start_idx = get_note_index(self.notes, start_note)
        return [ self.notes[n] for n in range(start_idx, start_idx + (num_notes * step), step) ]

    def get_note(self, note):
        """ return a note """
        return self.get_note_sequence(note, 1)[0]
