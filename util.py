#!/usr/bin/env python3

def get_note_index(d, value):
    """ look up dict key from value """
    for k, v in d.items():
        if v.fname == value:
            return k
