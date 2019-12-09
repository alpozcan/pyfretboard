#!/usr/bin/env python3
import theory

class String():
    def __init__(self, name):
        self.name = name
        self.notes = Fretboard.t.get_note_sequence(name, Fretboard.HIGHEST_FRET)

class Fretboard():
    """ Abstraction of a guitar fretboard """

    HIGHEST_FRET = 15
    TUNINGS = {
        'standard': [ 'E2', 'A2', 'D3', 'G3', 'B3', 'E4' ]
    }

    t = theory.Theory()

    def __init__(self, tuning='standard'):
        self.strings = { s : String(s) for s in Fretboard.TUNINGS[tuning] }

    # def __str__(self):
    #     return [ [ n for n in s.notes ] for s in self.strings ] # to fix

class Guitar():
    """ The greatest instrument mankind has invented """

    def __init__(self):
        self.fretboard = Fretboard()

