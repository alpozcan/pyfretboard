#!/usr/bin/env python3
import theory

class String():
    def __init__(self, name):
        self.name = name
        self.notes = Fretboard.t.get_note_sequence(name, Fretboard.UP_TO_FRET)

class Fretboard():
    """ Abstraction of a guitar fretboard """

    UP_TO_FRET = 13
    TUNINGS = {
        'standard': [ 'E2', 'A2', 'D3', 'G3', 'B3', 'E4' ]
    }

    t = theory.Theory()

    def __init__(self, tuning='standard'):
        self.strings = { s : String(s) for s in Fretboard.TUNINGS[tuning] }

    def __str__(self):
        out = ''
        fret_numbers = '\t'.join([str(fret) for fret in range(Fretboard.UP_TO_FRET)])
        out += fret_numbers + '\n'
        for string in self.strings.values():
            out += '\n'
            for n in string.notes:
                out += f'{n}\t'
        out += '\n'*2 + fret_numbers
        return out

    def section(self, from_fret=0, to_fret=UP_TO_FRET):
        note_matrix = []
        for string in self.strings.values():
            note_matrix.append( [ note.i for note in string.notes[from_fret:to_fret] ] )
        return note_matrix

class Guitar():
    """ The greatest instrument mankind has invented """

    def __init__(self):
        self.fretboard = Fretboard()

